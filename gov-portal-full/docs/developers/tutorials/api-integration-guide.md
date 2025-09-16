# 🔌 Guía de Integración API Nova-Cell

## 📋 Información General

**Versión API:** 2.0  
**Última Actualización:** Enero 2025  
**Base URL:** `https://api.nova-cell.novasolutionsystems.com/v2`

## 🔐 Autenticación

### OAuth 2.0 / JWT

```python
# Python - Obtener token
import requests

def get_access_token(client_id, client_secret):
    """Obtener token de acceso OAuth"""
    response = requests.post(
        "https://api.nova-cell.novasolutionsystems.com/v2/auth/token",
        json={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }
    )
    return response.json()["access_token"]

# Usar token en requests
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
```

```javascript
// JavaScript - Autenticación
async function authenticate(clientId, clientSecret) {
    const response = await fetch('https://api.nova-cell.novasolutionsystems.com/v2/auth/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            client_id: clientId,
            client_secret: clientSecret,
            grant_type: 'client_credentials'
        })
    });
    
    const data = await response.json();
    return data.access_token;
}
```

## 📡 REST API

### 1. Proyectos de IA

#### Crear Proyecto
```python
import requests
from typing import Dict, Any

class NovaProjectAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    def create_project(self, project_data: Dict[str, Any]):
        """Crear nuevo proyecto de IA"""
        response = requests.post(
            f"{self.base_url}/projects",
            json={
                "name": project_data["name"],
                "description": project_data["description"],
                "type": "classification",  # classification, nlp, vision
                "config": {
                    "model": "gpt-4",
                    "temperature": 0.7,
                    "max_tokens": 2000
                },
                "metadata": {
                    "department": "risk_management",
                    "compliance_level": "high"
                }
            },
            headers=self.headers
        )
        return response.json()
    
    def list_projects(self, filters: Dict = None):
        """Listar proyectos con filtros"""
        params = filters or {}
        response = requests.get(
            f"{self.base_url}/projects",
            params=params,
            headers=self.headers
        )
        return response.json()
```

#### CRUD Completo
```javascript
// JavaScript - Cliente API completo
class NovaAPIClient {
    constructor(baseUrl, token) {
        this.baseUrl = baseUrl;
        this.headers = {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        };
    }
    
    // CREATE
    async createResource(endpoint, data) {
        const response = await fetch(`${this.baseUrl}/${endpoint}`, {
            method: 'POST',
            headers: this.headers,
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }
        
        return response.json();
    }
    
    // READ
    async getResource(endpoint, id = null) {
        const url = id ? `${this.baseUrl}/${endpoint}/${id}` : `${this.baseUrl}/${endpoint}`;
        const response = await fetch(url, {
            headers: this.headers
        });
        
        return response.json();
    }
    
    // UPDATE
    async updateResource(endpoint, id, data) {
        const response = await fetch(`${this.baseUrl}/${endpoint}/${id}`, {
            method: 'PUT',
            headers: this.headers,
            body: JSON.stringify(data)
        });
        
        return response.json();
    }
    
    // DELETE
    async deleteResource(endpoint, id) {
        const response = await fetch(`${this.baseUrl}/${endpoint}/${id}`, {
            method: 'DELETE',
            headers: this.headers
        });
        
        return response.ok;
    }
}
```

### 2. Manejo de Errores

```python
# Python - Manejo robusto de errores
from enum import Enum
from typing import Optional
import logging

class APIError(Exception):
    """Custom API Exception"""
    def __init__(self, status_code: int, message: str, details: Optional[Dict] = None):
        self.status_code = status_code
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

class APIClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token
        self.logger = logging.getLogger(__name__)
    
    def _handle_response(self, response):
        """Manejo centralizado de respuestas"""
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 201:
            return response.json()
        elif response.status_code == 204:
            return None
        elif response.status_code == 400:
            raise APIError(400, "Bad Request", response.json())
        elif response.status_code == 401:
            raise APIError(401, "Unauthorized - Token may be expired")
        elif response.status_code == 403:
            raise APIError(403, "Forbidden - Insufficient permissions")
        elif response.status_code == 404:
            raise APIError(404, "Resource not found")
        elif response.status_code == 429:
            retry_after = response.headers.get('Retry-After', '60')
            raise APIError(429, f"Rate limit exceeded. Retry after {retry_after}s")
        elif response.status_code >= 500:
            raise APIError(response.status_code, "Server error occurred")
        else:
            raise APIError(response.status_code, "Unexpected error")
    
    def safe_request(self, method: str, endpoint: str, **kwargs):
        """Wrapper seguro para requests con retry logic"""
        max_retries = 3
        retry_delay = 1
        
        for attempt in range(max_retries):
            try:
                response = requests.request(
                    method,
                    f"{self.base_url}/{endpoint}",
                    headers={"Authorization": f"Bearer {self.token}"},
                    **kwargs
                )
                return self._handle_response(response)
                
            except APIError as e:
                if e.status_code == 429 and attempt < max_retries - 1:
                    time.sleep(retry_delay * (2 ** attempt))
                    continue
                raise
            except requests.exceptions.ConnectionError:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                raise
```

