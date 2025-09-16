-- ============================================
-- SUPABASE INITIAL SCHEMA FOR AI GOVERNANCE PORTAL
-- ============================================

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";
CREATE EXTENSION IF NOT EXISTS "vector";

-- ============================================
-- CORE TABLES
-- ============================================

-- IMPACT Metrics Table
CREATE TABLE IF NOT EXISTS impact_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    implementation DECIMAL(5,2) CHECK (implementation >= 0 AND implementation <= 100),
    momentum DECIMAL(5,2) CHECK (momentum >= 0 AND momentum <= 100),
    performance DECIMAL(5,2) CHECK (performance >= 0 AND performance <= 100),
    acceptance DECIMAL(5,2) CHECK (acceptance >= 0 AND acceptance <= 100),
    cost_effective DECIMAL(5,2) CHECK (cost_effective >= 0 AND cost_effective <= 100),
    trust DECIMAL(5,2) CHECK (trust >= 0 AND trust <= 100),
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    created_by UUID,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Adoption Metrics Table
CREATE TABLE IF NOT EXISTS adoption_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    provider VARCHAR(50) NOT NULL,
    coverage_pct DECIMAL(5,2) CHECK (coverage_pct >= 0 AND coverage_pct <= 100),
    ttfv_minutes DECIMAL(10,2) CHECK (ttfv_minutes >= 0),
    weekly_active_users INTEGER CHECK (weekly_active_users >= 0),
    nps_score DECIMAL(5,2) CHECK (nps_score >= -100 AND nps_score <= 100),
    roi DECIMAL(10,2) CHECK (roi >= 0),
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    squad_id UUID,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Squads Table
CREATE TABLE IF NOT EXISTS squads (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL UNIQUE,
    status VARCHAR(20) CHECK (status IN ('shadow', 'federated', 'autonomous')) DEFAULT 'shadow',
    product_owner UUID,
    risk_officer UUID,
    adoption_rate DECIMAL(5,2) CHECK (adoption_rate >= 0 AND adoption_rate <= 100),
    maturity_level INTEGER CHECK (maturity_level >= 1 AND maturity_level <= 5) DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Audit Events Table
CREATE TABLE IF NOT EXISTS audit_events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_type VARCHAR(50) NOT NULL,
    user_id UUID NOT NULL,
    squad_id UUID REFERENCES squads(id),
    action VARCHAR(100) NOT NULL,
    resource_type VARCHAR(50),
    resource_id VARCHAR(100),
    metadata JSONB DEFAULT '{}'::jsonb,
    compliance_flags TEXT[],
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    ip_address INET,
    user_agent TEXT
);

-- Training Enrollments Table
CREATE TABLE IF NOT EXISTS training_enrollments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    course_id VARCHAR(50) NOT NULL,
    enrolled_at TIMESTAMPTZ DEFAULT NOW(),
    status VARCHAR(20) CHECK (status IN ('enrolled', 'in_progress', 'completed', 'dropped')) DEFAULT 'enrolled',
    progress_percentage DECIMAL(5,2) CHECK (progress_percentage >= 0 AND progress_percentage <= 100) DEFAULT 0,
    completed_at TIMESTAMPTZ,
    certificate_id UUID,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Courses Table
CREATE TABLE IF NOT EXISTS courses (
    id VARCHAR(50) PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    track_id VARCHAR(50) NOT NULL,
    duration_hours INTEGER CHECK (duration_hours > 0),
    difficulty VARCHAR(20) CHECK (difficulty IN ('beginner', 'intermediate', 'advanced', 'expert')),
    provider VARCHAR(50),
    tags TEXT[],
    learning_objectives TEXT[],
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    is_active BOOLEAN DEFAULT true
);

-- Workflows Table
CREATE TABLE IF NOT EXISTS workflows (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    workflow_id VARCHAR(100) NOT NULL UNIQUE,
    workflow_type VARCHAR(50) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('pending', 'running', 'completed', 'failed', 'cancelled')) DEFAULT 'pending',
    started_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    params JSONB DEFAULT '{}'::jsonb,
    result JSONB,
    error_message TEXT,
    created_by UUID
);

