# 🖥️ Nova-Cell CLI

## Herramienta de Línea de Comandos para Desarrolladores de IA

**Versión:** 2.0.3 | **Licencia:** Enterprise | **Compatibilidad:** Windows, macOS, Linux

## 📋 Información General

Nova-Cell CLI es la interfaz de línea de comandos oficial para interactuar con la plataforma Nova-Cell. Diseñada para desarrolladores y DevOps, proporciona acceso completo a todas las funcionalidades de la plataforma desde tu terminal.

## 🚀 Instalación

### Requisitos Previos
- Python 3.9+ o Node.js 18+
- 4GB RAM mínimo
- Conexión a Internet
- Credenciales de Nova-Cell

### Métodos de Instalación

#### Opción 1: pip (Python)
```bash
# Instalación global
pip install nova-cell-cli

# Instalación en entorno virtual (recomendado)
python -m venv nova-env
source nova-env/bin/activate  # Linux/macOS
nova-env\Scripts\activate      # Windows
pip install nova-cell-cli
```

#### Opción 2: npm (Node.js)
```bash
# Instalación global
npm install -g @nova-cell/cli

# Instalación local
npm install --save-dev @nova-cell/cli
```

#### Opción 3: Binario Standalone
```bash
# macOS
curl -L https://nova-cell.novasolutionsystems.com/cli/latest/mac -o nova
chmod +x nova
sudo mv nova /usr/local/bin/

# Linux
wget https://nova-cell.novasolutionsystems.com/cli/latest/linux -O nova
chmod +x nova
sudo mv nova /usr/local/bin/

# Windows (PowerShell como Admin)
Invoke-WebRequest -Uri https://nova-cell.novasolutionsystems.com/cli/latest/windows -OutFile nova.exe
Move-Item nova.exe C:\Windows\System32\
```

## 🔧 Configuración Inicial

### 1. Autenticación
```bash
# Configurar credenciales
nova auth login

# Se abrirá el navegador para autenticación OAuth
# O usa API key directamente:
nova auth login --api-key YOUR_API_KEY

# Verificar autenticación
nova auth status
```

### 2. Configuración de Ambiente
```bash
# Configurar ambiente por defecto
nova config set default-env production

# Configurar región
nova config set region mx-central-1

# Configurar organización
nova config set org banco-xyz

# Ver configuración actual
nova config list
```

## 📚 Comandos Principales

### 🎯 Gestión de Proyectos

```bash
# Crear nuevo proyecto
nova project create my-ai-app \
  --template banking-chatbot \
  --team risk-management

# Listar proyectos
nova project list

# Cambiar proyecto activo
nova project use my-ai-app

# Clonar proyecto existente
nova project clone project-id --name new-project

# Eliminar proyecto
nova project delete my-old-project --confirm
```

### 🤖 Gestión de Modelos

```bash
# Listar modelos disponibles
nova model list --provider all

# Desplegar modelo
nova model deploy gpt-4 \
  --name customer-service-bot \
  --replicas 3 \
  --memory 8Gi

# Configurar modelo
nova model config customer-service-bot \
  --temperature 0.7 \
  --max-tokens 2000 \
  --system-prompt "Eres un asistente bancario..."

# Monitorear modelo
nova model monitor customer-service-bot --follow

# Versionar modelo
nova model version create \
  --model customer-service-bot \
  --tag v1.2.0 \
  --message "Mejorado manejo de consultas de crédito"
```

### 📊 Datos y Entrenamiento

```bash
# Subir dataset
nova data upload ./data/training.csv \
  --name credit-scoring-data \
  --type structured \
  --encrypt

# Procesar datos
nova data process credit-scoring-data \
  --pipeline cleaning,normalization,split \
  --output processed-data

# Entrenar modelo
nova train start \
  --data processed-data \
  --algorithm xgboost \
  --hyperparams '{"max_depth": 6, "learning_rate": 0.1}' \
  --validation-split 0.2

# Ver progreso de entrenamiento
nova train status job-123 --watch

# Evaluar modelo
nova evaluate model-456 \
  --metrics accuracy,precision,recall,f1 \
  --test-data test-set
```

### 🚀 Despliegue y CI/CD