## 🎨 GraphQL API

### 1. Configuración Cliente

```python
# Python - Cliente GraphQL
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

class NovaGraphQLClient:
    def __init__(self, url: str, token: str):
        transport = AIOHTTPTransport(
            url=url,
            headers={'Authorization': f'Bearer {token}'}
        )
        self.client = Client(transport=transport, fetch_schema_from_transport=True)
    
    def execute_query(self, query_string: str, variables: Dict = None):
        """Ejecutar query GraphQL"""
        query = gql(query_string)
        return self.client.execute(query, variable_values=variables)

# Ejemplo de uso
client = NovaGraphQLClient(
    "https://api.nova-cell.novasolutionsystems.com/graphql",
    access_token
)

# Query para obtener proyectos
projects_query = """
    query GetProjects($status: String, $limit: Int) {
        projects(status: $status, limit: $limit) {
            edges {
                node {
                    id
                    name
                    description
                    status
                    metrics {
                        accuracy
                        latency
                        cost
                    }
                    models {
                        id
                        name
                        version
                    }
                }
            }
            pageInfo {
                hasNextPage
                endCursor
            }
        }
    }
"""

result = client.execute_query(
    projects_query,
    variables={"status": "active", "limit": 10}
)
```

### 2. Mutations

```javascript
// JavaScript - GraphQL Mutations
import { GraphQLClient } from 'graphql-request';

const client = new GraphQLClient('https://api.nova-cell.novasolutionsystems.com/graphql', {
    headers: {
        authorization: `Bearer ${token}`,
    },
});

// Mutation para crear modelo
const CREATE_MODEL = `
    mutation CreateModel($input: CreateModelInput!) {
        createModel(input: $input) {
            model {
                id
                name
                type
                config
                status
            }
            errors {
                field
                message
            }
        }
    }
`;

async function createAIModel(modelData) {
    try {
        const variables = {
            input: {
                projectId: modelData.projectId,
                name: modelData.name,
                type: 'CHAT_COMPLETION',
                provider: 'OPENAI',
                config: {
                    model: 'gpt-4',
                    temperature: 0.7,
                    maxTokens: 2000,
                    systemPrompt: modelData.systemPrompt
                }
            }
        };
        
        const response = await client.request(CREATE_MODEL, variables);
        return response.createModel;
    } catch (error) {
        console.error('GraphQL Error:', error);
        throw error;
    }
}
```

### 3. Subscriptions

```python
# Python - WebSocket Subscriptions
import asyncio
from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport

async def subscribe_to_model_updates(project_id: str):
    """Suscribirse a actualizaciones de modelo en tiempo real"""
    
    transport = WebsocketsTransport(
        url='wss://api.nova-cell.novasolutionsystems.com/graphql',
        headers={'Authorization': f'Bearer {token}'}
    )
    
    async with Client(transport=transport) as session:
        subscription = gql("""
            subscription OnModelUpdate($projectId: ID!) {
                modelUpdated(projectId: $projectId) {
                    id
                    status
                    metrics {
                        accuracy
                        latency
                        throughput
                    }
                    timestamp
                }
            }
        """)
        
        async for result in session.subscribe(
            subscription,
            variable_values={'projectId': project_id}
        ):
            print(f"Model update: {result}")
            # Procesar actualización
            await process_model_update(result)
```

## 🤖 Integración de Modelos de IA

### 1. Multi-Model Orchestration

