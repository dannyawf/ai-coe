# Quick Setup Guide - AI Governance Portal

## Prerequisites
- Docker Desktop installed and running
- 16GB RAM minimum
- Terminal/Command Line

## Setup in 5 Minutes

### Step 1: Generate Security Keys
Run these commands to generate 3 required keys:

```bash
openssl rand -base64 32
openssl rand -base64 32  
openssl rand -base64 32
```

Save each output - you'll need them in Step 2.

### Step 2: Configure Environment
```bash
# Create your environment file
cp .env.example .env

# Edit the .env file and add your keys:
nano .env  # or use any text editor
```

Add these values to your `.env`:
```env
# Database password (create a strong one)
POSTGRES_PASSWORD=MyStr0ngP@ssw0rd!2024

# Paste your 3 generated keys here
JWT_SECRET=<paste-first-key-here>
ANON_KEY=<paste-second-key-here>
SERVICE_ROLE_KEY=<paste-third-key-here>

# Leave other settings as default
```

### Step 3: Start Everything
```bash
# Start all services with Docker Compose
docker-compose up -d

# Wait ~1 minute for services to initialize
# Check that everything is running
docker-compose ps
```

### Step 4: Access the Portal

| Service | URL | Purpose |
|---------|-----|---------|
| 🎯 **Dashboard** | http://localhost:3000 | Main portal interface |
| 📚 **Documentation** | http://localhost:8001 | Guides and playbooks |
| 🔌 **API** | http://localhost:8080/docs | Backend API explorer |
| 📊 **Grafana** | http://localhost:3001 | Metrics (admin/admin) |

## Verify Installation

Check that services are healthy:
```bash
# Check API health
curl http://localhost:8080/health

# Check logs if needed
docker-compose logs api
docker-compose logs dashboard
```

## Common Issues

### Ports Already in Use
If you get port conflicts, change them in `.env`:
```env
API_PORT=8081
DASHBOARD_PORT=3001
```

### Not Enough Memory
Docker Desktop needs at least 8GB RAM allocated:
- Docker Desktop → Settings → Resources → Memory: 8GB

### Services Not Starting
```bash
# Restart everything
docker-compose down
docker-compose up -d

# Check specific service logs
docker-compose logs service-name
```

## What's Included

✅ **All services run in Docker** - no local installation needed:
- Supabase (PostgreSQL + Auth + Realtime)
- FastAPI Backend
- Next.js Dashboard with Tremor UI
- Training Tracker Service
- MkDocs Documentation
- Temporal Workflow Engine
- Redis Cache
- Full Observability Stack (Prometheus, Grafana, Jaeger)
- Elasticsearch for search/logging

## Next Steps

1. **Create a user account** in Supabase Auth
2. **Import sample data** (optional):
   ```bash
   docker exec -i ai_coe-supabase-db-1 psql -U postgres < sample-data.sql
   ```
3. **Configure email** (optional) in `.env` for notifications
4. **Read the docs** at http://localhost:8001

## Stop Services

```bash
# Stop all services
docker-compose down

# Stop and remove all data (fresh start)
docker-compose down -v
```

---
**Need help?** Check `ARCHITECTURE.md` and `specs/implementation-guide.md` for detailed documentation.