```bash
# Desplegar a producción
nova deploy \
  --env production \
  --strategy blue-green \
  --health-check-url /health \
  --rollback-on-failure

# Crear pipeline CI/CD
nova pipeline create \
  --name ml-pipeline \
  --config ./nova-pipeline.yml

# Ejecutar pipeline
nova pipeline run ml-pipeline \
  --branch main \
  --wait

# Rollback
nova rollback \
  --env production \
  --to-version v1.1.0 \
  --reason "Detectado incremento en latencia"
```

### 📈 Monitoreo y Logs

```bash
# Ver métricas en tiempo real
nova metrics show \
  --service customer-service-bot \
  --period 1h \
  --interval 1m

# Streaming de logs
nova logs -f \
  --service all \
  --level error \
  --since 2h

# Alertas
nova alert create \
  --name high-latency \
  --condition "latency_p95 > 500ms" \
  --action email,slack \
  --severity critical

# Dashboard
nova dashboard open \
  --browser chrome \
  --fullscreen
```

### 🔒 Seguridad y Compliance

```bash
# Escaneo de seguridad
nova security scan \
  --project my-ai-app \
  --type full \
  --compliance cnbv,gdpr

# Auditoría
nova audit trail \
  --from 2024-01-01 \
  --to 2024-01-31 \
  --export pdf

# Gestión de secretos
nova secret create \
  --name db-password \
  --value "$(read -s -p 'Enter password: ' && echo $REPLY)" \
  --encrypt

# Validación de compliance
nova compliance check \
  --standard cnbv \
  --model customer-service-bot \
  --generate-report
```

## 🎨 Comandos Avanzados

### Framework Agéntico

```bash
# Crear agente
nova agent create \
  --name financial-analyst \
  --capabilities "data_analysis,reporting,forecasting" \
  --model gpt-4

# Orquestar múltiples agentes
nova orchestrate \
  --task "Analyze quarterly report" \
  --agents analyst,validator,reporter \
  --timeout 5m

# Ver historial de agentes
nova agent history \
  --agent financial-analyst \
  --last 10
```

### RAG (Retrieval Augmented Generation)

```bash
# Indexar documentos
nova rag index \
  --source ./documents \
  --type pdf,docx,txt \
  --embedding text-embedding-3

# Consultar knowledge base
nova rag query \
  "¿Cuáles son los requisitos CNBV para modelos de riesgo?" \
  --sources regulations \
  --top-k 5

# Actualizar índice
nova rag update \
  --incremental \
  --source ./new-documents
```

### Batch Processing

```bash
# Crear job batch
nova batch create \
  --input ./batch-requests.jsonl \
  --model gpt-4 \
  --parallel 10 \
  --output ./results

# Monitorear batch
nova batch status job-789 --progress

# Cancelar batch
nova batch cancel job-789
```

## 🛠️ Configuración Avanzada

### Archivo de Configuración

```yaml
# ~/.nova-cell/config.yml
version: 2
defaults:
  environment: production
  region: mx-central-1
  organization: banco-xyz

profiles:
  development:
    api_endpoint: https://dev.nova-cell.novasolutionsystems.com
    timeout: 30
    retry_attempts: 3
    
  production:
    api_endpoint: https://api.nova-cell.novasolutionsystems.com
    timeout: 60
    retry_attempts: 5
    ssl_verify: true

models:
  default_provider: openai
  fallback_providers:
    - anthropic
    - google
  
  cost_optimization: true
  cache_responses: true
  cache_ttl: 3600

monitoring:
  metrics_enabled: true
  tracing_enabled: true
  log_level: info
  
security:
  encrypt_traffic: true
  audit_all_commands: true
  mfa_required: true
```

### Variables de Entorno

```bash
# Configuración via variables de entorno
export NOVA_CELL_API_KEY="your-api-key"
export NOVA_CELL_ENV="production"
export NOVA_CELL_REGION="mx-central-1"
export NOVA_CELL_TIMEOUT="60"
export NOVA_CELL_DEBUG="false"
export NOVA_CELL_COLOR_OUTPUT="true"
```

## 📝 Ejemplos de Uso

### Ejemplo 1: Flujo Completo de Desarrollo

```bash
#!/bin/bash
# nova-dev-workflow.sh

# 1. Crear proyecto
nova project create credit-scorer --template ml-classification

# 2. Subir y procesar datos
nova data upload ./historical-loans.csv --encrypt
nova data process historical-loans --pipeline standard

# 3. Entrenar modelo
nova train start \
  --data processed-historical-loans \
  --algorithm random-forest \
  --auto-tune

# 4. Evaluar
nova evaluate latest-model --comprehensive

# 5. Si métricas OK, desplegar
if nova evaluate latest-model --metric accuracy --threshold 0.95; then
  nova deploy --env staging --auto-scale
fi

# 6. Monitorear
nova monitor --dashboard --alert-on-drift
```

