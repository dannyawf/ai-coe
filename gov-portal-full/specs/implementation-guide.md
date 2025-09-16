# AI Governance Portal - Implementation Guide

## Quick Start

### Prerequisites
- Docker Desktop 4.25+ with Docker Compose v2
- 16GB RAM minimum (32GB recommended)
- 50GB available disk space
- Git

### Step 1: Clone and Configure

```bash
# Clone the repository
git clone https://github.com/your-org/ai-governance-portal.git
cd ai-governance-portal

# Copy environment template
cp .env.example .env

# Generate secure keys
openssl rand -base64 32  # For JWT_SECRET
openssl rand -base64 32  # For ANON_KEY
openssl rand -base64 32  # For SERVICE_ROLE_KEY

# Edit .env with your values
nano .env
```

### Step 2: Start Core Services

```bash
# Start Supabase stack first
docker-compose up -d supabase-db supabase-auth supabase-kong

# Wait for database to be ready (30 seconds)
sleep 30

# Start remaining services
docker-compose up -d

# Verify all services are running
docker-compose ps
```

### Step 3: Access Services

| Service | URL | Default Credentials |
|---------|-----|---------------------|
| Dashboard | http://localhost:3000 | Configure in Supabase |
| API | http://localhost:8080/docs | No auth for docs |
| Documentation | http://localhost:8001 | Public access |
| Training Tracker | http://localhost:8082/docs | No auth for docs |
| Grafana | http://localhost:3001 | admin/admin |
| Temporal UI | http://localhost:8088 | No auth |
| Jaeger | http://localhost:16686 | No auth |
| Prometheus | http://localhost:9090 | No auth |

## Configuration Details

### Environment Variables

#### Required Variables
```bash
# Database
POSTGRES_PASSWORD=your-super-secret-password

# JWT Keys (Generate with: openssl rand -base64 32)
JWT_SECRET=your-jwt-secret-at-least-32-characters
ANON_KEY=your-anon-key
SERVICE_ROLE_KEY=your-service-role-key
```

#### Optional Email Configuration
```bash
# SMTP for email notifications
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
SMTP_SENDER_NAME=AI Governance Portal
```

### Database Initialization

The database is automatically initialized with:
- Core tables (IMPACT metrics, squads, training, audit)
- Indexes for performance
- Row-level security policies
- Initial seed data (courses, squads)
- Vector extension for AI embeddings

To reset the database:
```bash
docker-compose down -v
docker-compose up -d supabase-db
# Wait 30 seconds for initialization
docker-compose up -d
```

## Development Workflow

### Local Development

1. **API Development**
```bash
cd services/api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app:app --reload --port 8080
```

2. **Dashboard Development**
```bash
cd services/dashboard
npm install
npm run dev
```

3. **Training Tracker Development**
```bash
cd services/training-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8082
```

### Testing

```bash
# Run API tests
cd services/api
pytest tests/

# Run Dashboard tests
cd services/dashboard
npm test

# Integration tests
docker-compose up -d
python tests/integration/test_e2e.py
```

## Production Deployment

### Docker Swarm Deployment

```bash
# Initialize swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml ai-governance

# Scale services
docker service scale ai-governance_api=3
docker service scale ai-governance_dashboard=2
```

### Kubernetes Deployment

```bash
# Create namespace
kubectl create namespace ai-governance

# Apply configurations
kubectl apply -f k8s/

# Check deployment
kubectl get pods -n ai-governance
```

### Cloud Deployments

#### AWS ECS
1. Push images to ECR
2. Create ECS task definitions
3. Configure ALB for load balancing
4. Set up RDS for PostgreSQL
5. Use ElastiCache for Redis

#### Google Cloud Run
1. Push images to Artifact Registry
2. Deploy services to Cloud Run
3. Use Cloud SQL for PostgreSQL
4. Use Memorystore for Redis
5. Configure Cloud Load Balancing

#### Azure Container Instances
1. Push images to ACR
2. Deploy to Container Instances
3. Use Azure Database for PostgreSQL
4. Use Azure Cache for Redis
5. Configure Application Gateway

## Monitoring & Maintenance

### Health Checks

```bash
# Check all service health endpoints
curl http://localhost:8080/health
curl http://localhost:8082/health
curl http://localhost:3000/api/health

# Check database connection
docker exec -it ai_coe-supabase-db-1 pg_isready -U postgres
```