```python
# Python - Orquestación de múltiples modelos
from typing import List, Dict, Any
from enum import Enum
import asyncio

class ModelProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    AZURE = "azure"

class MultiModelOrchestrator:
    """Orquestador para múltiples proveedores de IA"""
    
    def __init__(self, api_keys: Dict[str, str]):
        self.providers = self._initialize_providers(api_keys)
        self.fallback_order = [
            ModelProvider.OPENAI,
            ModelProvider.ANTHROPIC,
            ModelProvider.GOOGLE
        ]
    
    def _initialize_providers(self, api_keys: Dict[str, str]):
        """Inicializar proveedores disponibles"""
        providers = {}
        
        if api_keys.get("openai"):
            from openai import OpenAI
            providers[ModelProvider.OPENAI] = OpenAI(api_key=api_keys["openai"])
        
        if api_keys.get("anthropic"):
            from anthropic import Anthropic
            providers[ModelProvider.ANTHROPIC] = Anthropic(api_key=api_keys["anthropic"])
        
        if api_keys.get("google"):
            import google.generativeai as genai
            genai.configure(api_key=api_keys["google"])
            providers[ModelProvider.GOOGLE] = genai
        
        return providers
    
    async def generate_with_fallback(
        self,
        prompt: str,
        preferred_provider: ModelProvider = ModelProvider.OPENAI,
        **kwargs
    ) -> Dict[str, Any]:
        """Generar respuesta con fallback automático"""
        
        # Intentar con proveedor preferido
        providers_to_try = [preferred_provider] + [
            p for p in self.fallback_order if p != preferred_provider
        ]
        
        for provider in providers_to_try:
            if provider not in self.providers:
                continue
                
            try:
                response = await self._call_provider(provider, prompt, **kwargs)
                return {
                    "provider": provider.value,
                    "response": response,
                    "success": True
                }
            except Exception as e:
                print(f"Error with {provider.value}: {e}")
                continue
        
        raise Exception("All providers failed")
    
    async def _call_provider(
        self,
        provider: ModelProvider,
        prompt: str,
        **kwargs
    ) -> str:
        """Llamar a proveedor específico"""
        
        if provider == ModelProvider.OPENAI:
            client = self.providers[provider]
            response = client.chat.completions.create(
                model=kwargs.get("model", "gpt-4"),
                messages=[{"role": "user", "content": prompt}],
                temperature=kwargs.get("temperature", 0.7),
                max_tokens=kwargs.get("max_tokens", 2000)
            )
            return response.choices[0].message.content
        
        elif provider == ModelProvider.ANTHROPIC:
            client = self.providers[provider]
            response = client.messages.create(
                model=kwargs.get("model", "claude-3-opus-20240229"),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=kwargs.get("max_tokens", 2000)
            )
            return response.content[0].text
        
        elif provider == ModelProvider.GOOGLE:
            genai = self.providers[provider]
            model = genai.GenerativeModel(kwargs.get("model", "gemini-pro"))
            response = model.generate_content(prompt)
            return response.text

# Uso del orquestador
orchestrator = MultiModelOrchestrator({
    "openai": "sk-...",
    "anthropic": "sk-ant-...",
    "google": "AIza..."
})

response = await orchestrator.generate_with_fallback(
    prompt="Analiza este documento bancario...",
    preferred_provider=ModelProvider.OPENAI,
    temperature=0.5
)
```

### 2. RAG Implementation

```python
# Python - RAG con LangChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import os

class BankingRAGSystem:
    """Sistema RAG para documentos bancarios"""
    
    def __init__(self, openai_api_key: str, persist_directory: str = "./chroma_db"):
        os.environ["OPENAI_API_KEY"] = openai_api_key
        self.embeddings = OpenAIEmbeddings()
        self.persist_directory = persist_directory
        self.vectorstore = None
        self.qa_chain = None
    
    def load_documents(self, document_paths: List[str]):
        """Cargar y procesar documentos bancarios"""
        documents = []
        
        for path in document_paths:
            if path.endswith('.pdf'):
                loader = PyPDFLoader(path)
                documents.extend(loader.load())
        
        # Dividir documentos en chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        chunks = text_splitter.split_documents(documents)
        
        # Crear o actualizar vectorstore
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        self.vectorstore.persist()
        
        # Crear cadena QA
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(temperature=0),
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(
                search_kwargs={"k": 4}
            ),
            return_source_documents=True
        )
    
    def query(self, question: str) -> Dict[str, Any]:
        """Consultar el sistema RAG"""
        if not self.qa_chain:
            raise ValueError("No documents loaded")
        
        result = self.qa_chain({"query": question})
        
        return {
            "answer": result["result"],
            "sources": [
                {
                    "content": doc.page_content[:200],
                    "metadata": doc.metadata
                }
                for doc in result["source_documents"]
            ]
        }

# Uso del sistema RAG
rag_system = BankingRAGSystem(openai_api_key="sk-...")

# Cargar documentos regulatorios
rag_system.load_documents([
    "docs/cnbv_regulations.pdf",
    "docs/basel_iii.pdf",
    "docs/aml_guidelines.pdf"
])

# Consultar
response = rag_system.query(
    "¿Cuáles son los requisitos de capital según Basilea III?"
)
print(response["answer"])
```

