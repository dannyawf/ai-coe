# Backstage Knowledge Hub

## Overview

Backstage serves as the Knowledge Hub for the AI CoE, integrating with Langfuse to provide a centralized portal for:
- Prompt library management
- Agent catalog
- Best practices documentation
- Developer resources
- Team collaboration

## Setup

### 1. Configure Environment Variables

Copy the `.env.example` file and add your Langfuse API keys:

```bash
# Langfuse Configuration
LANGFUSE_BASE_URL=https://cloud.langfuse.com
LANGFUSE_PUBLIC_KEY=pk-lf-your-public-key
LANGFUSE_SECRET_KEY=sk-lf-your-secret-key
```

### 2. Start Services

```bash
# Start Backstage with docker-compose
docker-compose up backstage backstage-db

# Or start only Backstage services
docker-compose up -d backstage backstage-db
```

### 3. Access the Portal

- **Backstage UI**: http://localhost:3002
- **Backstage API**: http://localhost:7007
- **API Docs**: http://localhost:7007/api-docs

## Langfuse Integration

The custom Langfuse plugin provides:

### API Endpoints

- `GET /api/langfuse/prompts` - List all prompts
- `GET /api/langfuse/prompts/:name` - Get specific prompt
- `GET /api/langfuse/traces` - Get execution traces
- `GET /api/langfuse/scores` - Get evaluation scores
- `GET /api/langfuse/sessions` - Get user sessions
- `GET /api/langfuse/metrics` - Get usage metrics
- `POST /api/langfuse/search` - Search across entities

### Features

1. **Prompt Management**
   - Version control for prompts
   - Metadata and tags
   - Usage statistics
   - Performance metrics

2. **Observability**
   - Trace visualization
   - Token usage tracking
   - Cost analysis
   - Error monitoring

3. **Evaluation**
   - LLM-as-a-Judge scores
   - User feedback
   - A/B testing results
   - Performance benchmarks

## Development

### Adding New Integrations

1. Create a new plugin in `plugins/` directory
2. Register it in `app-config.yaml`
3. Add API routes in the backend plugin
4. Create frontend components as needed

### Plugin Structure

```
plugins/
├── langfuse-backend/
│   ├── src/
│   │   ├── service/
│   │   │   ├── router.ts        # API routes
│   │   │   └── LangfuseClient.ts # API client
│   │   └── index.ts
│   └── package.json
└── langfuse-frontend/ (future)
    ├── src/
    │   ├── components/
    │   └── api/
    └── package.json
```

## Troubleshooting

### Connection Issues

1. Verify Langfuse API keys are correct
2. Check firewall settings allow outbound HTTPS
3. Ensure Backstage database is running
4. Review logs: `docker-compose logs backstage`

### Common Errors

- **401 Unauthorized**: Invalid API keys
- **403 Forbidden**: API key lacks permissions
- **500 Internal Error**: Check Backstage logs
- **Connection Refused**: Database not started

## Security

- API keys are stored as environment variables
- All Langfuse requests use HTTPS
- Backstage uses PostgreSQL for catalog storage
- Authentication can be configured (GitHub OAuth, etc.)

## Roadmap

- [ ] Frontend UI for prompt browsing
- [ ] Semantic search integration
- [ ] Wiki system for documentation
- [ ] Slack integration for notifications
- [ ] Advanced analytics dashboard
- [ ] Export/Import functionality