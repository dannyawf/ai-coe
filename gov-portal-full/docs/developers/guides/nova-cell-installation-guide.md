# 🚀 Guía de Instalación Nova-Cell Platform

## 📋 Información General

**Versión:** 2.0.3  
**Última Actualización:** Enero 2025  
**Audiencia:** Desarrolladores, DevOps, Arquitectos de Soluciones  
**Tiempo Estimado:** 2-4 horas (instalación completa)

## 🎯 Objetivo

Esta guía proporciona instrucciones detalladas para instalar y configurar Nova-Cell Platform en diferentes entornos, desde desarrollo local hasta producción en la nube.

## 📊 Requisitos del Sistema

### Hardware Mínimo

| Componente | Desarrollo | Staging | Producción |
|------------|------------|---------|------------|
| CPU | 4 cores | 8 cores | 16 cores |
| RAM | 16 GB | 32 GB | 64 GB |
| Storage | 100 GB SSD | 250 GB SSD | 500 GB NVMe |
| Network | 100 Mbps | 1 Gbps | 10 Gbps |

### Software Requerido

```yaml
# Versiones mínimas requeridas
docker: "24.0.0"
docker-compose: "2.20.0"
kubernetes: "1.28.0"
python: "3.11.0"
nodejs: "20.0.0"
postgresql: "15.0"
mongodb: "7.0"
redis: "7.2"
```

### Dependencias del Sistema

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    jq \
    make \
    gcc \
    g++ \
    python3-dev \
    libpq-dev \
    libssl-dev \
    libffi-dev

# RHEL/CentOS
sudo yum groupinstall -y "Development Tools"
sudo yum install -y \
    git \
    curl \
    wget \
    jq \
    python3-devel \
    postgresql-devel \
    openssl-devel
```

## ✅ Pre-Instalación Checklist

### 1. Verificación de Prerrequisitos

```bash
#!/bin/bash
# Script de verificación pre-instalación

echo "🔍 Verificando prerrequisitos Nova-Cell..."

# Verificar Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no instalado"
    exit 1
fi
echo "✅ Docker: $(docker --version)"

# Verificar Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose no instalado"
    exit 1
fi
echo "✅ Docker Compose: $(docker-compose --version)"

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no instalado"
    exit 1
fi
echo "✅ Python: $(python3 --version)"

# Verificar Git
if ! command -v git &> /dev/null; then
    echo "❌ Git no instalado"
    exit 1
fi
echo "✅ Git: $(git --version)"

# Verificar espacio en disco
AVAILABLE_SPACE=$(df -BG / | awk 'NR==2 {print $4}' | sed 's/G//')
if [ "$AVAILABLE_SPACE" -lt 50 ]; then
    echo "⚠️  Espacio en disco insuficiente: ${AVAILABLE_SPACE}GB disponibles"
fi

echo "✅ Todos los prerrequisitos cumplidos"
```

### 2. Configuración de Credenciales

```bash
# Crear archivo de configuración de credenciales
cat > ~/.nova-cell/credentials <<EOF
# Credenciales de Nova-Cell
NOVA_LICENSE_KEY=your-license-key
NOVA_ADMIN_EMAIL=ai@novasolutionsystems.com
NOVA_ADMIN_PASSWORD=$(openssl rand -base64 32)

# Credenciales de Base de Datos
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nova_cell
DB_USER=nova_admin
DB_PASSWORD=$(openssl rand -base64 32)

# Credenciales de MongoDB
MONGO_URI=mongodb://localhost:27017
MONGO_DB=nova_analytics
MONGO_USER=nova_mongo
MONGO_PASSWORD=$(openssl rand -base64 32)

# API Keys de Modelos
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
GOOGLE_API_KEY=your-google-key
AZURE_OPENAI_KEY=your-azure-key

# Configuración de Seguridad
JWT_SECRET=$(openssl rand -base64 64)
ENCRYPTION_KEY=$(openssl rand -base64 32)
EOF

chmod 600 ~/.nova-cell/credentials
```

## 🐳 Instalación Local con Docker

### 1. Clonar Repositorio

```bash
# Clonar repositorio principal
git clone https://github.com/banco/nova-cell-platform.git
cd nova-cell-platform

# Cambiar a rama estable
git checkout stable/v2.0.3
```

### 2. Configuración Docker Compose

```yaml
# docker-compose.yml
version: '3.9'