## 🏦 APIs Específicas de Banca

### 1. Procesamiento de Transacciones

```python
# Python - API de transacciones bancarias
from decimal import Decimal
from datetime import datetime
from typing import Optional
import hashlib
import hmac

class TransactionAPI:
    """API para procesamiento seguro de transacciones"""
    
    def __init__(self, base_url: str, api_key: str, secret_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
    
    def _generate_signature(self, payload: str) -> str:
        """Generar firma HMAC para seguridad"""
        return hmac.new(
            self.secret_key.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()
    
    def process_transaction(
        self,
        amount: Decimal,
        source_account: str,
        destination_account: str,
        transaction_type: str,
        metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Procesar transacción con validaciones"""
        
        # Validar monto
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Preparar payload
        transaction_data = {
            "amount": str(amount),
            "source_account": source_account,
            "destination_account": destination_account,
            "type": transaction_type,
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": metadata or {}
        }
        
        # Generar firma
        payload_str = json.dumps(transaction_data, sort_keys=True)
        signature = self._generate_signature(payload_str)
        
        # Enviar request
        response = requests.post(
            f"{self.base_url}/transactions",
            json=transaction_data,
            headers={
                "X-API-Key": self.api_key,
                "X-Signature": signature,
                "Content-Type": "application/json"
            }
        )
        
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Transaction failed: {response.text}")
    
    def verify_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """Verificar estado de transacción"""
        response = requests.get(
            f"{self.base_url}/transactions/{transaction_id}",
            headers={"X-API-Key": self.api_key}
        )
        return response.json()
```

### 2. Evaluación de Riesgos

```javascript
// JavaScript - Sistema de evaluación de riesgos
class RiskAssessmentAPI {
    constructor(baseUrl, apiKey) {
        this.baseUrl = baseUrl;
        this.apiKey = apiKey;
    }
    
    async assessCreditRisk(customerData) {
        // Preparar datos para evaluación
        const riskPayload = {
            customer_id: customerData.id,
            financial_data: {
                annual_income: customerData.income,
                debt_to_income: customerData.debtRatio,
                credit_score: customerData.creditScore,
                employment_years: customerData.employmentYears
            },
            loan_details: {
                amount: customerData.loanAmount,
                term_months: customerData.loanTerm,
                purpose: customerData.loanPurpose
            },
            behavioral_data: {
                payment_history: customerData.paymentHistory,
                account_age_months: customerData.accountAge,
                utilization_rate: customerData.utilizationRate
            }
        };
        
        // Llamar API de evaluación
        const response = await fetch(`${this.baseUrl}/risk/credit/assess`, {
            method: 'POST',
            headers: {
                'X-API-Key': this.apiKey,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(riskPayload)
        });
        
        const result = await response.json();
        
        // Interpretar resultados
        return {
            risk_score: result.score,
            risk_level: this.getRiskLevel(result.score),
            factors: result.contributing_factors,
            recommendations: result.recommendations,
            confidence: result.confidence_interval
        };
    }
    
    getRiskLevel(score) {
        if (score < 300) return 'VERY_HIGH';
        if (score < 500) return 'HIGH';
        if (score < 650) return 'MEDIUM';
        if (score < 750) return 'LOW';
        return 'VERY_LOW';
    }
    
    async monitorTransactionRisk(transaction) {
        // Monitoreo en tiempo real de transacciones sospechosas
        const features = {
            amount: transaction.amount,
            merchant_category: transaction.merchantCategory,
            location: transaction.location,
            time_of_day: new Date(transaction.timestamp).getHours(),
            frequency_24h: transaction.recentTransactionCount,
            amount_deviation: transaction.amountDeviation
        };
        
        const response = await fetch(`${this.baseUrl}/risk/transaction/monitor`, {
            method: 'POST',
            headers: {
                'X-API-Key': this.apiKey,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(features)
        });
        
        return response.json();
    }
}
```

