# 🏆 Mejores Prácticas para Desarrollo de IA en Banca

## 📋 Información General

**Versión:** 1.0.0  
**Última Actualización:** Enero 2025  
**Audiencia:** Desarrolladores, Tech Leads, Arquitectos

## 🎯 Principios Fundamentales

### Los 5 Pilares del Desarrollo IA Bancario

1. **Seguridad Primera** - Zero trust, encriptación end-to-end
2. **Explicabilidad** - Decisiones auditables y comprensibles
3. **Cumplimiento** - CNBV, Banxico, CONDUSEF siempre
4. **Rendimiento** - Latencia < 100ms para servicios críticos
5. **Escalabilidad** - Diseño para 10x crecimiento

## 📝 Estándares de Código

### 1. Clean Code para IA

```python
# ❌ MALO - Código poco claro
def proc(d):
    r = []
    for i in d:
        if i['s'] > 700:
            r.append(i)
    return r

# ✅ BUENO - Código autodocumentado
def filter_high_credit_score_customers(customers: List[Customer]) -> List[Customer]:
    """
    Filtra clientes con score crediticio alto (>700).
    
    Args:
        customers: Lista de clientes a evaluar
    
    Returns:
        Lista de clientes con score > 700
    """
    MIN_HIGH_CREDIT_SCORE = 700
    
    return [
        customer for customer in customers
        if customer.credit_score > MIN_HIGH_CREDIT_SCORE
    ]
```

### 2. Documentación Obligatoria

```python
class AIRiskModel:
    """
    Modelo de evaluación de riesgo crediticio usando ML.
    
    Este modelo implementa un ensemble de XGBoost y Random Forest
    para evaluar el riesgo crediticio según normativa CNBV.
    
    Attributes:
        model_version: Versión del modelo en producción
        threshold: Umbral de decisión para aprobación
        explainer: SHAP explainer para interpretabilidad
    
    Example:
        >>> model = AIRiskModel(version="2.0.3")
        >>> risk_score = model.evaluate(customer_data)
        >>> explanation = model.explain(risk_score)
    """
    
    def evaluate(self, customer_data: Dict[str, Any]) -> RiskScore:
        """
        Evalúa riesgo crediticio del cliente.
        
        Args:
            customer_data: Diccionario con información del cliente
                - income: Ingreso mensual (MXN)
                - debt_ratio: Ratio deuda/ingreso
                - credit_history: Historial crediticio (meses)
        
        Returns:
            RiskScore con probabilidad de default y categoría
        
        Raises:
            ValidationError: Si datos del cliente son inválidos
            ModelError: Si el modelo no está cargado
        
        Note:
            Este método registra todas las evaluaciones para auditoría
            según requerimiento regulatorio CNBV-2024-AI-003.
        """
        pass
```

### 3. Testing Comprehensivo

```python
# tests/test_risk_model.py
import pytest
from unittest.mock import Mock, patch
import numpy as np

class TestAIRiskModel:
    """Tests para modelo de riesgo con casos edge bancarios"""
    
    @pytest.fixture
    def model(self):
        """Fixture con modelo pre-entrenado"""
        return AIRiskModel(version="test")
    
    @pytest.fixture
    def valid_customer(self):
        """Cliente con datos válidos típicos"""
        return {
            "income": 50000,
            "debt_ratio": 0.3,
            "credit_history": 24,
            "employment_years": 5
        }
    
    def test_high_income_low_risk(self, model, valid_customer):
        """Alto ingreso debe resultar en bajo riesgo"""
        valid_customer["income"] = 200000
        score = model.evaluate(valid_customer)
        assert score.risk_category == "LOW"
        assert score.probability < 0.1
    
    def test_edge_case_zero_income(self, model, valid_customer):
        """Ingreso cero debe rechazar evaluación"""
        valid_customer["income"] = 0
        with pytest.raises(ValidationError):
            model.evaluate(valid_customer)
    
    def test_model_explainability(self, model, valid_customer):
        """Toda decisión debe ser explicable"""
        score = model.evaluate(valid_customer)
        explanation = model.explain(score)
        
        assert explanation.top_factors is not None
        assert len(explanation.top_factors) >= 3
        assert sum(explanation.feature_importance.values()) > 0.8
    
    @patch('audit_logger.log')
    def test_audit_logging(self, mock_log, model, valid_customer):
        """Verificar logging para auditoría"""
        model.evaluate(valid_customer)
        mock_log.assert_called_once()
        
        log_data = mock_log.call_args[0][0]
        assert "customer_id" in log_data
        assert "decision" in log_data
        assert "timestamp" in log_data
```

