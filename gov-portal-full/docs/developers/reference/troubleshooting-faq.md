# 🔧 Troubleshooting y FAQ - Nova-Cell Platform

## 📋 Información General

**Última Actualización:** Enero 2025  
**Versión Platform:** 2.0.3  
**Canales de Soporte:** [Slack](https://banco-ai.slack.com) | [Email](mailto:ai@novasolutionsystems.com)

## 🚨 Problemas Comunes y Soluciones

### 🔴 Errores de Instalación

#### Error: "Docker daemon is not running"

**Síntomas:**
```bash
Cannot connect to the Docker daemon at unix:///var/run/docker.sock
```

**Solución:**
```bash
# macOS
colima start --cpu 4 --memory 8

# Linux
sudo systemctl start docker
sudo systemctl enable docker

# Windows WSL2
wsl --shutdown
# Reiniciar Docker Desktop
```

#### Error: "Port already in use"

**Síntomas:**
```bash
Error: bind: address already in use :8000
```

**Solución:**
```bash
# Encontrar proceso usando el puerto
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Matar proceso
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows

# O cambiar puerto en configuración
export API_PORT=8001
```

#### Error: "Insufficient memory"

**Síntomas:**
```bash
ERROR: Container killed due to memory limit
```

**Solución:**
```bash
# Aumentar límites de Docker
# Docker Desktop: Settings > Resources > Memory: 8GB mínimo

# docker-compose.yml
services:
  nova-api:
    deploy:
      resources:
        limits:
          memory: 4G
        reservations:
          memory: 2G
```

### 🟡 Problemas de Autenticación

#### Error: "401 Unauthorized"

**Causas comunes:**
1. Token expirado
2. Credenciales incorrectas
3. Permisos insuficientes

**Diagnóstico:**
```python
# Verificar token
import jwt
import json

def decode_token(token):
    try:
        # Decodificar sin verificar (solo para debug)
        decoded = jwt.decode(token, options={"verify_signature": False})
        print(json.dumps(decoded, indent=2))
        
        # Verificar expiración
        import time
        if decoded.get('exp', 0) < time.time():
            print("❌ Token expirado")
        else:
            print("✅ Token válido")
            
    except Exception as e:
        print(f"Error decodificando token: {e}")

# Uso
decode_token("eyJ0eXAiOiJKV1Q...")
```

**Solución:**
```python
# Renovar token automáticamente
class TokenManager:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.token_expiry = 0
    
    def get_valid_token(self):
        import time
        
        # Renovar si expira en menos de 5 minutos
        if time.time() > self.token_expiry - 300:
            self.refresh_token()
        
        return self.token
    
    def refresh_token(self):
        response = requests.post(
            "https://api.nova-cell.novasolutionsystems.com/auth/token",
            json={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "client_credentials"
            }
        )
        
        data = response.json()
        self.token = data["access_token"]
        self.token_expiry = time.time() + data["expires_in"]
```

### 🔵 Problemas con Modelos de IA

#### Error: "Rate limit exceeded"

**Síntomas:**
```json
{
  "error": {
    "message": "Rate limit exceeded",
    "type": "rate_limit_error",
    "code": 429
  }
}
```

**Solución:**
```python
# Implementar retry con exponential backoff
import time
from typing import Callable, Any

def retry_with_backoff(
    func: Callable,
    max_retries: int = 5,
    base_delay: float = 1.0
) -> Any:
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if "rate_limit" in str(e):
                delay = base_delay * (2 ** attempt)
                print(f"Rate limited. Waiting {delay}s...")
                time.sleep(delay)
            else:
                raise
    
    raise Exception("Max retries exceeded")

# Uso
result = retry_with_backoff(
    lambda: openai_client.completions.create(...)
)
```

#### Error: "Model timeout"

**Síntomas:**
```
TimeoutError: Request timed out after 30 seconds
```

**Solución:**
```python
# Configurar timeouts apropiados
import httpx

class RobustAIClient:
    def __init__(self):
        self.client = httpx.Client(
            timeout=httpx.Timeout(
                connect=5.0,      # Conexión
                read=60.0,        # Lectura (más tiempo para modelos grandes)
                write=10.0,       # Escritura
                pool=5.0          # Pool de conexiones
            )
        )
    
    async def streaming_inference(self, prompt: str):
        """Usar streaming para respuestas largas"""
        async with httpx.AsyncClient() as client:
            async with client.stream(
                "POST",
                "https://api.nova-cell.novasolutionsystems.com/inference",
                json={"prompt": prompt, "stream": True}
            ) as response:
                async for chunk in response.aiter_text():
                    yield chunk
```

### 🟢 Problemas de Base de Datos

#### Error: "Connection pool exhausted"

**Síntomas:**
```
psycopg2.OperationalError: FATAL: remaining connection slots are reserved
```

**Solución:**
```python
# Configurar pool de conexiones correctamente
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    "postgresql://user:pass@localhost/db",
    poolclass=QueuePool,
    pool_size=20,           # Conexiones permanentes
    max_overflow=40,        # Conexiones adicionales temporales
    pool_pre_ping=True,     # Verificar conexión antes de usar
    pool_recycle=3600,      # Reciclar conexiones cada hora
    echo_pool=True          # Debug del pool
)

# Monitorear uso del pool
from sqlalchemy import event

@event.listens_for(engine, "connect")
def receive_connect(dbapi_conn, connection_record):
    connection_record.info['connect_time'] = time.time()

@event.listens_for(engine, "checkout")
def receive_checkout(dbapi_conn, connection_record, connection_proxy):
    age = time.time() - connection_record.info.get('connect_time', 0)
    if age > 3600:  # Conexión muy vieja
        print(f"⚠️ Connection age: {age}s")
```

#### Error: "Deadlock detected"

**Síntomas:**
```
psycopg2.errors.DeadlockDetected: deadlock detected
```

**Solución:**
```python
# Implementar retry logic para deadlocks
from contextlib import contextmanager
import random
import time

@contextmanager
def safe_transaction(session, max_retries=3):
    """Manejo seguro de transacciones con retry en deadlock"""
    for attempt in range(max_retries):
        try:
            yield session
            session.commit()
            break
        except Exception as e:
            session.rollback()
            
            if "deadlock" in str(e).lower():
                if attempt < max_retries - 1:
                    # Espera aleatoria para evitar colisiones
                    time.sleep(random.uniform(0.1, 0.5))
                    continue
            raise
        finally:
            session.close()

# Uso
with safe_transaction(db_session) as session:
    # Operaciones de base de datos
    pass
```

## ❓ Preguntas Frecuentes (FAQ)

### 🏦 General - Banca y Compliance

**P: ¿Cómo aseguro que mi código cumple con regulaciones CNBV?**

R: Utiliza nuestro checklist de compliance:
```python
# compliance_validator.py
class CNBVComplianceValidator:
    def validate_model(self, model_path: str) -> bool:
        checks = {
            "has_explainability": self.check_explainability(model_path),
            "has_audit_trail": self.check_audit_trail(model_path),
            "has_bias_testing": self.check_bias_testing(model_path),
            "has_data_lineage": self.check_data_lineage(model_path),
            "encrypted_pii": self.check_pii_encryption(model_path)
        }
        
        return all(checks.values())
```

**P: ¿Qué datos NO debo loggear por seguridad?**

R: Nunca loggear:
- Números de cuenta completos
- NIP/PIN
- CVV de tarjetas
- Contraseñas
- Tokens de autenticación
- Información personal identificable (PII) sin encriptar

### 🤖 Modelos de IA

**P: ¿Cuál modelo debo usar para mi caso de uso?**

R: Guía de selección:

| Caso de Uso | Modelo Recomendado | Razón |
|-------------|-------------------|--------|
| Análisis de documentos largos | Claude 3 Opus | Contexto de 200k tokens |
| Respuestas rápidas | GPT-4 Turbo | Baja latencia |
| Análisis financiero | GPT-4 | Mejor con números |
| Generación de código | Claude 3 | Código más limpio |
| Búsqueda semántica | text-embedding-3 | Optimizado para embeddings |
| Clasificación | Gemini Pro | Costo-efectivo |

**P: ¿Cómo optimizo costos de API?**

R: Estrategias de optimización:
```python
# cost_optimizer.py
class AICallOptimizer:
    def optimize(self, prompt: str, context: str) -> Dict:
        # 1. Cache de respuestas frecuentes
        cache_key = hashlib.md5(prompt.encode()).hexdigest()
        if cached := self.cache.get(cache_key):
            return cached
        
        # 2. Comprimir contexto
        compressed = self.compress_context(context)
        
        # 3. Usar modelo más barato primero
        if self.can_use_smaller_model(prompt):
            response = self.call_gpt35(prompt, compressed)
        else:
            response = self.call_gpt4(prompt, compressed)
        
        # 4. Cachear respuesta
        self.cache.set(cache_key, response, ttl=3600)
        
        return response
```

### 🔧 Desarrollo

**P: ¿Cómo debuggeo inferencias de IA?**

R: Usa nuestro debugger integrado:
```python
# debug_inference.py
from nova_cell import AIDebugger

debugger = AIDebugger(verbose=True)

# Captura toda la información de la inferencia
with debugger.trace() as tracer:
    response = model.generate(prompt)
    
# Analiza el trace
print(tracer.get_summary())
# Output:
# - Token count: 1,523
# - Latency: 2.3s
# - Model: gpt-4
# - Temperature: 0.7
# - Cost: $0.045

# Exportar para análisis
tracer.export_to_json("inference_debug.json")
```

**P: ¿Cómo manejo errores de modelos de forma elegante?**

R: Implementa fallback strategy:
```python
class ModelFallbackStrategy:
    def __init__(self):
        self.models = [
            ("gpt-4", self.call_gpt4),
            ("claude-3", self.call_claude),
            ("gemini-pro", self.call_gemini),
            ("local-llama", self.call_local)
        ]
    
    async def generate_with_fallback(self, prompt: str) -> str:
        errors = []
        
        for model_name, model_func in self.models:
            try:
                return await model_func(prompt)
            except Exception as e:
                errors.append(f"{model_name}: {str(e)}")
                continue
        
        # Si todos fallan, usar respuesta predeterminada
        return self.get_default_response(prompt, errors)
```

### 🚀 Performance

**P: Mi API es muy lenta, ¿cómo la optimizo?**

R: Checklist de optimización:

1. **Profiling del código:**
```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Tu código aquí
result = your_slow_function()

profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumulative')
stats.print_stats(10)  # Top 10 funciones lentas
```

2. **Implementar caching:**
```python
from functools import lru_cache
from redis import Redis

redis_client = Redis()

def redis_cache(ttl=3600):
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Check cache
            if cached := redis_client.get(key):
                return json.loads(cached)
            
            # Compute and cache
            result = func(*args, **kwargs)
            redis_client.setex(key, ttl, json.dumps(result))
            
            return result
        return wrapper
    return decorator
```

3. **Usar async/await:**
```python
import asyncio
import aiohttp

async def fetch_all_data(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

### 📊 Monitoreo

**P: ¿Qué métricas debo monitorear en producción?**

R: Métricas esenciales:

```python
# metrics_config.py
ESSENTIAL_METRICS = {
    "business": [
        "transactions_per_second",
        "approval_rate",
        "fraud_detection_rate",
        "customer_satisfaction_score"
    ],
    "technical": [
        "api_latency_p95",
        "error_rate",
        "cpu_usage",
        "memory_usage",
        "database_connections"
    ],
    "ai_specific": [
        "model_accuracy",
        "inference_latency",
        "token_usage",
        "api_costs",
        "cache_hit_rate"
    ],
    "compliance": [
        "audit_trail_completeness",
        "pii_encryption_coverage",
        "regulatory_violations",
        "model_drift"
    ]
}
```

## 🛠️ Scripts de Utilidad

### Diagnóstico Completo del Sistema

```bash
#!/bin/bash
# health_check.sh

echo "🔍 Nova-Cell System Diagnostics"
echo "================================"

# Check services
echo "📡 Checking services..."
services=("nova-api" "postgres" "redis" "mongodb")
for service in "${services[@]}"; do
    if docker ps | grep -q $service; then
        echo "✅ $service: Running"
    else
        echo "❌ $service: Not running"
    fi
done

# Check disk space
echo -e "\n💾 Disk usage:"
df -h | grep -E "/$|/var|/tmp"

# Check memory
echo -e "\n🧠 Memory usage:"
free -h

# Check API health
echo -e "\n🌐 API Health:"
curl -s http://localhost:8000/health | jq '.'

# Check database connections
echo -e "\n🗄️ Database connections:"
docker exec postgres psql -U nova_admin -c \
    "SELECT count(*) as connections FROM pg_stat_activity;"

# Check Redis
echo -e "\n📦 Redis status:"
docker exec redis redis-cli INFO server | grep uptime

# Check logs for errors
echo -e "\n⚠️ Recent errors (last 10):"
docker logs nova-api 2>&1 | grep ERROR | tail -10
```

### Reset de Ambiente de Desarrollo

```bash
#!/bin/bash
# reset_dev_env.sh

echo "🔄 Resetting development environment..."

# Stop all containers
docker-compose down -v

# Clean Docker
docker system prune -af

# Clear caches
rm -rf ~/.cache/pip
rm -rf node_modules
rm -rf __pycache__
find . -type d -name "*.egg-info" -exec rm -rf {} +

# Reset databases
rm -rf data/postgres/*
rm -rf data/mongodb/*
rm -rf data/redis/*

# Reinstall dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt

npm install

# Restart services
docker-compose up -d

echo "✅ Environment reset complete!"
```

## 📞 Contacto y Soporte

### Canales de Soporte

- **🔥 Urgente (P0):** Llamar al +52 55 1234 5678
- **📧 Email:** ai@novasolutionsystems.com
- **💬 Slack:** #nova-cell-support
- **📝 Tickets:** [JIRA](https://banco.atlassian.net/nova)

### SLA de Respuesta

| Prioridad | Descripción | Tiempo de Respuesta |
|-----------|-------------|-------------------|
| P0 | Sistema caído | 15 minutos |
| P1 | Funcionalidad crítica afectada | 1 hora |
| P2 | Funcionalidad degradada | 4 horas |
| P3 | Pregunta o mejora | 24 horas |

### Información para Reporte de Issues

Cuando reportes un issue, incluye:

```markdown
## Descripción del Problema
[Descripción clara del problema]

## Pasos para Reproducir
1. [Paso 1]
2. [Paso 2]
3. [...]

## Comportamiento Esperado
[Qué debería pasar]

## Comportamiento Actual
[Qué está pasando]

## Ambiente
- OS: [macOS/Linux/Windows]
- Nova-Cell Version: [2.0.3]
- Python Version: [3.11]
- Browser: [si aplica]

## Logs Relevantes
```
[Pegar logs aquí]
```

## Screenshots
[Si aplica]
```

---

*Última actualización: Enero 2025 | Versión 2.0.3*