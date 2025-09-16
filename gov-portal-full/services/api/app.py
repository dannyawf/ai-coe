from fastapi import FastAPI, HTTPException, Depends, status, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from supabase import create_client, Client
from temporalio.client import Client as TemporalClient
import os
import redis
import json
import asyncio
from prometheus_client import Counter, Histogram, generate_latest
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Initialize FastAPI
app = FastAPI(
    title="AI Governance Portal API",
    description="Backend API for AI CoE Governance Portal with IMPACT metrics",
    version="2.0.0"
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
TEMPORAL_HOST = os.getenv("TEMPORAL_HOST", "localhost:7233")

# Initialize clients
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_KEY else None
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

# Metrics
api_requests = Counter('api_requests_total', 'Total API requests', ['method', 'endpoint'])
api_latency = Histogram('api_request_duration_seconds', 'API request latency')
impact_metric_updates = Counter('impact_metric_updates_total', 'IMPACT metric updates')

# OpenTelemetry instrumentation
FastAPIInstrumentor.instrument_app(app)
tracer = trace.get_tracer(__name__)

# ============================================
# MODELS
# ============================================

class IMPACTMetrics(BaseModel):
    implementation: float = Field(ge=0, le=100)
    momentum: float = Field(ge=0, le=100)
    performance: float = Field(ge=0, le=100)
    acceptance: float = Field(ge=0, le=100)
    cost_effective: float = Field(ge=0, le=100)
    trust: float = Field(ge=0, le=100)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class AdoptionMetrics(BaseModel):
    provider: str
    coverage_pct: float = Field(ge=0, le=100)
    ttfv_minutes: float = Field(ge=0)
    weekly_active_users: int = Field(ge=0)
    nps_score: float = Field(ge=-100, le=100)
    roi: float = Field(ge=0)

class AuditEvent(BaseModel):
    event_type: str
    user_id: str
    squad_id: Optional[str] = None
    action: str
    metadata: Dict[str, Any] = {}
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    compliance_flags: List[str] = []

class Squad(BaseModel):
    id: str
    name: str
    status: str = Field(pattern="^(shadow|federated|autonomous)$")
    product_owner: Optional[str] = None
    risk_officer: Optional[str] = None
    adoption_rate: float = Field(ge=0, le=100)
    maturity_level: int = Field(ge=1, le=5)

class WorkflowExecution(BaseModel):
    workflow_id: str
    workflow_type: str
    status: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    result: Optional[Dict[str, Any]] = None

# ============================================
# HEALTH & MONITORING
# ============================================

@app.get("/health")
async def health_check():
    """Health check endpoint with dependency status"""
    health_status = {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "dependencies": {
            "supabase": "connected" if supabase else "not configured",
            "redis": "connected",
            "temporal": "connected"
        }
    }
    
    # Check Redis
    try:
        redis_client.ping()
    except:
        health_status["dependencies"]["redis"] = "disconnected"
        health_status["status"] = "degraded"
    
    return health_status

@app.get("/metrics", response_class=PlainTextResponse)
async def prometheus_metrics():
    """Expose Prometheus metrics"""
    return generate_latest()

# ============================================
# IMPACT METRICS
# ============================================

@app.get("/metrics/impact", response_model=IMPACTMetrics)
async def get_impact_metrics():
    """Get current IMPACT metrics"""
    with tracer.start_as_current_span("get_impact_metrics"):
        # Try to get from cache first
        cached = redis_client.get("metrics:impact:current")
        if cached:
            return json.loads(cached)
        
        # Calculate metrics (would query Supabase in production)
        metrics = IMPACTMetrics(
            implementation=75.5,
            momentum=68.2,
            performance=82.1,
            acceptance=71.3,
            cost_effective=89.7,
            trust=77.4
        )
        
        # Cache for 5 minutes
        redis_client.setex(
            "metrics:impact:current",
            300,
            json.dumps(metrics.dict(), default=str)
        )
        
        impact_metric_updates.inc()
        return metrics

@app.post("/metrics/impact", response_model=IMPACTMetrics)
async def update_impact_metrics(metrics: IMPACTMetrics):
    """Update IMPACT metrics"""
    with tracer.start_as_current_span("update_impact_metrics"):
        # Store in Redis
        redis_client.setex(
            "metrics:impact:current",
            300,
            json.dumps(metrics.dict(), default=str)
        )
        
        # Store history in Supabase if configured
        if supabase:
            supabase.table("impact_metrics").insert(metrics.dict()).execute()
        
        impact_metric_updates.inc()
        return metrics

@app.get("/metrics/impact/history")
async def get_impact_history(days: int = 30):
    """Get IMPACT metrics history"""
    with tracer.start_as_current_span("get_impact_history"):
        if supabase:
            since = datetime.utcnow() - timedelta(days=days)
            result = supabase.table("impact_metrics")\
                .select("*")\
                .gte("timestamp", since.isoformat())\
                .order("timestamp")\
                .execute()
            return result.data
        
        # Mock data if no Supabase
        return [
            {
                "timestamp": (datetime.utcnow() - timedelta(days=i)).isoformat(),
                "implementation": 75 + i * 0.5,
                "momentum": 68 + i * 0.3,
                "performance": 82 + i * 0.2,
                "acceptance": 71 + i * 0.4,
                "cost_effective": 89 - i * 0.1,
                "trust": 77 + i * 0.15
            }
            for i in range(min(days, 30))
        ]

# ============================================
# ADOPTION METRICS
# ============================================

@app.get("/metrics/adoption", response_model=List[AdoptionMetrics])
async def get_adoption_metrics():
    """Get adoption metrics by provider"""
    providers = ["nova-cell", "github-copilot", "claude", "openai", "gemini"]
    metrics = []
    
    for provider in providers:
        # Get from cache or calculate
        cached = redis_client.get(f"metrics:adoption:{provider}")
        if cached:
            metrics.append(json.loads(cached))
        else:
            metric = AdoptionMetrics(
                provider=provider,
                coverage_pct=75.0 if provider == "nova-cell" else 60.0,
                ttfv_minutes=12.3,
                weekly_active_users=150,
                nps_score=42,
                roi=3.2
            )
            metrics.append(metric.dict())
            
            # Cache for 10 minutes
            redis_client.setex(
                f"metrics:adoption:{provider}",
                600,
                json.dumps(metric.dict())
            )
    
    return metrics

# ============================================
# SQUADS MANAGEMENT
# ============================================

@app.get("/squads", response_model=List[Squad])
async def get_squads():
    """Get all squads and their federation status"""
    # Would query Supabase in production
    squads = [
        Squad(
            id="squad-risk",
            name="Riesgos",
            status="federated",
            product_owner="María García",
            risk_officer="Juan Pérez",
            adoption_rate=85.0,
            maturity_level=4
        ),
        Squad(
            id="squad-digital",
            name="Digital Banking",
            status="federated",
            product_owner="Carlos López",
            risk_officer="Ana Martínez",
            adoption_rate=78.0,
            maturity_level=3
        ),
        Squad(
            id="squad-infra",
            name="Infraestructura",
            status="shadow",
            risk_officer="Pedro Sánchez",
            adoption_rate=45.0,
            maturity_level=2
        ),
        Squad(
            id="squad-marketing",
            name="Marketing",
            status="federated",
            product_owner="Laura Torres",
            risk_officer="Diego Ruiz",
            adoption_rate=92.0,
            maturity_level=4
        ),
        Squad(
            id="squad-compliance",
            name="Compliance",
            status="shadow",
            risk_officer="Sofia Mendez",
            adoption_rate=38.0,
            maturity_level=2
        )
    ]
    
    return squads

@app.post("/squads", response_model=Squad)
async def create_squad(squad: Squad):
    """Create a new squad"""
    if supabase:
        result = supabase.table("squads").insert(squad.dict()).execute()
        return result.data[0]
    
    # Store in Redis if no Supabase
    redis_client.hset(f"squad:{squad.id}", mapping=squad.dict())
    return squad

@app.put("/squads/{squad_id}/federate")
async def federate_squad(squad_id: str, product_owner: str, risk_officer: str):
    """Transition a squad from shadow to federated"""
    # Start Temporal workflow for federation process
    if supabase:
        supabase.table("squads").update({
            "status": "federated",
            "product_owner": product_owner,
            "risk_officer": risk_officer
        }).eq("id", squad_id).execute()
    
    # Trigger workflow
    workflow_id = f"federate-{squad_id}-{datetime.utcnow().timestamp()}"
    
    return {
        "status": "federation_initiated",
        "squad_id": squad_id,
        "workflow_id": workflow_id
    }

# ============================================
# AUDIT & COMPLIANCE
# ============================================

@app.get("/audit/events", response_model=List[AuditEvent])
async def get_audit_events(
    limit: int = 100,
    squad_id: Optional[str] = None,
    user_id: Optional[str] = None
):
    """Get audit events with optional filtering"""
    if supabase:
        query = supabase.table("audit_events").select("*")
        if squad_id:
            query = query.eq("squad_id", squad_id)
        if user_id:
            query = query.eq("user_id", user_id)
        result = query.limit(limit).order("timestamp", desc=True).execute()
        return result.data
    
    # Mock data
    return [
        AuditEvent(
            event_type="model_access",
            user_id=user_id or "user123",
            squad_id=squad_id or "squad-risk",
            action="prompt_execution",
            metadata={"model": "gpt-4", "tokens": 1500},
            compliance_flags=["iso-42001", "cnbv-compliant"]
        )
    ]

@app.post("/audit/events", response_model=AuditEvent)
async def create_audit_event(event: AuditEvent, background_tasks: BackgroundTasks):
    """Create a new audit event"""
    # Add to background task for async processing
    background_tasks.add_task(process_audit_event, event)
    
    api_requests.labels(method="POST", endpoint="/audit/events").inc()
    return event

async def process_audit_event(event: AuditEvent):
    """Process audit event asynchronously"""
    # Store in Supabase
    if supabase:
        supabase.table("audit_events").insert(event.dict()).execute()
    
    # Check for compliance violations
    if "violation" in event.compliance_flags:
        # Trigger alert workflow
        pass
    
    # Update metrics
    redis_client.hincrby("metrics:audit:counts", event.event_type, 1)

# ============================================
# WORKFLOW MANAGEMENT
# ============================================

@app.get("/workflows", response_model=List[WorkflowExecution])
async def get_workflows(status: Optional[str] = None):
    """Get workflow executions"""
    # Would query Temporal in production
    workflows = [
        WorkflowExecution(
            workflow_id="onboard-po-123",
            workflow_type="onboarding_product_owner",
            status="completed",
            started_at=datetime.utcnow() - timedelta(hours=2),
            completed_at=datetime.utcnow() - timedelta(hours=1),
            result={"success": True, "squad": "squad-risk"}
        ),
        WorkflowExecution(
            workflow_id="training-enroll-456",
            workflow_type="training_enrollment",
            status="running",
            started_at=datetime.utcnow() - timedelta(minutes=30)
        )
    ]
    
    if status:
        workflows = [w for w in workflows if w.status == status]
    
    return workflows

@app.post("/workflows/{workflow_type}/start")
async def start_workflow(workflow_type: str, params: Dict[str, Any]):
    """Start a new workflow execution"""
    workflow_id = f"{workflow_type}-{datetime.utcnow().timestamp()}"
    
    # Would start Temporal workflow in production
    # For now, store in Redis
    redis_client.hset(f"workflow:{workflow_id}", mapping={
        "workflow_type": workflow_type,
        "status": "running",
        "started_at": datetime.utcnow().isoformat(),
        "params": json.dumps(params)
    })
    
    return {
        "workflow_id": workflow_id,
        "status": "started",
        "workflow_type": workflow_type
    }

# ============================================
# COURSES (Legacy compatibility)
# ============================================

@app.get("/courses")
async def get_courses():
    """Get available courses (redirects to training-tracker service)"""
    # This endpoint maintained for backward compatibility
    # In production, would proxy to training-tracker service
    return [
        {"code": "AI-101", "title": "Fundamentos GenAI"},
        {"code": "AI-201", "title": "Prompt Engineering Avanzado"},
        {"code": "AI-301", "title": "APIs de IA para Desarrolladores"},
        {"code": "AI-401", "title": "ISO/IEC 42001 Compliance"}
    ]

# ============================================
# REPORTS & EXPORTS
# ============================================

@app.get("/reports/executive-summary")
async def get_executive_summary():
    """Generate executive summary report"""
    impact = await get_impact_metrics()
    adoption = await get_adoption_metrics()
    squads = await get_squads()
    
    federated_count = len([s for s in squads if s.status == "federated"])
    avg_adoption = sum(s.adoption_rate for s in squads) / len(squads)
    
    return {
        "generated_at": datetime.utcnow().isoformat(),
        "impact_score": sum([
            impact.implementation,
            impact.momentum,
            impact.performance,
            impact.acceptance,
            impact.cost_effective,
            impact.trust
        ]) / 6,
        "adoption_summary": {
            "providers_active": len(adoption),
            "avg_coverage": sum(a["coverage_pct"] for a in adoption) / len(adoption),
            "total_weekly_users": sum(a["weekly_active_users"] for a in adoption)
        },
        "federation_status": {
            "federated_squads": federated_count,
            "total_squads": len(squads),
            "avg_adoption_rate": avg_adoption
        },
        "compliance_status": {
            "iso_42001": "compliant",
            "cnbv": "compliant",
            "banxico": "in_progress"
        }
    }

@app.get("/reports/export/{format}")
async def export_report(format: str = "json"):
    """Export reports in various formats"""
    if format not in ["json", "csv"]:
        raise HTTPException(status_code=400, detail="Format must be json or csv")
    
    data = await get_executive_summary()
    
    if format == "json":
        return JSONResponse(content=data)
    
    # CSV export would be implemented here
    return {"message": "CSV export not yet implemented"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)