## 🤖 Mejores Prácticas de IA

### 1. Prompt Engineering

```python
class PromptTemplate:
    """Templates optimizados para banca"""
    
    @staticmethod
    def credit_analysis_prompt(context: Dict) -> str:
        """Prompt para análisis crediticio"""
        return f"""
        Rol: Eres un analista de crédito senior con 20 años de experiencia en banca mexicana.
        
        Contexto Regulatorio:
        - Normativa CNBV vigente
        - Límites de endeudamiento: 30% del ingreso neto
        - Tasa de interés máxima: CAT no mayor a 35%
        
        Cliente:
        - Ingreso mensual: ${context['income']:,.2f} MXN
        - Historial crediticio: {context['credit_history']} meses
        - Score actual: {context['credit_score']}
        - Propósito del crédito: {context['loan_purpose']}
        
        Tarea:
        1. Evalúa la capacidad de pago
        2. Identifica riesgos potenciales
        3. Recomienda monto y plazo apropiados
        4. Justifica tu decisión con datos específicos
        
        Formato de respuesta:
        - Decisión: [APROBAR/RECHAZAR/REVISAR]
        - Monto recomendado: $X MXN
        - Plazo: X meses
        - Justificación: [máximo 100 palabras]
        - Riesgos identificados: [lista]
        """
    
    @staticmethod
    def optimize_prompt(prompt: str, model: str = "gpt-4") -> str:
        """Optimiza prompt según el modelo"""
        optimizations = {
            "gpt-4": {
                "max_length": 4000,
                "style": "detailed",
                "temperature": 0.3
            },
            "claude-3": {
                "max_length": 8000,
                "style": "conversational",
                "temperature": 0.5
            },
            "gemini-pro": {
                "max_length": 6000,
                "style": "structured",
                "temperature": 0.4
            }
        }
        
        config = optimizations.get(model, optimizations["gpt-4"])
        
        # Truncar si es necesario
        if len(prompt) > config["max_length"]:
            prompt = prompt[:config["max_length"]] + "\n[TRUNCADO]"
        
        return prompt, config["temperature"]
```

### 2. Versionado de Modelos

```python
# model_versioning.py
from datetime import datetime
import hashlib
import json

class ModelVersionManager:
    """Gestión de versiones de modelos ML"""
    
    def __init__(self, storage_backend: str = "s3"):
        self.storage = self._init_storage(storage_backend)
        self.registry = {}
    
    def register_model(
        self,
        model,
        metadata: Dict[str, Any],
        performance_metrics: Dict[str, float]
    ) -> str:
        """Registra nueva versión de modelo"""
        
        # Generar version hash único
        model_bytes = pickle.dumps(model)
        version_hash = hashlib.sha256(model_bytes).hexdigest()[:8]
        
        version_info = {
            "version": f"v{datetime.now().strftime('%Y%m%d')}_{version_hash}",
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": metadata,
            "metrics": performance_metrics,
            "framework": type(model).__module__,
            "parameters": self._extract_params(model),
            "training_data": metadata.get("training_data_version"),
            "compliance": {
                "bias_tested": metadata.get("bias_tested", False),
                "explainability": metadata.get("has_explainer", False),
                "approved_by": metadata.get("approved_by", None)
            }
        }
        
        # Validar métricas mínimas
        if performance_metrics.get("accuracy", 0) < 0.85:
            raise ValueError("Model accuracy below minimum threshold (85%)")
        
        # Guardar modelo y metadata
        self.storage.save(f"models/{version_info['version']}/model.pkl", model_bytes)
        self.storage.save(f"models/{version_info['version']}/metadata.json", 
                         json.dumps(version_info))
        
        self.registry[version_info['version']] = version_info
        
        return version_info['version']
    
    def rollback(self, to_version: str):
        """Rollback a versión anterior"""
        if to_version not in self.registry:
            raise ValueError(f"Version {to_version} not found")
        
        # Log rollback para auditoría
        self._log_rollback(to_version)
        
        # Cargar modelo anterior
        model_bytes = self.storage.load(f"models/{to_version}/model.pkl")
        return pickle.loads(model_bytes)
```

### 3. Optimización de Rendimiento

