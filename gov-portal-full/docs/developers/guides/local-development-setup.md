# 💻 Guía de Configuración del Entorno de Desarrollo Local

## 📋 Información General

**Versión:** 1.0.0  
**Última Actualización:** Enero 2025  
**Tiempo Estimado:** 1-2 horas  
**Nivel:** Intermedio

## 🎯 Objetivo

Configurar un entorno de desarrollo local completo para trabajar con Nova-Cell Platform y desarrollar aplicaciones de IA para el sector bancario.

## 🛠️ Stack Tecnológico

### Core Technologies
- **Python** 3.11+ (Backend, ML)
- **Node.js** 20+ (Frontend, Tools)
- **Docker** 24+ (Containerization)
- **PostgreSQL** 15+ (Primary Database)
- **Redis** 7+ (Cache, Queue)
- **MongoDB** 7+ (Analytics)

### AI/ML Stack
- **LangChain** (Orchestration)
- **OpenAI SDK** (GPT Models)
- **Anthropic SDK** (Claude)
- **Google AI SDK** (Gemini)
- **Hugging Face** (Open Models)

## 📦 Instalación Base

### 1. Herramientas de Desarrollo

#### macOS
```bash
# Instalar Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar herramientas base
brew install git wget curl jq make gcc
brew install python@3.11 node@20 yarn
brew install postgresql@15 redis mongodb-community
brew install docker docker-compose colima

# Iniciar Colima (Docker en macOS)
colima start --cpu 4 --memory 8 --disk 100
```

#### Linux (Ubuntu/Debian)
```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y build-essential git curl wget jq
sudo apt install -y python3.11 python3.11-venv python3-pip
sudo apt install -y postgresql-15 redis-server mongodb

# Instalar Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Instalar Docker
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
```

#### Windows (WSL2)
```powershell
# Instalar WSL2
wsl --install

# Instalar Ubuntu
wsl --install -d Ubuntu-22.04

# Dentro de WSL2, seguir instrucciones de Linux
```

### 2. IDEs y Editores

#### VS Code - Configuración Recomendada
```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/node_modules": true,
    "**/.pytest_cache": true
  }
}
```

#### Extensiones Esenciales
```bash
# Instalar extensiones de VS Code
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-azuretools.vscode-docker
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension github.copilot
code --install-extension ms-vscode.makefile-tools
code --install-extension redhat.vscode-yaml
code --install-extension hashicorp.terraform
```

## 🐍 Configuración Python

### 1. Entorno Virtual
```bash
# Crear directorio del proyecto
mkdir ~/dev/nova-cell-dev
cd ~/dev/nova-cell-dev

# Crear entorno virtual
python3.11 -m venv venv

# Activar entorno
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate  # Windows

# Actualizar pip
pip install --upgrade pip setuptools wheel
```

### 2. Dependencias Core
```bash
# requirements-dev.txt
pip install -r - <<EOF
# Core
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic==2.5.0
sqlalchemy==2.0.25
alembic==1.13.0

# AI/ML
langchain==0.1.0
langchain-openai==0.0.5
langchain-anthropic==0.0.2
langchain-google-genai==0.0.5
chromadb==0.4.22
tiktoken==0.5.2

# Database
psycopg2-binary==2.9.9
redis==5.0.1
pymongo==4.6.1

# Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# Development
pytest==7.4.4
pytest-asyncio==0.23.3
pytest-cov==4.1.0
black==23.12.1
pylint==3.0.3
mypy==1.8.0
ipython==8.20.0
jupyter==1.0.0

# Monitoring
prometheus-client==0.19.0
opentelemetry-api==1.22.0
opentelemetry-sdk==1.22.0
EOF
```

## 🌐 Configuración Node.js

### 1. Proyecto Frontend
```bash
# Crear proyecto React
npx create-react-app nova-cell-ui --template typescript
cd nova-cell-ui

# Instalar dependencias adicionales
npm install axios react-query zustand
npm install @mui/material @emotion/react @emotion/styled
npm install recharts react-markdown
npm install --save-dev @types/node @types/react
```

### 2. Configuración TypeScript
```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "esnext",
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "baseUrl": "src",
    "paths": {
      "@/*": ["*"],
      "@components/*": ["components/*"],
      "@services/*": ["services/*"],
      "@utils/*": ["utils/*"]
    }
  },
  "include": ["src"],
  "exclude": ["node_modules", "build"]
}
```