### Ejemplo 2: Pipeline de CI/CD

```yaml
# nova-pipeline.yml
version: 1
name: ml-deployment-pipeline

stages:
  - name: validate
    steps:
      - nova lint check
      - nova security scan --quick
      - nova test unit
      
  - name: build
    steps:
      - nova build --optimize
      - nova package --format docker
      
  - name: test
    parallel: true
    steps:
      - nova test integration
      - nova test performance
      - nova compliance check --standard cnbv
      
  - name: deploy
    approval: required
    steps:
      - nova deploy --env production --strategy canary
      - nova monitor --duration 30m --rollback-on-error
```

### Ejemplo 3: Automatización con Scripts

```python
#!/usr/bin/env python3
# nova_automation.py

import subprocess
import json

def run_nova_command(command):
    """Ejecuta comando Nova-Cell y retorna resultado"""
    result = subprocess.run(
        f"nova {command} --json",
        shell=True,
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)

# Obtener métricas de todos los modelos
models = run_nova_command("model list")

for model in models["items"]:
    metrics = run_nova_command(f"metrics show --model {model['id']} --period 24h")
    
    # Alertar si latencia alta
    if metrics["latency_p95"] > 500:
        run_nova_command(
            f"alert trigger high-latency --model {model['id']} "
            f"--value {metrics['latency_p95']}"
        )
    
    # Auto-escalar si necesario
    if metrics["cpu_usage"] > 80:
        current_replicas = model["replicas"]
        new_replicas = min(current_replicas + 2, 10)
        run_nova_command(
            f"model scale {model['id']} --replicas {new_replicas}"
        )
```

## 🔍 Troubleshooting

### Problemas Comunes

#### Error de Autenticación
```bash
# Problema: Token expirado
nova auth refresh

# Problema: Permisos insuficientes
nova auth whoami  # Verificar rol
nova auth permissions  # Ver permisos actuales
```

#### Timeout en Comandos
```bash
# Aumentar timeout
nova --timeout 300 model deploy large-model

# Usar modo async
nova model deploy large-model --async
nova job status <job-id>  # Verificar después
```

#### Problemas de Conectividad
```bash
# Verificar conectividad
nova doctor --network

# Usar proxy
export HTTPS_PROXY=http://proxy.novasolutionsystems.com:8080
nova --proxy model list

# Modo offline (comandos limitados)
nova --offline project list --cached
```

## 🎓 Recursos Adicionales

### Documentación
- [Referencia Completa de Comandos](https://docs.nova-cell.mx/cli/reference)
- [Guías y Tutoriales](https://docs.nova-cell.mx/cli/guides)
- [Ejemplos de Código](https://github.com/banco/nova-cell-examples)

### Herramientas Complementarias
- **Nova-Cell VS Code Extension:** Integración con IDE
- **Nova-Cell GitHub Actions:** CI/CD automatizado
- **Nova-Cell Terraform Provider:** Infrastructure as Code

### Soporte
- 📧 Email: cli-support@nova-cell.mx
- 💬 Slack: #nova-cli-support
- 🐛 Issues: [GitHub](https://github.com/banco/nova-cell-cli/issues)

## 🔄 Actualizaciones

### Verificar Versión
```bash
nova version
nova version --check-update
```

### Actualizar CLI
```bash
# pip
pip install --upgrade nova-cell-cli

# npm
npm update -g @nova-cell/cli

# Auto-actualización
nova self-update
```

### Changelog
```bash
# Ver cambios recientes
nova changelog

# Ver cambios de versión específica
nova changelog --version 2.0.3
```

---

<div style="background: #f0f9ff; border-left: 4px solid #0284c7; padding: 15px; margin: 20px 0;">
  <strong>💡 Pro Tip:</strong> Usa <code>nova --help</code> en cualquier momento para obtener ayuda contextual. Cada comando tiene su propia página de ayuda detallada con ejemplos.
</div>

---

*Nova-Cell CLI v2.0.3 | [Volver al Hub](./nova-cell-hub.md) | [Web UI →](./nova-cell-webui.md)*