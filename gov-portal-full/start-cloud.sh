#!/bin/bash

# AI Governance Portal - Cloud Mode Startup Script
# Uses Supabase Cloud instead of self-hosted

echo "🚀 Starting AI Governance Portal in Cloud Mode..."
echo "📡 Using Supabase Cloud: ${SUPABASE_URL:-Not configured}"

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please copy .env.example to .env and configure your Supabase Cloud keys"
    exit 1
fi

# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Check for required Supabase Cloud variables
if [ -z "$SUPABASE_URL" ] || [ -z "$SUPABASE_ANON_KEY" ] || [ -z "$SUPABASE_SERVICE_KEY" ]; then
    echo "❌ Error: Supabase Cloud credentials not configured!"
    echo "Please set SUPABASE_URL, SUPABASE_ANON_KEY, and SUPABASE_SERVICE_KEY in .env"
    exit 1
fi

echo "✅ Supabase Cloud configured"
echo "🔧 Starting services..."

# Start services using cloud compose file
docker-compose -f docker-compose.cloud.yml up -d

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 10

# Check service health
echo "🔍 Checking service health..."

# Check API
if curl -s http://localhost:${API_PORT:-8080}/health > /dev/null; then
    echo "✅ API is healthy"
else
    echo "⚠️  API might still be starting..."
fi

# Check Dashboard
if curl -s http://localhost:${DASHBOARD_PORT:-3000} > /dev/null; then
    echo "✅ Dashboard is ready"
else
    echo "⚠️  Dashboard might still be building..."
fi

echo ""
echo "🎉 AI Governance Portal is starting!"
echo ""
echo "📊 Access your services:"
echo "  Dashboard:        http://localhost:${DASHBOARD_PORT:-3000}"
echo "  API Docs:         http://localhost:${API_PORT:-8080}/docs"
echo "  Documentation:    http://localhost:${DOCS_PORT:-8001}"
echo "  Training Tracker: http://localhost:${TRAINING_PORT:-8082}/docs"
echo "  Grafana:          http://localhost:${GRAFANA_PORT:-3001} (admin/admin)"
echo "  Temporal UI:      http://localhost:${TEMPORAL_UI_PORT:-8088}"
echo ""
echo "📝 View logs: docker-compose -f docker-compose.cloud.yml logs -f"
echo "🛑 Stop all:  docker-compose -f docker-compose.cloud.yml down"