-- Knowledge Base Table (for vector embeddings)
CREATE TABLE IF NOT EXISTS knowledge_base (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    category VARCHAR(50),
    tags TEXT[],
    embedding vector(1536),
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    created_by UUID
);

-- ============================================
-- INDEXES
-- ============================================

CREATE INDEX idx_impact_metrics_timestamp ON impact_metrics(timestamp DESC);
CREATE INDEX idx_adoption_metrics_provider ON adoption_metrics(provider, timestamp DESC);
CREATE INDEX idx_adoption_metrics_squad ON adoption_metrics(squad_id);
CREATE INDEX idx_audit_events_user ON audit_events(user_id, timestamp DESC);
CREATE INDEX idx_audit_events_squad ON audit_events(squad_id, timestamp DESC);
CREATE INDEX idx_audit_events_type ON audit_events(event_type, timestamp DESC);
CREATE INDEX idx_training_enrollments_user ON training_enrollments(user_id);
CREATE INDEX idx_training_enrollments_course ON training_enrollments(course_id);
CREATE INDEX idx_workflows_type ON workflows(workflow_type, status);
CREATE INDEX idx_knowledge_base_embedding ON knowledge_base USING ivfflat (embedding vector_cosine_ops);

-- ============================================
-- ROW LEVEL SECURITY (RLS)
-- ============================================

ALTER TABLE impact_metrics ENABLE ROW LEVEL SECURITY;
ALTER TABLE adoption_metrics ENABLE ROW LEVEL SECURITY;
ALTER TABLE squads ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE training_enrollments ENABLE ROW LEVEL SECURITY;
ALTER TABLE courses ENABLE ROW LEVEL SECURITY;
ALTER TABLE workflows ENABLE ROW LEVEL SECURITY;
ALTER TABLE knowledge_base ENABLE ROW LEVEL SECURITY;

-- ============================================
-- FUNCTIONS & TRIGGERS
-- ============================================

-- Auto-update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_squads_updated_at BEFORE UPDATE ON squads
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_courses_updated_at BEFORE UPDATE ON courses
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_knowledge_base_updated_at BEFORE UPDATE ON knowledge_base
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Function to calculate IMPACT score
CREATE OR REPLACE FUNCTION calculate_impact_score(
    p_implementation DECIMAL,
    p_momentum DECIMAL,
    p_performance DECIMAL,
    p_acceptance DECIMAL,
    p_cost_effective DECIMAL,
    p_trust DECIMAL
) RETURNS DECIMAL AS $$
BEGIN
    RETURN (p_implementation + p_momentum + p_performance + p_acceptance + p_cost_effective + p_trust) / 6.0;
END;
$$ LANGUAGE plpgsql;

-- ============================================
-- INITIAL DATA
-- ============================================

-- Insert initial courses
INSERT INTO courses (id, code, title, description, track_id, duration_hours, difficulty, provider)
VALUES 
    ('ai-101', 'AI-101', 'Fundamentos de IA Generativa', 'Introducción a conceptos básicos de GenAI', 'tier1', 8, 'beginner', 'internal'),
    ('ai-201', 'AI-201', 'Prompt Engineering Avanzado', 'Técnicas avanzadas para optimizar prompts', 'track-a', 12, 'intermediate', 'anthropic'),
    ('ai-301', 'AI-301', 'APIs de IA para Desarrolladores', 'Integración de APIs de OpenAI, Anthropic y Google', 'track-b', 16, 'advanced', 'openai'),
    ('ai-401', 'AI-401', 'ISO/IEC 42001 Compliance', 'Implementación de estándares ISO para IA', 'track-d', 20, 'expert', 'internal')
ON CONFLICT (id) DO NOTHING;

-- Insert initial squads
INSERT INTO squads (name, status, adoption_rate, maturity_level)
VALUES 
    ('Riesgos', 'federated', 85.0, 4),
    ('Digital Banking', 'federated', 78.0, 3),
    ('Infraestructura', 'shadow', 45.0, 2),
    ('Marketing', 'federated', 92.0, 4),
    ('Compliance', 'shadow', 38.0, 2)
ON CONFLICT (name) DO NOTHING;