```python
# performance_optimization.py
from functools import lru_cache
import asyncio
from concurrent.futures import ThreadPoolExecutor
import redis

class AIPerformanceOptimizer:
    """Optimizaciones para servicios de IA"""
    
    def __init__(self):
        self.cache = redis.Redis(host='localhost', port=6379, db=0)
        self.executor = ThreadPoolExecutor(max_workers=10)
    
    @lru_cache(maxsize=1000)
    def cached_inference(self, input_hash: str):
        """Cache de inferencias frecuentes"""
        # Cache en memoria para requests muy frecuentes
        pass
    
    async def batch_inference(self, requests: List[Dict]) -> List[Dict]:
        """Procesa requests en batch para eficiencia"""
        
        # Agrupar por tipo de modelo
        grouped = {}
        for req in requests:
            model_type = req.get("model", "default")
            if model_type not in grouped:
                grouped[model_type] = []
            grouped[model_type].append(req)
        
        # Procesar en paralelo
        tasks = []
        for model_type, batch in grouped.items():
            task = asyncio.create_task(
                self._process_batch(model_type, batch)
            )
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        
        # Flatten results
        return [item for sublist in results for item in sublist]
    
    def optimize_prompt_tokens(self, prompt: str, max_tokens: int = 2000) -> str:
        """Optimiza uso de tokens"""
        
        # Comprimir espacios múltiples
        prompt = " ".join(prompt.split())
        
        # Remover información redundante
        lines = prompt.split("\n")
        unique_lines = []
        seen = set()
        
        for line in lines:
            line_hash = hash(line.strip())
            if line_hash not in seen and line.strip():
                unique_lines.append(line)
                seen.add(line_hash)
        
        optimized = "\n".join(unique_lines)
        
        # Truncar si excede límite
        if len(optimized) > max_tokens * 4:  # ~4 chars per token
            optimized = optimized[:max_tokens * 4]
        
        return optimized
```

## 🔒 Seguridad en Desarrollo

### 1. Gestión de Secretos

```python
# secrets_management.py
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import boto3
from typing import Optional

class SecureSecretsManager:
    """Gestión segura de secretos para banca"""
    
    def __init__(self, provider: str = "azure"):
        self.provider = provider
        self._init_client()
    
    def _init_client(self):
        """Inicializa cliente según proveedor"""
        if self.provider == "azure":
            credential = DefaultAzureCredential()
            vault_url = os.environ["AZURE_KEYVAULT_URL"]
            self.client = SecretClient(vault_url=vault_url, credential=credential)
        elif self.provider == "aws":
            self.client = boto3.client('secretsmanager')
    
    def get_secret(self, secret_name: str) -> Optional[str]:
        """Obtiene secreto de forma segura"""
        try:
            if self.provider == "azure":
                secret = self.client.get_secret(secret_name)
                return secret.value
            elif self.provider == "aws":
                response = self.client.get_secret_value(SecretId=secret_name)
                return response['SecretString']
        except Exception as e:
            # Log pero no exponer detalles del error
            self._log_error(f"Failed to retrieve secret: {secret_name}")
            return None
    
    def rotate_api_keys(self):
        """Rotación automática de API keys"""
        keys_to_rotate = [
            "openai_api_key",
            "anthropic_api_key",
            "google_api_key"
        ]
        
        for key_name in keys_to_rotate:
            # Generar nueva key
            new_key = self._generate_new_key(key_name)
            
            # Guardar nueva versión
            self._save_secret(f"{key_name}_new", new_key)
            
            # Programar rotación
            self._schedule_rotation(key_name)
```

### 2. Validación de Inputs

```python
# input_validation.py
from pydantic import BaseModel, validator, Field
from typing import Optional
import re

class BankingTransactionInput(BaseModel):
    """Validación estricta para transacciones bancarias"""
    
    account_number: str = Field(..., min_length=10, max_length=18)
    amount: float = Field(..., gt=0, le=1000000)
    currency: str = Field(..., regex="^(MXN|USD|EUR)$")
    description: str = Field(..., max_length=200)
    beneficiary_name: str = Field(..., max_length=100)
    reference: Optional[str] = Field(None, max_length=30)
    
    @validator('account_number')
    def validate_account(cls, v):
        """Valida formato de cuenta CLABE"""
        if not re.match(r'^\d{18}$', v):
            raise ValueError('Invalid CLABE format')
        
        # Validar dígito verificador
        if not cls._validate_clabe_checksum(v):
            raise ValueError('Invalid CLABE checksum')
        
        return v
    
    @validator('amount')
    def validate_amount(cls, v):
        """Valida montos según regulación"""
        if v > 100000:  # Transacciones > 100k requieren autorización
            raise ValueError('Amount requires special authorization')
        
        # Máximo 2 decimales
        if round(v, 2) != v:
            raise ValueError('Amount must have max 2 decimal places')
        
        return v
    
    @validator('beneficiary_name')
    def sanitize_name(cls, v):
        """Sanitiza nombre del beneficiario"""
        # Remover caracteres especiales peligrosos
        v = re.sub(r'[<>\"\'%;()&+]', '', v)
        
        # Solo permitir letras, números, espacios y puntos
        if not re.match(r'^[a-zA-Z0-9\s\.\-]+$', v):
            raise ValueError('Invalid characters in beneficiary name')
        
        return v.strip()
    
    @staticmethod
    def _validate_clabe_checksum(clabe: str) -> bool:
        """Valida checksum de CLABE"""
        # Implementación del algoritmo de validación CLABE
        weights = [3, 7, 1] * 6
        total = sum(int(clabe[i]) * weights[i] for i in range(17))
        checksum = (10 - (total % 10)) % 10
        return checksum == int(clabe[17])
```