## 🐳 Docker Development Stack

### 1. Docker Compose para Desarrollo
```yaml
# docker-compose.dev.yml
version: '3.9'

services:
  # PostgreSQL
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: nova_dev
      POSTGRES_PASSWORD: nova_dev_pass
      POSTGRES_DB: nova_cell_dev
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./scripts/init.sql:/docker-entrypoint-initdb.d/init.sql

  # Redis
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # MongoDB
  mongodb:
    image: mongo:7
    environment:
      MONGO_INITDB_ROOT_USERNAME: nova_dev
      MONGO_INITDB_ROOT_PASSWORD: nova_dev_pass
      MONGO_INITDB_DATABASE: nova_analytics
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

  # MinIO (S3 Compatible)
  minio:
    image: minio/minio:latest
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - minio_data:/data

  # Adminer (DB Management)
  adminer:
    image: adminer
    ports:
      - "8080:8080"
    environment:
      ADMINER_DEFAULT_SERVER: postgres

  # RedisInsight
  redis-insight:
    image: redislabs/redisinsight:latest
    ports:
      - "8001:8001"
    volumes:
      - redis_insight:/db

volumes:
  postgres_data:
  redis_data:
  mongo_data:
  minio_data:
  redis_insight:
```

### 2. Iniciar Stack de Desarrollo
```bash
# Iniciar servicios
docker-compose -f docker-compose.dev.yml up -d

# Verificar estado
docker-compose -f docker-compose.dev.yml ps

# Ver logs
docker-compose -f docker-compose.dev.yml logs -f

# Detener servicios
docker-compose -f docker-compose.dev.yml down
```

## 🔑 Configuración de Credenciales

### 1. Variables de Entorno
```bash
# .env.development
# API Configuration
API_HOST=localhost
API_PORT=8000
API_PREFIX=/api/v1

# Database
DATABASE_URL=postgresql://nova_dev:nova_dev_pass@localhost:5432/nova_cell_dev
MONGODB_URI=mongodb://nova_dev:nova_dev_pass@localhost:27017/nova_analytics
REDIS_URL=redis://localhost:6379/0

# AI Models
OPENAI_API_KEY=sk-dev-xxx
ANTHROPIC_API_KEY=sk-ant-dev-xxx
GOOGLE_API_KEY=AIza-dev-xxx
HUGGINGFACE_TOKEN=hf_dev_xxx

# Security
JWT_SECRET=dev-jwt-secret-change-in-production
ENCRYPTION_KEY=dev-encryption-key-32-chars-long

# S3/MinIO
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=nova-dev

# Development
DEBUG=true
LOG_LEVEL=debug
RELOAD=true
```

### 2. Git Configuration
```bash
# Configurar Git
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@novasolutionsystems.com"

# Configurar Git Hooks
cat > .git/hooks/pre-commit <<'EOF'
#!/bin/bash
# Ejecutar linters y tests antes de commit

# Python
black --check .
pylint src/
pytest tests/ -v

# JavaScript/TypeScript
npm run lint
npm test

# Verificar secretos
git secrets --scan
EOF

chmod +x .git/hooks/pre-commit
```

## 🧪 Testing Setup

### 1. Configuración de Pytest
```python
# pytest.ini
[tool:pytest]
minversion = 7.0
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -ra
    --strict-markers
    --cov=src
    --cov-branch
    --cov-report=term-missing:skip-covered
    --cov-report=html
    --cov-report=xml
    --cov-fail-under=80
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### 2. Test Structure
```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope="session")
def db_engine():
    """Create test database engine"""
    engine = create_engine(
        "postgresql://test_user:test_pass@localhost:5432/test_db"
    )
    return engine

@pytest.fixture(scope="function")
def db_session(db_engine):
    """Create test database session"""
    Session = sessionmaker(bind=db_engine)
    session = Session()
    yield session
    session.rollback()
    session.close()

@pytest.fixture
def client():
    """Create test client"""
    from main import app
    return TestClient(app)

@pytest.fixture
def mock_openai(monkeypatch):
    """Mock OpenAI API calls"""
    def mock_completion(*args, **kwargs):
        return {
            "choices": [{
                "message": {
                    "content": "Mocked response"
                }
            }]
        }
    monkeypatch.setattr(
        "openai.ChatCompletion.create",
        mock_completion
    )