### 3. Compliance y Auditoría

```python
# Python - Sistema de compliance y auditoría
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any
import json

class ComplianceAPI:
    """API para verificaciones de compliance y auditoría"""
    
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.audit_trail = []
    
    def kyc_verification(self, customer_data: Dict[str, Any]) -> Dict[str, Any]:
        """Verificación Know Your Customer (KYC)"""
        
        verification_request = {
            "request_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "customer": {
                "id": customer_data.get("id"),
                "name": customer_data.get("full_name"),
                "document_type": customer_data.get("document_type"),
                "document_number": customer_data.get("document_number"),
                "date_of_birth": customer_data.get("date_of_birth"),
                "address": customer_data.get("address")
            },
            "checks_requested": [
                "identity_verification",
                "pep_screening",  # Politically Exposed Person
                "sanctions_screening",
                "adverse_media"
            ]
        }
        
        # Log para auditoría
        self._log_audit_event("KYC_VERIFICATION_INITIATED", verification_request)
        
        # Llamar API de verificación
        response = requests.post(
            f"{self.base_url}/compliance/kyc/verify",
            json=verification_request,
            headers=self._get_headers()
        )
        
        result = response.json()
        
        # Log resultado
        self._log_audit_event("KYC_VERIFICATION_COMPLETED", result)
        
        return {
            "verification_id": result["verification_id"],
            "status": result["status"],
            "risk_score": result["risk_score"],
            "checks": result["checks"],
            "requires_manual_review": result["risk_score"] > 70
        }
    
    def aml_screening(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Anti-Money Laundering (AML) screening"""
        
        screening_request = {
            "transaction_id": transaction_data["id"],
            "amount": transaction_data["amount"],
            "currency": transaction_data["currency"],
            "source": transaction_data["source_account"],
            "destination": transaction_data["destination_account"],
            "patterns": self._detect_patterns(transaction_data)
        }
        
        response = requests.post(
            f"{self.base_url}/compliance/aml/screen",
            json=screening_request,
            headers=self._get_headers()
        )
        
        return response.json()
    
    def _detect_patterns(self, transaction: Dict) -> List[str]:
        """Detectar patrones sospechosos"""
        patterns = []
        
        # Structuring detection
        if transaction["amount"] == 9999:
            patterns.append("POSSIBLE_STRUCTURING")
        
        # Rapid movement
        if transaction.get("rapid_transfer"):
            patterns.append("RAPID_MOVEMENT")
        
        # Round amounts
        if transaction["amount"] % 1000 == 0:
            patterns.append("ROUND_AMOUNT")
        
        return patterns
    
    def generate_regulatory_report(
        self,
        report_type: str,
        start_date: datetime,
        end_date: datetime
    ) -> Dict[str, Any]:
        """Generar reportes regulatorios"""
        
        report_request = {
            "type": report_type,  # CNBV, CONDUSEF, etc.
            "period": {
                "start": start_date.isoformat(),
                "end": end_date.isoformat()
            },
            "format": "JSON",  # JSON, XML, PDF
            "include_sections": [
                "executive_summary",
                "transaction_analysis",
                "risk_metrics",
                "compliance_violations",
                "recommendations"
            ]
        }
        
        response = requests.post(
            f"{self.base_url}/compliance/reports/generate",
            json=report_request,
            headers=self._get_headers()
        )
        
        return response.json()
    
    def _log_audit_event(self, event_type: str, data: Dict[str, Any]):
        """Registrar evento para auditoría"""
        audit_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "data": data,
            "user": "system",
            "ip_address": "127.0.0.1"
        }
        
        self.audit_trail.append(audit_entry)
        
        # Persistir en base de datos
        requests.post(
            f"{self.base_url}/audit/log",
            json=audit_entry,
            headers=self._get_headers()
        )
    
    def _get_headers(self) -> Dict[str, str]:
        """Headers para requests"""
        return {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json",
            "X-Audit-User": "compliance_system"
        }
```

## 📊 Monitoreo y Métricas

### Rate Limiting y Throttling

