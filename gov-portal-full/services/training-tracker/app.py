from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from supabase import create_client, Client
import os
import redis
import json
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import PlainTextResponse

# Initialize FastAPI app
app = FastAPI(
    title="AI Training Tracker",
    description="Lightweight training management service for AI Governance Portal",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL", "http://localhost:8000")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY", "")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# Initialize clients
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_KEY else None
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

# Metrics
course_enrollments = Counter('training_course_enrollments_total', 'Total course enrollments')
course_completions = Counter('training_course_completions_total', 'Total course completions')
course_progress_updates = Counter('training_progress_updates_total', 'Total progress updates')
api_latency = Histogram('training_api_latency_seconds', 'API endpoint latency')

# ============================================
# MODELS
# ============================================

class TrainingTrack(BaseModel):
    id: str
    name: str
    description: str
    tier: int = Field(ge=1, le=4)
    prerequisites: List[str] = []
    
class Course(BaseModel):
    id: str
    code: str
    title: str
    description: str
    track_id: str
    duration_hours: int
    difficulty: str = Field(pattern="^(beginner|intermediate|advanced|expert)$")
    provider: Optional[str] = None
    tags: List[str] = []
    learning_objectives: List[str] = []
    
class Enrollment(BaseModel):
    user_id: str
    course_id: str
    enrolled_at: datetime
    status: str = Field(pattern="^(enrolled|in_progress|completed|dropped)$")
    progress_percentage: float = Field(ge=0, le=100)
    completed_at: Optional[datetime] = None
    
class Progress(BaseModel):
    enrollment_id: str
    module_id: str
    progress_percentage: float
    time_spent_minutes: int
    last_accessed: datetime
    
class Certificate(BaseModel):
    id: str
    user_id: str
    course_id: str
    issued_at: datetime
    certificate_url: str
    verification_code: str

class TrainingMetrics(BaseModel):
    total_enrollments: int
    active_learners: int
    completion_rate: float
    avg_time_to_complete: float
    satisfaction_score: float
    courses_by_track: Dict[str, int]
    top_courses: List[Dict[str, Any]]
    weekly_progress: List[Dict[str, Any]]

# ============================================
# TRAINING TRACKS
# ============================================

@app.get("/tracks", response_model=List[TrainingTrack])
async def get_training_tracks():
    """Get all training tracks (Tier 1 + 4 specialized)"""
    tracks = [
        {
            "id": "tier1",
            "name": "Fundacional GenAI",
            "description": "Conceptos básicos de IA Generativa para todos",
            "tier": 1,
            "prerequisites": []
        },
        {
            "id": "track-a",
            "name": "Track A: Analysts & Business",
            "description": "IA para análisis de negocio y toma de decisiones",
            "tier": 2,
            "prerequisites": ["tier1"]
        },
        {
            "id": "track-b",
            "name": "Track B: Developers",
            "description": "Desarrollo con IA, APIs, y arquitectura",
            "tier": 2,
            "prerequisites": ["tier1"]
        },
        {
            "id": "track-c",
            "name": "Track C: Marketing & Creative",
            "description": "IA para contenido, diseño y marketing",
            "tier": 2,
            "prerequisites": ["tier1"]
        },
        {
            "id": "track-d",
            "name": "Track D: Compliance & Risk",
            "description": "Gobierno, ética y gestión de riesgos de IA",
            "tier": 2,
            "prerequisites": ["tier1"]
        }
    ]
    return tracks

# ============================================
# COURSES
# ============================================

@app.get("/courses", response_model=List[Course])
async def get_courses(track_id: Optional[str] = None):
    """Get all courses or filter by track"""
    courses = [
        {
            "id": "ai-101",
            "code": "AI-101",
            "title": "Fundamentos de IA Generativa",
            "description": "Introducción a conceptos básicos de GenAI",
            "track_id": "tier1",
            "duration_hours": 8,
            "difficulty": "beginner",
            "provider": "internal",
            "tags": ["fundamentals", "genai", "basics"],
            "learning_objectives": [
                "Entender qué es IA Generativa",
                "Conocer casos de uso empresariales",
                "Identificar oportunidades de aplicación"
            ]
        },
        {
            "id": "ai-201",
            "code": "AI-201",
            "title": "Prompt Engineering Avanzado",
            "description": "Técnicas avanzadas para optimizar prompts",
            "track_id": "track-a",
            "duration_hours": 12,
            "difficulty": "intermediate",
            "provider": "anthropic",
            "tags": ["prompts", "optimization", "claude"],
            "learning_objectives": [
                "Dominar técnicas de few-shot learning",
                "Implementar chain-of-thought prompting",
                "Optimizar prompts para diferentes modelos"
            ]
        },
        {
            "id": "ai-301",
            "code": "AI-301",
            "title": "APIs de IA para Desarrolladores",
            "description": "Integración de APIs de OpenAI, Anthropic y Google",
            "track_id": "track-b",
            "duration_hours": 16,
            "difficulty": "advanced",
            "provider": "openai",
            "tags": ["apis", "integration", "development"],
            "learning_objectives": [
                "Integrar APIs de múltiples proveedores",
                "Implementar rate limiting y error handling",
                "Optimizar costos y latencia"
            ]
        },
        {
            "id": "ai-401",
            "code": "AI-401",
            "title": "ISO/IEC 42001 Compliance",
            "description": "Implementación de estándares ISO para IA",
            "track_id": "track-d",
            "duration_hours": 20,
            "difficulty": "expert",
            "provider": "internal",
            "tags": ["compliance", "iso", "governance"],
            "learning_objectives": [
                "Implementar ISO/IEC 42001",
                "Auditar sistemas de IA",
                "Gestionar riesgos de IA"
            ]
        }
    ]
    
    if track_id:
        courses = [c for c in courses if c["track_id"] == track_id]
    
    return courses

@app.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
async def create_course(course: Course):
    """Create a new course"""
    # Cache in Redis
    redis_client.hset(f"course:{course.id}", mapping=course.dict())
    course_enrollments.inc()
    return course

# ============================================
# ENROLLMENTS
# ============================================

@app.post("/enrollments", response_model=Enrollment)
async def enroll_user(enrollment: Enrollment):
    """Enroll a user in a course"""
    # Store in Redis for quick access
    enrollment_key = f"enrollment:{enrollment.user_id}:{enrollment.course_id}"
    redis_client.hset(enrollment_key, mapping={
        "user_id": enrollment.user_id,
        "course_id": enrollment.course_id,
        "enrolled_at": enrollment.enrolled_at.isoformat(),
        "status": enrollment.status,
        "progress_percentage": enrollment.progress_percentage
    })
    
    course_enrollments.inc()
    return enrollment

@app.get("/enrollments/{user_id}", response_model=List[Enrollment])
async def get_user_enrollments(user_id: str):
    """Get all enrollments for a user"""
    # Scan Redis for user enrollments
    pattern = f"enrollment:{user_id}:*"
    enrollments = []
    
    for key in redis_client.scan_iter(match=pattern):
        data = redis_client.hgetall(key)
        if data:
            enrollments.append({
                "user_id": data["user_id"],
                "course_id": data["course_id"],
                "enrolled_at": data["enrolled_at"],
                "status": data["status"],
                "progress_percentage": float(data["progress_percentage"])
            })
    
    return enrollments

# ============================================
# PROGRESS TRACKING
# ============================================

@app.put("/progress/{enrollment_id}")
async def update_progress(enrollment_id: str, progress: Progress):
    """Update learning progress"""
    # Update progress in Redis
    progress_key = f"progress:{enrollment_id}:{progress.module_id}"
    redis_client.hset(progress_key, mapping={
        "progress_percentage": progress.progress_percentage,
        "time_spent_minutes": progress.time_spent_minutes,
        "last_accessed": progress.last_accessed.isoformat()
    })
    
    course_progress_updates.inc()
    
    # Check if course is completed
    if progress.progress_percentage >= 100:
        course_completions.inc()
    
    return {"status": "progress_updated"}

@app.get("/progress/{user_id}/{course_id}")
async def get_course_progress(user_id: str, course_id: str):
    """Get detailed progress for a user in a course"""
    enrollment_key = f"enrollment:{user_id}:{course_id}"
    enrollment = redis_client.hgetall(enrollment_key)
    
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    
    # Get all progress records
    pattern = f"progress:{user_id}:{course_id}:*"
    progress_records = []
    
    for key in redis_client.scan_iter(match=pattern):
        data = redis_client.hgetall(key)
        if data:
            progress_records.append(data)
    
    return {
        "enrollment": enrollment,
        "progress_details": progress_records
    }

# ============================================
# CERTIFICATES
# ============================================

@app.post("/certificates", response_model=Certificate)
async def issue_certificate(certificate: Certificate):
    """Issue a completion certificate"""
    # Store certificate
    cert_key = f"certificate:{certificate.id}"
    redis_client.hset(cert_key, mapping={
        "user_id": certificate.user_id,
        "course_id": certificate.course_id,
        "issued_at": certificate.issued_at.isoformat(),
        "certificate_url": certificate.certificate_url,
        "verification_code": certificate.verification_code
    })
    
    return certificate

@app.get("/certificates/{user_id}", response_model=List[Certificate])
async def get_user_certificates(user_id: str):
    """Get all certificates for a user"""
    pattern = f"certificate:*"
    certificates = []
    
    for key in redis_client.scan_iter(match=pattern):
        data = redis_client.hgetall(key)
        if data and data.get("user_id") == user_id:
            certificates.append(data)
    
    return certificates

# ============================================
# METRICS & ANALYTICS
# ============================================

@app.get("/metrics/training", response_model=TrainingMetrics)
async def get_training_metrics():
    """Get comprehensive training metrics for IMPACT framework"""
    
    # Calculate metrics (simplified for demo)
    metrics = TrainingMetrics(
        total_enrollments=int(redis_client.get("metric:total_enrollments") or 150),
        active_learners=int(redis_client.get("metric:active_learners") or 87),
        completion_rate=float(redis_client.get("metric:completion_rate") or 0.73),
        avg_time_to_complete=float(redis_client.get("metric:avg_completion_time") or 14.5),
        satisfaction_score=float(redis_client.get("metric:satisfaction") or 4.6),
        courses_by_track={
            "tier1": 45,
            "track-a": 32,
            "track-b": 28,
            "track-c": 25,
            "track-d": 20
        },
        top_courses=[
            {"course_id": "ai-101", "title": "Fundamentos GenAI", "enrollments": 145},
            {"course_id": "ai-201", "title": "Prompt Engineering", "enrollments": 89},
            {"course_id": "ai-301", "title": "APIs de IA", "enrollments": 67}
        ],
        weekly_progress=[
            {"week": "2024-W01", "enrollments": 23, "completions": 15},
            {"week": "2024-W02", "enrollments": 31, "completions": 19},
            {"week": "2024-W03", "enrollments": 28, "completions": 22}
        ]
    )
    
    return metrics

@app.get("/metrics/impact")
async def get_impact_metrics():
    """Get IMPACT metrics for training effectiveness"""
    return {
        "implementation": {
            "coverage": 0.75,
            "adoption_rate": 0.68,
            "training_completion": 0.73
        },
        "momentum": {
            "weekly_active_users": 87,
            "engagement_rate": 0.82,
            "content_velocity": 12
        },
        "performance": {
            "skill_improvement": 0.78,
            "assessment_scores": 0.84,
            "practical_application": 0.71
        },
        "acceptance": {
            "satisfaction_score": 4.6,
            "nps": 42,
            "recommendation_rate": 0.89
        },
        "cost_effective": {
            "cost_per_learner": 120,
            "roi": 3.2,
            "time_to_productivity": 21
        },
        "trust": {
            "certification_rate": 0.67,
            "compliance_score": 0.92,
            "quality_assurance": 0.88
        }
    }

# ============================================
# HEALTH & MONITORING
# ============================================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "training-tracker",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/metrics", response_class=PlainTextResponse)
async def prometheus_metrics():
    """Expose Prometheus metrics"""
    return generate_latest()

# ============================================
# LEARNING PATHS
# ============================================

@app.get("/learning-paths/{user_id}")
async def get_personalized_learning_path(user_id: str):
    """Get personalized learning path based on role and progress"""
    # This would integrate with user profile and role
    return {
        "user_id": user_id,
        "current_track": "track-b",
        "completed_courses": ["ai-101"],
        "recommended_next": [
            {"course_id": "ai-201", "reason": "Build on fundamentals"},
            {"course_id": "ai-301", "reason": "Role-specific skills"}
        ],
        "estimated_completion": "2024-03-15",
        "skill_gaps": ["api_integration", "prompt_optimization"],
        "certification_path": [
            {"cert": "AI Fundamentals", "status": "completed"},
            {"cert": "Developer Track", "status": "in_progress"},
            {"cert": "AI Architect", "status": "planned"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)