services:
  # Base de Datos PostgreSQL
  postgres:
    image: postgres:15-alpine
    container_name: nova-postgres
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d
    ports:
      - "5432:5432"
    networks:
      - nova-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  # MongoDB para Analytics
  mongodb:
    image: mongo:7.0
    container_name: nova-mongodb
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_USER}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_PASSWORD}
      MONGO_INITDB_DATABASE: ${MONGO_DB}
    volumes:
      - mongo_data:/data/db
    ports:
      - "27017:27017"
    networks:
      - nova-network

  # Redis para Cache y Queue
  redis:
    image: redis:7.2-alpine
    container_name: nova-redis
    command: redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    networks:
      - nova-network

  # Nova-Cell Core API
  nova-api:
    build:
      context: .
      dockerfile: Dockerfile.api
    container_name: nova-api
    environment:
      - DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@postgres:5432/${DB_NAME}
      - MONGODB_URI=mongodb://${MONGO_USER}:${MONGO_PASSWORD}@mongodb:27017/${MONGO_DB}
      - REDIS_URL=redis://:${REDIS_PASSWORD}@redis:6379/0
      - JWT_SECRET=${JWT_SECRET}
      - ENCRYPTION_KEY=${ENCRYPTION_KEY}
    volumes:
      - ./api:/app
      - ./models:/models
      - ./logs:/logs
    ports:
      - "8000:8000"
    depends_on:
      - postgres
      - mongodb
      - redis
    networks:
      - nova-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Nova-Cell Web UI
  nova-ui:
    build:
      context: .
      dockerfile: Dockerfile.ui
    container_name: nova-ui
    environment:
      - REACT_APP_API_URL=http://nova-api:8000
      - REACT_APP_WS_URL=ws://nova-api:8000/ws
    volumes:
      - ./ui:/app
    ports:
      - "3000:3000"
    depends_on:
      - nova-api
    networks:
      - nova-network

  # ML Service
  nova-ml:
    build:
      context: .
      dockerfile: Dockerfile.ml
    container_name: nova-ml
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - MODEL_CACHE_DIR=/models
    volumes:
      - ./ml-service:/app
      - model_cache:/models
    ports:
      - "8001:8001"
    networks:
      - nova-network
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: nova-nginx
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/ssl:/etc/nginx/ssl
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - nova-api
      - nova-ui
    networks:
      - nova-network

volumes:
  postgres_data:
  mongo_data:
  redis_data:
  model_cache:

networks:
  nova-network:
    driver: bridge
```

### 3. Inicialización de la Base de Datos

```sql
-- init-scripts/01-create-schema.sql
CREATE SCHEMA IF NOT EXISTS nova_core;
CREATE SCHEMA IF NOT EXISTS nova_auth;
CREATE SCHEMA IF NOT EXISTS nova_audit;

-- Crear tablas principales
CREATE TABLE nova_core.organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255) UNIQUE NOT NULL,
    settings JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE nova_auth.users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    org_id UUID REFERENCES nova_core.organizations(id),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP
);