```python
# Python - Implementación de rate limiting
from functools import wraps
from datetime import datetime, timedelta
import redis
import time

class RateLimiter:
    """Rate limiter con Redis"""
    
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
    
    def limit(self, key: str, max_requests: int, window_seconds: int):
        """Decorator para rate limiting"""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Generar key única
                limit_key = f"rate_limit:{key}:{datetime.now().strftime('%Y%m%d%H%M')}"
                
                # Incrementar contador
                current = self.redis.incr(limit_key)
                
                # Establecer TTL en primera request
                if current == 1:
                    self.redis.expire(limit_key, window_seconds)
                
                # Verificar límite
                if current > max_requests:
                    raise Exception(f"Rate limit exceeded: {max_requests} requests per {window_seconds}s")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator

# Uso del rate limiter
redis_client = redis.Redis(host='localhost', port=6379, db=0)
limiter = RateLimiter(redis_client)

@limiter.limit("api_calls", max_requests=100, window_seconds=60)
def call_api():
    # Tu código aquí
    pass
```

## 🔒 Mejores Prácticas de Seguridad

### 1. Encriptación de Datos Sensibles

```python
# Python - Encriptación para datos bancarios
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
import base64
import os

class BankingDataEncryption:
    """Encriptación para datos sensibles bancarios"""
    
    def __init__(self, master_key: str):
        # Derivar key desde master key
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'stable_salt',  # En producción, usar salt único
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_key.encode()))
        self.cipher = Fernet(key)
    
    def encrypt_pii(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Encriptar información personal identificable"""
        sensitive_fields = ['ssn', 'account_number', 'credit_card', 'pin']
        encrypted_data = data.copy()
        
        for field in sensitive_fields:
            if field in encrypted_data:
                value = str(encrypted_data[field])
                encrypted_data[field] = self.cipher.encrypt(value.encode()).decode()
        
        return encrypted_data
    
    def decrypt_pii(self, encrypted_data: Dict[str, Any]) -> Dict[str, Any]:
        """Desencriptar información"""
        sensitive_fields = ['ssn', 'account_number', 'credit_card', 'pin']
        decrypted_data = encrypted_data.copy()
        
        for field in sensitive_fields:
            if field in decrypted_data:
                encrypted_value = decrypted_data[field].encode()
                decrypted_data[field] = self.cipher.decrypt(encrypted_value).decode()
        
        return decrypted_data
```

### 2. Validación y Sanitización

```javascript
// JavaScript - Validación de inputs
class InputValidator {
    static validateAccountNumber(accountNumber) {
        // Formato: 10-12 dígitos
        const pattern = /^\d{10,12}$/;
        if (!pattern.test(accountNumber)) {
            throw new Error('Invalid account number format');
        }
        return accountNumber;
    }
    
    static validateAmount(amount) {
        const numAmount = parseFloat(amount);
        if (isNaN(numAmount) || numAmount <= 0) {
            throw new Error('Invalid amount');
        }
        // Máximo 2 decimales
        return Math.round(numAmount * 100) / 100;
    }
    
    static sanitizeInput(input) {
        // Remover caracteres peligrosos
        return input
            .replace(/[<>]/g, '')
            .replace(/javascript:/gi, '')
            .replace(/on\w+=/gi, '')
            .trim();
    }
    
    static validateEmail(email) {
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!pattern.test(email)) {
            throw new Error('Invalid email format');
        }
        return email.toLowerCase();
    }
}
```

## 📚 Recursos Adicionales

### SDKs Oficiales
- [Python SDK](https://github.com/banco/nova-cell-python-sdk)
- [JavaScript SDK](https://github.com/banco/nova-cell-js-sdk)
- [Java SDK](https://github.com/banco/nova-cell-java-sdk)

### Herramientas de Testing
- [Postman Collection](https://api.nova-cell.novasolutionsystems.com/postman)
- [Swagger UI](https://api.nova-cell.novasolutionsystems.com/swagger)
- [GraphQL Playground](https://api.nova-cell.novasolutionsystems.com/graphql-playground)

### Documentación
- [API Reference](https://docs.nova-cell.novasolutionsystems.com/api)
- [Webhooks Guide](https://docs.nova-cell.novasolutionsystems.com/webhooks)
- [Error Codes](https://docs.nova-cell.novasolutionsystems.com/errors)

---

*Última actualización: Enero 2025 | API Version 2.0*