## 🏗️ Patrones de Arquitectura

### 1. Microservicios para IA

```yaml
# docker-compose.microservices.yml
version: '3.9'

services:
  # API Gateway
  api-gateway:
    image: kong:3.0
    environment:
      KONG_DATABASE: "off"
      KONG_DECLARATIVE_CONFIG: /kong/kong.yml
    ports:
      - "8000:8000"
    volumes:
      - ./kong.yml:/kong/kong.yml
    networks:
      - ai-network

  # Servicio de Inferencia
  inference-service:
    build: ./services/inference
    environment:
      MODEL_CACHE_SIZE: "10GB"
      MAX_BATCH_SIZE: "32"
      TIMEOUT_SECONDS: "30"
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 8G
          cpus: '4'
    networks:
      - ai-network

  # Servicio de Procesamiento de Documentos
  document-processor:
    build: ./services/document-processor
    environment:
      OCR_ENGINE: "tesseract"
      PDF_MAX_SIZE: "100MB"
    volumes:
      - document-storage:/data
    networks:
      - ai-network

  # Servicio de Evaluación de Riesgos
  risk-evaluator:
    build: ./services/risk-evaluator
    environment:
      RISK_MODEL_VERSION: "2.0.3"
      COMPLIANCE_MODE: "strict"
    depends_on:
      - postgres
      - redis
    networks:
      - ai-network

  # Circuit Breaker / Service Mesh
  linkerd:
    image: linkerd/linkerd:stable
    ports:
      - "9990:9990"
    networks:
      - ai-network

networks:
  ai-network:
    driver: overlay
    attachable: true

volumes:
  document-storage:
```

### 2. Event-Driven Architecture

```python
# event_driven_ai.py
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict
import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import json

@dataclass
class AIEvent:
    """Evento base para arquitectura event-driven"""
    event_id: str
    event_type: str
    timestamp: datetime
    payload: Dict[str, Any]
    metadata: Dict[str, Any]

class AIEventBus:
    """Bus de eventos para servicios de IA"""
    
    def __init__(self, kafka_servers: str):
        self.kafka_servers = kafka_servers
        self.producer = None
        self.consumers = {}
    
    async def start(self):
        """Inicializa productor y consumidores"""
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.kafka_servers,
            value_serializer=lambda v: json.dumps(v).encode()
        )
        await self.producer.start()
    
    async def publish_event(self, topic: str, event: AIEvent):
        """Publica evento al bus"""
        event_data = {
            "event_id": event.event_id,
            "event_type": event.event_type,
            "timestamp": event.timestamp.isoformat(),
            "payload": event.payload,
            "metadata": event.metadata
        }
        
        await self.producer.send(topic, event_data)
    
    async def subscribe(self, topic: str, handler):
        """Suscribe handler a topic"""
        consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers=self.kafka_servers,
            value_deserializer=lambda m: json.loads(m.decode())
        )
        
        await consumer.start()
        self.consumers[topic] = consumer
        
        # Procesar eventos
        async for msg in consumer:
            try:
                await handler(msg.value)
            except Exception as e:
                # Log error pero continuar procesando
                print(f"Error processing event: {e}")

# Ejemplo de uso
async def handle_model_training_complete(event_data: Dict):
    """Handler para evento de entrenamiento completado"""
    model_id = event_data["payload"]["model_id"]
    metrics = event_data["payload"]["metrics"]
    
    # Triggear evaluación de compliance
    if metrics["accuracy"] > 0.9:
        await trigger_compliance_check(model_id)
    
    # Actualizar dashboard
    await update_metrics_dashboard(model_id, metrics)
    
    # Notificar stakeholders
    await send_notification(
        f"Model {model_id} training complete. Accuracy: {metrics['accuracy']}"
    )

# Setup
event_bus = AIEventBus("localhost:9092")
await event_bus.start()
await event_bus.subscribe("model.training.complete", handle_model_training_complete)
```

## 🚀 CI/CD para IA

### 1. Pipeline de Deployment