```

## 🚀 Scripts de Desarrollo

### 1. Makefile
```makefile
# Makefile
.PHONY: help install dev test clean

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make dev      - Start development server"
	@echo "  make test     - Run tests"
	@echo "  make clean    - Clean cache files"

install:
	pip install -r requirements-dev.txt
	npm install
	pre-commit install

dev:
	docker-compose -f docker-compose.dev.yml up -d
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest tests/ -v --cov=src
	npm test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov
	rm -rf node_modules/.cache
```

### 2. Development Scripts
```bash
#!/bin/bash
# scripts/dev-setup.sh

echo "🚀 Setting up Nova-Cell development environment..."

# Check prerequisites
command -v python3.11 >/dev/null 2>&1 || { echo "Python 3.11 required"; exit 1; }
command -v node >/dev/null 2>&1 || { echo "Node.js required"; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "Docker required"; exit 1; }

# Create project structure
mkdir -p {src,tests,scripts,docs,config}
mkdir -p src/{api,models,services,utils}
mkdir -p tests/{unit,integration,e2e}

# Setup Python environment
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt

# Setup Node environment
npm install

# Start Docker services
docker-compose -f docker-compose.dev.yml up -d

# Run database migrations
alembic upgrade head

# Create test data
python scripts/seed_dev_data.py

echo "✅ Development environment ready!"
echo "📝 Next steps:"
echo "  1. source venv/bin/activate"
echo "  2. make dev"
echo "  3. Open http://localhost:8000"
```

## 🔍 Debugging Configuration

### 1. VS Code Launch Configuration
```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "main:app",
        "--reload",
        "--port", "8000"
      ],
      "jinja": true,
      "justMyCode": false,
      "env": {
        "PYTHONPATH": "${workspaceFolder}",
        "ENV": "development"
      }
    },
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "Jest Debug",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["test", "--", "--runInBand"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen"
    }
  ]
}
```

### 2. Logging Configuration
```python
# config/logging.py
import logging
import sys
from pathlib import Path

def setup_logging(level="DEBUG"):
    """Configure logging for development"""
    
    # Create logs directory
    Path("logs").mkdir(exist_ok=True)
    
    # Configure formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # File handler
    file_handler = logging.FileHandler('logs/dev.log')
    file_handler.setFormatter(formatter)
    
    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level))
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
```

## 📊 Monitoring Local

### 1. Prometheus Configuration
```yaml
# config/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'nova-api'
    static_configs:
      - targets: ['localhost:8000']
    metrics_path: '/metrics'
  
  - job_name: 'postgres'
    static_configs:
      - targets: ['localhost:9187']
  
  - job_name: 'redis'
    static_configs:
      - targets: ['localhost:9121']
```

### 2. Grafana Dashboard
```json
{
  "dashboard": {
    "title": "Nova-Cell Dev Metrics",
    "panels": [
      {
        "title": "API Response Time",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))"
          }
        ]
      },
      {
        "title": "Database Connections",
        "targets": [
          {
            "expr": "pg_stat_database_numbackends{datname='nova_cell_dev'}"
          }
        ]
      }
    ]
  }
}
```

## 🛡️ Security Best Practices

### 1. Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
  
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
  
  - repo: https://github.com/pycqa/pylint
    rev: v3.0.3
    hooks:
      - id: pylint
  
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
```

## 📚 Recursos de Desarrollo

### Documentación
- [Nova-Cell API Docs](http://localhost:8000/docs)
- [React DevTools](https://react.dev/learn/react-developer-tools)
- [LangChain Docs](https://python.langchain.com/)

### Herramientas Útiles
- **Postman/Insomnia** - API testing
- **TablePlus/DBeaver** - Database management
- **Lens** - Kubernetes IDE
- **Sourcetree/GitKraken** - Git GUI

## 🆘 Troubleshooting

### Problemas Comunes

```bash
# Error: Port already in use
lsof -i :8000  # Find process
kill -9 <PID>  # Kill process

# Error: Database connection failed
docker-compose -f docker-compose.dev.yml restart postgres
psql -U nova_dev -d nova_cell_dev -h localhost

# Error: Node modules issues
rm -rf node_modules package-lock.json
npm install

# Error: Python package conflicts
deactivate
rm -rf venv
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

---

*Última actualización: Enero 2025 | Versión 1.0.0*