CREATE TABLE nova_core.projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    org_id UUID REFERENCES nova_core.organizations(id),
    owner_id UUID REFERENCES nova_auth.users(id),
    config JSONB DEFAULT '{}',
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE nova_core.models (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES nova_core.projects(id),
    name VARCHAR(255) NOT NULL,
    version VARCHAR(50),
    type VARCHAR(100),
    parameters JSONB,
    metrics JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Índices para optimización
CREATE INDEX idx_users_email ON nova_auth.users(email);
CREATE INDEX idx_users_org ON nova_auth.users(org_id);
CREATE INDEX idx_projects_org ON nova_core.projects(org_id);
CREATE INDEX idx_models_project ON nova_core.models(project_id);
```

### 4. Arranque del Sistema

```bash
# Cargar variables de entorno
source ~/.nova-cell/credentials

# Construir imágenes
docker-compose build

# Iniciar servicios
docker-compose up -d

# Verificar estado
docker-compose ps

# Ver logs
docker-compose logs -f nova-api

# Ejecutar migraciones
docker-compose exec nova-api python manage.py migrate

# Crear superusuario
docker-compose exec nova-api python manage.py createsuperuser
```

## ☁️ Instalación en AWS

### 1. Configuración con Terraform

```hcl
# terraform/main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC y Networking
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  
  name = "nova-cell-vpc"
  cidr = "10.0.0.0/16"
  
  azs             = ["${var.aws_region}a", "${var.aws_region}b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]
  
  enable_nat_gateway = true
  enable_vpn_gateway = true
  
  tags = {
    Environment = var.environment
    Project     = "nova-cell"
  }
}

# EKS Cluster
module "eks" {
  source = "terraform-aws-modules/eks/aws"
  
  cluster_name    = "nova-cell-cluster"
  cluster_version = "1.28"
  
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets
  
  node_groups = {
    main = {
      desired_capacity = 3
      max_capacity     = 10
      min_capacity     = 2
      
      instance_types = ["t3.xlarge"]
      
      k8s_labels = {
        Environment = var.environment
        Application = "nova-cell"
      }
    }
  }
}

# RDS PostgreSQL
resource "aws_db_instance" "nova_postgres" {
  identifier = "nova-cell-db"
  
  engine         = "postgres"
  engine_version = "15.4"
  instance_class = "db.r6g.xlarge"
  
  allocated_storage     = 100
  storage_encrypted     = true
  storage_type          = "gp3"
  
  db_name  = "nova_cell"
  username = var.db_username
  password = var.db_password
  
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.nova.name
  
  backup_retention_period = 30
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  tags = {
    Name = "nova-cell-database"
  }
}

# ElastiCache Redis
resource "aws_elasticache_cluster" "nova_redis" {
  cluster_id           = "nova-cell-cache"
  engine              = "redis"
  engine_version      = "7.2"
  node_type           = "cache.r6g.large"
  num_cache_nodes     = 1
  parameter_group_name = "default.redis7"
  port                = 6379
  
  subnet_group_name = aws_elasticache_subnet_group.nova.name
  security_group_ids = [aws_security_group.redis.id]
}

# S3 Buckets
resource "aws_s3_bucket" "nova_models" {
  bucket = "nova-cell-models-${var.environment}"
  
  tags = {
    Name        = "Nova Cell Models"
    Environment = var.environment
  }
}

resource "aws_s3_bucket" "nova_data" {
  bucket = "nova-cell-data-${var.environment}"
  
  tags = {
    Name        = "Nova Cell Data"
    Environment = var.environment
  }
}
```

### 2. Despliegue con Kubernetes

```yaml
# k8s/nova-cell-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nova-api
  namespace: nova-cell
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nova-api
  template:
    metadata:
      labels:
        app: nova-api
    spec:
      containers:
      - name: nova-api
        image: banco.azurecr.io/nova-cell/api:2.0.3
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: nova-secrets
              key: database-url
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: nova-secrets
              key: redis-url
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: nova-api-service
  namespace: nova-cell
spec:
  selector:
    app: nova-api
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nova-api-hpa
  namespace: nova-cell
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nova-api
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

## 🏢 Instalación On-Premises

### 1. Preparación del Servidor

```bash
#!/bin/bash
# Configuración inicial del servidor

# Actualizar sistema
sudo apt-get update && sudo apt-get upgrade -y

# Instalar dependencias
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Configurar firewall
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8000/tcp
sudo ufw allow 3000/tcp
sudo ufw enable

# Configurar límites del sistema
cat >> /etc/security/limits.conf <<EOF
* soft nofile 65536
* hard nofile 65536
* soft nproc 32768
* hard nproc 32768
EOF

# Optimización de kernel
cat >> /etc/sysctl.conf <<EOF
net.core.rmem_max = 134217728
net.core.wmem_max = 134217728
net.ipv4.tcp_rmem = 4096 87380 134217728
net.ipv4.tcp_wmem = 4096 65536 134217728
vm.swappiness = 10
EOF

sudo sysctl -p
```

### 2. Instalación Manual

```bash
# Crear estructura de directorios
sudo mkdir -p /opt/nova-cell/{api,ui,ml,data,logs,config}
sudo mkdir -p /var/log/nova-cell

# Crear usuario del sistema
sudo useradd -r -s /bin/bash -d /opt/nova-cell nova

# Instalar Python y dependencias
sudo apt-get install -y python3.11 python3.11-venv python3-pip

# Crear entorno virtual
cd /opt/nova-cell
python3.11 -m venv venv
source venv/bin/activate

# Instalar dependencias Python
pip install --upgrade pip
pip install -r requirements.txt

# Instalar Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Construir frontend
cd /opt/nova-cell/ui
npm install
npm run build

# Configurar systemd service
sudo cat > /etc/systemd/system/nova-api.service <<EOF
[Unit]
Description=Nova Cell API Service
After=network.target postgresql.service

[Service]
Type=simple
User=nova
Group=nova
WorkingDirectory=/opt/nova-cell/api
Environment="PATH=/opt/nova-cell/venv/bin"
ExecStart=/opt/nova-cell/venv/bin/python app.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Habilitar y arrancar servicio
sudo systemctl daemon-reload
sudo systemctl enable nova-api
sudo systemctl start nova-api
```

## 🔧 Configuración Post-Instalación

### 1. Configuración de Variables de Entorno

```bash
# /opt/nova-cell/config/.env
# Configuración General
APP_NAME=Nova-Cell
APP_ENV=production
APP_DEBUG=false
APP_URL=https://nova.novasolutionsystems.com

# Base de Datos
DB_CONNECTION=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=nova_cell
DB_USERNAME=nova_admin
DB_PASSWORD=secure_password

# Cache y Queue
CACHE_DRIVER=redis
QUEUE_CONNECTION=redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=redis_password

# Seguridad
JWT_SECRET=your-jwt-secret
JWT_TTL=60
ENCRYPTION_KEY=your-encryption-key
CORS_ALLOWED_ORIGINS=https://nova.novasolutionsystems.com

# Modelos de IA
OPENAI_API_KEY=sk-...
OPENAI_ORG_ID=org-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AIza...
AZURE_OPENAI_ENDPOINT=https://banco.openai.azure.com/
AZURE_OPENAI_KEY=...

# Configuración de Logs
LOG_CHANNEL=daily
LOG_LEVEL=info
LOG_DAYS=30

# Métricas y Monitoreo
PROMETHEUS_ENABLED=true
PROMETHEUS_PORT=9090
GRAFANA_ENABLED=true
GRAFANA_PORT=3001

# Límites de Rate
RATE_LIMIT_PER_MINUTE=60
RATE_LIMIT_PER_HOUR=1000

# Storage
STORAGE_DRIVER=s3
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=nova-cell-storage
```

### 2. Integración con Sistemas Bancarios

```python
# config/banking_integration.py
from typing import Dict, Any
import requests
from cryptography.fernet import Fernet

class BankingIntegration:
    """Integración con sistemas core bancarios"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.encryption = Fernet(config['ENCRYPTION_KEY'])
        
    def connect_core_banking(self):
        """Conexión con sistema core bancario"""
        endpoints = {
            'accounts': f"{self.config['CORE_BANKING_URL']}/api/accounts",
            'transactions': f"{self.config['CORE_BANKING_URL']}/api/transactions",
            'customers': f"{self.config['CORE_BANKING_URL']}/api/customers"
        }
        
        headers = {
            'Authorization': f"Bearer {self.config['CORE_BANKING_TOKEN']}",
            'X-API-Key': self.config['CORE_BANKING_API_KEY']
        }
        
        return endpoints, headers
    
    def connect_risk_system(self):
        """Conexión con sistema de riesgos"""
        return {
            'url': self.config['RISK_SYSTEM_URL'],
            'credentials': self.encryption.decrypt(
                self.config['RISK_SYSTEM_CREDENTIALS']
            )
        }
    
    def connect_compliance(self):
        """Conexión con sistema de compliance"""
        return {
            'aml_endpoint': self.config['AML_SYSTEM_URL'],
            'kyc_endpoint': self.config['KYC_SYSTEM_URL'],
            'reporting_endpoint': self.config['REGULATORY_REPORTING_URL']
        }
```

## ✅ Validación de Instalación

### 1. Health Checks

```bash
#!/bin/bash
# Script de validación de salud

echo "🏥 Ejecutando Health Checks..."

# API Health
API_HEALTH=$(curl -s http://localhost:8000/health | jq -r '.status')
if [ "$API_HEALTH" = "healthy" ]; then
    echo "✅ API: Healthy"
else
    echo "❌ API: Unhealthy"
fi

# Database Connection
DB_CHECK=$(docker exec nova-postgres pg_isready -U nova_admin)
if [ $? -eq 0 ]; then
    echo "✅ PostgreSQL: Connected"
else
    echo "❌ PostgreSQL: Disconnected"
fi

# Redis Connection
REDIS_CHECK=$(docker exec nova-redis redis-cli ping)
if [ "$REDIS_CHECK" = "PONG" ]; then
    echo "✅ Redis: Connected"
else
    echo "❌ Redis: Disconnected"
fi

# MongoDB Connection
MONGO_CHECK=$(docker exec nova-mongodb mongosh --eval "db.adminCommand('ping')" --quiet)
if [ $? -eq 0 ]; then
    echo "✅ MongoDB: Connected"
else
    echo "❌ MongoDB: Disconnected"
fi

# ML Service
ML_HEALTH=$(curl -s http://localhost:8001/health | jq -r '.status')
if [ "$ML_HEALTH" = "ready" ]; then
    echo "✅ ML Service: Ready"
else
    echo "❌ ML Service: Not Ready"
fi
```

### 2. Test de Funcionalidad

```python
# tests/test_installation.py
import requests
import json
from datetime import datetime

class NovaInstallationTest:
    """Suite de pruebas post-instalación"""
    
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.token = None
        
    def test_authentication(self):
        """Prueba de autenticación"""
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={
                "email": "ai@novasolutionsystems.com",
                "password": "admin_password"
            }
        )
        assert response.status_code == 200
        self.token = response.json()['token']
        print("✅ Autenticación exitosa")
        
    def test_project_creation(self):
        """Prueba de creación de proyecto"""
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post(
            f"{self.base_url}/api/projects",
            headers=headers,
            json={
                "name": "Test Project",
                "description": "Proyecto de prueba post-instalación",
                "type": "classification"
            }
        )
        assert response.status_code == 201
        print("✅ Creación de proyecto exitosa")
        
    def test_model_inference(self):
        """Prueba de inferencia de modelo"""
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post(
            f"{self.base_url}/api/inference",
            headers=headers,
            json={
                "model": "gpt-4",
                "prompt": "Hello, Nova-Cell!",
                "max_tokens": 50
            }
        )
        assert response.status_code == 200
        print("✅ Inferencia de modelo exitosa")
        
    def run_all_tests(self):
        """Ejecutar todas las pruebas"""
        print("\n🧪 Ejecutando pruebas de instalación...")
        self.test_authentication()
        self.test_project_creation()
        self.test_model_inference()
        print("\n✅ Todas las pruebas pasaron exitosamente!")

if __name__ == "__main__":
    tester = NovaInstallationTest()
    tester.run_all_tests()
```

## 🔧 Troubleshooting Común

### Problemas de Conexión

```bash
# Error: Cannot connect to PostgreSQL
# Solución:
sudo systemctl status postgresql
sudo systemctl restart postgresql
psql -U nova_admin -d nova_cell -c "SELECT 1;"

# Error: Redis connection refused
# Solución:
redis-cli ping
sudo systemctl restart redis
redis-cli CONFIG SET requirepass "your_password"

# Error: Docker daemon not running
# Solución:
sudo systemctl start docker
sudo systemctl enable docker
docker info
```

### Problemas de Permisos

```bash
# Error: Permission denied
# Solución:
sudo chown -R nova:nova /opt/nova-cell
sudo chmod -R 755 /opt/nova-cell
sudo usermod -aG docker nova

# Error: Cannot write to logs
# Solución:
sudo mkdir -p /var/log/nova-cell
sudo chown nova:nova /var/log/nova-cell
sudo chmod 755 /var/log/nova-cell
```

### Problemas de Rendimiento

```bash
# Optimización de PostgreSQL
sudo -u postgres psql -c "ALTER SYSTEM SET shared_buffers = '4GB';"
sudo -u postgres psql -c "ALTER SYSTEM SET effective_cache_size = '12GB';"
sudo -u postgres psql -c "ALTER SYSTEM SET maintenance_work_mem = '1GB';"
sudo systemctl restart postgresql

# Optimización de Docker
cat > /etc/docker/daemon.json <<EOF
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ]
}
EOF
sudo systemctl restart docker
```

## 📚 Recursos Adicionales

### Enlaces Útiles
- 📖 [Documentación Completa](https://docs.nova-cell.novasolutionsystems.com)
- 🎥 [Videos Tutoriales](https://learning.novasolutionsystems.com/nova-cell)
- 💬 [Comunidad Slack](https://banco-ai.slack.com)
- 🐛 [Reporte de Issues](https://jira.novasolutionsystems.com/nova-cell)

### Soporte
- **Email:** ai@novasolutionsystems.com
- **Teléfono:** +52 55 1234 5678
- **Horario:** Lunes a Viernes, 9:00 - 18:00 CST

---

*Última actualización: Enero 2025 | Versión 2.0.3*