```yaml
# .github/workflows/ai-deploy.yml
name: AI Model Deployment Pipeline

on:
  push:
    branches: [main]
    paths:
      - 'models/**'
      - 'services/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Validate Model
        run: |
          python scripts/validate_model.py \
            --model-path ./models/latest \
            --min-accuracy 0.85 \
            --max-bias 0.05
      
      - name: Security Scan
        run: |
          pip install bandit safety
          bandit -r services/
          safety check
      
      - name: Compliance Check
        run: |
          python scripts/compliance_check.py \
            --regulations CNBV,BASEL_III \
            --model-path ./models/latest

  test:
    needs: validate
    runs-on: ubuntu-latest
    strategy:
      matrix:
        test-type: [unit, integration, performance]
    
    steps:
      - name: Run ${{ matrix.test-type }} tests
        run: |
          pytest tests/${{ matrix.test-type }} \
            --cov=services \
            --cov-report=xml \
            --junitxml=results.xml

  deploy-staging:
    needs: test
    runs-on: ubuntu-latest
    environment: staging
    
    steps:
      - name: Deploy to Staging
        run: |
          kubectl apply -f k8s/staging/ \
            --namespace=nova-staging
      
      - name: Run Smoke Tests
        run: |
          python tests/smoke/test_staging.py \
            --endpoint=${{ secrets.STAGING_ENDPOINT }}
      
      - name: A/B Test Setup
        run: |
          python scripts/setup_ab_test.py \
            --variant-a current \
            --variant-b candidate \
            --traffic-split 90:10

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    if: github.ref == 'refs/heads/main'
    
    steps:
      - name: Blue-Green Deployment
        run: |
          # Deploy to green environment
          kubectl apply -f k8s/production/green/ \
            --namespace=nova-prod
          
          # Health check
          python scripts/health_check.py \
            --endpoint=${{ secrets.GREEN_ENDPOINT }}
          
          # Switch traffic
          kubectl patch service nova-api \
            -p '{"spec":{"selector":{"version":"green"}}}'
          
          # Keep blue for rollback
          kubectl label deployment nova-api-blue \
            rollback-version=previous
```

### 2. Monitoring y Observabilidad

```python
# monitoring.py
from prometheus_client import Counter, Histogram, Gauge
import time
from functools import wraps
from opentelemetry import trace
from opentelemetry.exporter.jaeger import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Métricas Prometheus
inference_counter = Counter('ai_inference_total', 'Total AI inferences', ['model', 'status'])
inference_duration = Histogram('ai_inference_duration_seconds', 'Inference duration', ['model'])
model_accuracy = Gauge('ai_model_accuracy', 'Current model accuracy', ['model', 'version'])
active_models = Gauge('ai_active_models', 'Number of active models')

# Tracing con Jaeger
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

def monitor_inference(model_name: str):
    """Decorator para monitorear inferencias"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Start tracing
            with tracer.start_as_current_span(f"inference_{model_name}") as span:
                span.set_attribute("model.name", model_name)
                span.set_attribute("model.version", kwargs.get("version", "unknown"))
                
                # Measure duration
                start_time = time.time()
                
                try:
                    result = func(*args, **kwargs)
                    
                    # Update metrics
                    inference_counter.labels(model=model_name, status="success").inc()
                    duration = time.time() - start_time
                    inference_duration.labels(model=model_name).observe(duration)
                    
                    span.set_attribute("inference.duration", duration)
                    span.set_attribute("inference.success", True)
                    
                    return result
                    
                except Exception as e:
                    inference_counter.labels(model=model_name, status="error").inc()
                    span.set_attribute("inference.success", False)
                    span.set_attribute("error.message", str(e))
                    raise
                    
        return wrapper
    return decorator

# Ejemplo de uso
@monitor_inference("credit_risk_model")
def evaluate_credit_risk(customer_data: Dict) -> float:
    """Evalúa riesgo crediticio con monitoreo"""
    # Tu lógica aquí
    pass
```

## 📚 Recursos y Herramientas

### Herramientas Esenciales
- **Pre-commit hooks**: `pre-commit install`
- **Linting**: `black`, `pylint`, `flake8`
- **Type checking**: `mypy`
- **Security**: `bandit`, `safety`
- **Testing**: `pytest`, `pytest-cov`

### Configuración Recomendada

```toml
# pyproject.toml
[tool.black]
line-length = 100
target-version = ['py311']

[tool.pylint]
max-line-length = 100
disable = ["C0111", "R0903"]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
minversion = "7.0"
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-ra --strict-markers --cov=src --cov-fail-under=80"
```

---

*Última actualización: Enero 2025 | Versión 1.0.0*