### Logs

```bash
# View all logs
docker-compose logs -f

# Service-specific logs
docker-compose logs -f api
docker-compose logs -f dashboard
docker-compose logs -f supabase-db

# Export logs
docker-compose logs > logs.txt
```

### Metrics

1. **Grafana Dashboards** (http://localhost:3001)
   - IMPACT Metrics Dashboard
   - Service Health Dashboard
   - Training Analytics Dashboard
   - Infrastructure Metrics

2. **Prometheus Queries** (http://localhost:9090)
```promql
# API request rate
rate(api_requests_total[5m])

# IMPACT metric updates
rate(impact_metric_updates_total[1h])

# Training enrollments
sum(training_course_enrollments_total)
```

### Backup & Restore

```bash
# Backup database
docker exec ai_coe-supabase-db-1 pg_dump -U postgres postgres > backup.sql

# Restore database
docker exec -i ai_coe-supabase-db-1 psql -U postgres postgres < backup.sql

# Backup volumes
docker run --rm -v ai_coe_postgres-data:/data -v $(pwd):/backup alpine tar czf /backup/postgres-backup.tar.gz /data
```

## Troubleshooting

### Common Issues

1. **Services not starting**
```bash
# Check logs
docker-compose logs service-name

# Restart specific service
docker-compose restart service-name

# Rebuild service
docker-compose build --no-cache service-name
docker-compose up -d service-name
```

2. **Database connection errors**
```bash
# Check database is running
docker-compose ps supabase-db

# Test connection
docker exec -it ai_coe-supabase-db-1 psql -U postgres -c "SELECT 1"

# Reset database
docker-compose down -v supabase-db
docker-compose up -d supabase-db
```

3. **Port conflicts**
```bash
# Check port usage
lsof -i :8080  # Mac/Linux
netstat -ano | findstr :8080  # Windows

# Change ports in .env file
API_PORT=8081
DASHBOARD_PORT=3001
```

4. **Memory issues**
```bash
# Increase Docker memory (Docker Desktop)
# Preferences → Resources → Memory: 8GB minimum

# Or use swap
docker-compose down
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
docker-compose up -d
```

## Security Hardening

### Production Checklist

- [ ] Change all default passwords
- [ ] Enable TLS/SSL for all services
- [ ] Configure firewall rules
- [ ] Enable Supabase RLS policies
- [ ] Set up API rate limiting
- [ ] Configure CORS properly
- [ ] Enable audit logging
- [ ] Set up backup automation
- [ ] Configure monitoring alerts
- [ ] Implement secret rotation
- [ ] Enable MFA for admin accounts
- [ ] Regular security updates

### TLS Configuration

```nginx
# nginx.conf for reverse proxy
server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    ssl_certificate /etc/ssl/certs/your-cert.pem;
    ssl_certificate_key /etc/ssl/private/your-key.pem;
    
    location / {
        proxy_pass http://dashboard:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Performance Tuning

### Database Optimization

```sql
-- Add missing indexes
CREATE INDEX CONCURRENTLY idx_audit_events_timestamp ON audit_events(timestamp);
CREATE INDEX CONCURRENTLY idx_impact_metrics_created ON impact_metrics(timestamp);

-- Analyze tables
ANALYZE impact_metrics;
ANALYZE audit_events;
ANALYZE squads;

-- Configure connection pooling
ALTER SYSTEM SET max_connections = 200;
ALTER SYSTEM SET shared_buffers = '256MB';
```

### Redis Configuration

```redis
# redis.conf
maxmemory 2gb
maxmemory-policy allkeys-lru
save 900 1
save 300 10
save 60 10000
```

### API Performance

```python
# Use connection pooling
from databases import Database
database = Database(DATABASE_URL, min_size=10, max_size=20)

# Enable response caching
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
FastAPICache.init(RedisBackend(redis), prefix="api-cache")
```

## Support & Resources

- **Documentation**: http://localhost:8001
- **API Docs**: http://localhost:8080/docs
- **Architecture**: See ARCHITECTURE.md
- **Issues**: https://github.com/your-org/ai-governance-portal/issues
- **Slack**: #ai-governance-support
- **Email**: support@ai-governance.com

## Version History

- **v2.0.0** - Migrated to Supabase, added Temporal, improved observability
- **v1.0.0** - Initial release with Keycloak and Moodle