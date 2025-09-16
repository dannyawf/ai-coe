---
title: API Documentation - Centro de Excelencia IA
tags:
  - api
  - technical
  - integration
  - documentation
search:
  boost: 3
---

# API Documentation - Ecosistema CoE IA

<div class="nova-card">
  <div class="nova-accent-border">
    <h2>🔌 APIs del Centro de Excelencia de IA</h2>
    <p>Documentación técnica completa de las APIs RESTful del ecosistema CoE IA, incluyendo Knowledge Hub, Nova-Cell Platform, Governance & Compliance, y Analytics. Cumple con estándares OpenAPI 3.0 y mejores prácticas de la industria.</p>
  </div>
</div>

## 📑 Tabla de Contenidos

1. [Overview de APIs del CoE](#overview-de-apis-del-coe)
2. [Knowledge Hub API](#knowledge-hub-api)
3. [Nova-Cell Platform API](#nova-cell-platform-api)
4. [Governance & Compliance API](#governance-compliance-api)
5. [Analytics & Metrics API](#analytics-metrics-api)
6. [Webhooks & Events](#webhooks-events)
7. [SDKs y Client Libraries](#sdks-y-client-libraries)
8. [Ejemplos y Tutoriales](#ejemplos-y-tutoriales)

## 🏗️ Overview de APIs del CoE

### Arquitectura de APIs

La arquitectura del CoE IA se basa en microservicios RESTful orquestados mediante un API Gateway seguro:

```mermaid
graph TB
    A[Client Applications] --> B[API Gateway]
    B --> C[Authentication Service]
    B --> D[Knowledge Hub API]
    B --> E[Nova-Cell API]
    B --> F[Governance API]
    B --> G[Analytics API]
    D --> H[(PostgreSQL + pgvector)]
    E --> I[(Supabase Storage)]
    F --> J[(Audit Logs)]
    G --> K[(Metrics DB)]
```

### Base URL y Versionado

```yaml
production:
  base_url: https://api.coe-ia.banco.mx
  version: v1
  full_path: https://api.coe-ia.banco.mx/api/v1

staging:
  base_url: https://api-staging.coe-ia.banco.mx
  version: v1
```

### Autenticación y Autorización

Todas las APIs requieren autenticación mediante OAuth2/JWT:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### Obtener Token

```http
POST /auth/token
Content-Type: application/json

{
  "grant_type": "client_credentials",
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "scope": "read write admin"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...",
  "scope": "read write admin"
}
```

### Rate Limiting y Quotas

| Tier | Requests/Hour | Burst Limit | Headers Response |
|------|---------------|-------------|------------------|
| **Basic** | 1,000 | 50/min | `X-RateLimit-Limit: 1000` |
| **Premium** | 10,000 | 500/min | `X-RateLimit-Remaining: 9985` |
| **Enterprise** | 100,000 | 5000/min | `X-RateLimit-Reset: 1641024000` |

#### Error de Rate Limit (429)

```json
{
  "error": "RATE_LIMIT_EXCEEDED",
  "message": "API rate limit exceeded. Please retry after 60 seconds.",
  "retry_after": 60,
  "documentation": "https://docs.coe-ia.banco.mx/rate-limits"
}
```

## 📚 Knowledge Hub API

### Endpoints Principales

#### 1. Crear Artefacto (Prompt)

```http
POST /api/v1/prompts
Content-Type: application/json
Authorization: Bearer <token>

{
  "titulo": "Asistente de Análisis Crediticio",
  "descripcion": "Analiza solicitudes de crédito y evalúa riesgo",
  "texto": "Eres un especialista en análisis crediticio bancario...",
  "categoria": "credit-scoring",
  "tags": ["credito", "riesgo", "scoring"],
  "modelo_compatible": ["GPT-4", "Claude-2"],
  "departamento": "Riesgos",
  "caso_uso_bancario": "Evaluación automatizada de solicitudes de crédito personal",
  "metricas_esperadas": {
    "precision": 0.95,
    "tiempo_respuesta_ms": 500
  },
  "compliance": {
    "normativas": ["CNBV", "LFPDPPP"],
    "nivel_riesgo": "MEDIO"
  }
}
```

**Response (201 Created):**
```json
{
  "id": "prmpt_7f8a9b2c3d4e5f6g",
  "titulo": "Asistente de Análisis Crediticio",
  "estado": "PENDING_REVIEW",
  "version": "1.0.0",
  "created_at": "2025-01-10T10:30:00Z",
  "created_by": "user_123",
  "review_url": "https://knowledge-hub.banco.mx/review/prmpt_7f8a9b2c3d4e5f6g",
  "estimated_review_time": "2-3 días hábiles"
}
```

#### 2. Búsqueda Semántica

```http
POST /api/v1/search/semantic
Content-Type: application/json
Authorization: Bearer <token>

{
  "query": "detector de fraude en transacciones internacionales",
  "filters": {
    "categoria": ["fraud-detection", "aml"],
    "estado": "APPROVED",
    "departamento": ["Riesgos", "Compliance"]
  },
  "limit": 10,
  "similarity_threshold": 0.75,
  "include_metadata": true
}
```

**Response:**
```json
{
  "total_results": 3,
  "query_embedding_model": "text-embedding-ada-002",
  "results": [
    {
      "id": "prmpt_8g9h0i1j2k3l",
      "titulo": "Detector de Fraude SWIFT",
      "similarity_score": 0.89,
      "categoria": "fraud-detection",
      "descripcion": "Detecta patrones anómalos en transacciones SWIFT",
      "metadata": {
        "uso_count": 1247,
        "rating_promedio": 4.8,
        "ultima_actualizacion": "2025-01-05T14:20:00Z"
      }
    },
    {
      "id": "agnt_4m5n6o7p8q9r",
      "titulo": "Agente AML Internacional",
      "similarity_score": 0.82,
      "categoria": "aml",
      "descripcion": "Monitorea transacciones cross-border para prevención de lavado"
    }
  ]
}
```

#### 3. Obtener Métricas de Uso

```http
GET /api/v1/metrics/artifact/{id}
Authorization: Bearer <token>
```

**Response:**
```json
{
  "artifact_id": "prmpt_7f8a9b2c3d4e5f6g",
  "periodo": "2025-01",
  "metricas": {
    "total_usos": 3456,
    "usuarios_unicos": 89,
    "departamentos": ["Riesgos", "Operaciones", "Tecnología"],
    "tiempo_promedio_respuesta_ms": 234,
    "tasa_exito": 0.97,
    "feedback": {
      "positivo": 3201,
      "negativo": 45,
      "neutral": 210
    }
  },
  "tendencia": {
    "crecimiento_mensual": "+15%",
    "proyeccion_proximos_30_dias": 4100
  }
}
```

#### 4. Versionado de Artefactos

```http
GET /api/v1/prompts/{id}/versions
Authorization: Bearer <token>
```

**Response:**
```json
{
  "artifact_id": "prmpt_7f8a9b2c3d4e5f6g",
  "current_version": "2.1.0",
  "versions": [
    {
      "version": "2.1.0",
      "estado": "APPROVED",
      "fecha": "2025-01-08T10:00:00Z",
      "cambios": "Optimización para casos de crédito hipotecario",
      "aprobado_por": "risk_committee"
    },
    {
      "version": "2.0.0",
      "estado": "DEPRECATED",
      "fecha": "2024-12-15T09:30:00Z",
      "cambios": "Mejora en análisis de riesgo"
    },
    {
      "version": "1.0.0",
      "estado": "ARCHIVED",
      "fecha": "2024-11-01T08:00:00Z",
      "cambios": "Versión inicial"
    }
  ]
}
```

## 🚀 Nova-Cell Platform API

### Code Generation

#### Generar Código

```http
POST /api/v1/nova-cell/generate-code
Content-Type: application/json
Authorization: Bearer <token>

{
  "requisitos": "Crear un servicio REST para gestión de cuentas bancarias con CRUD completo",
  "lenguaje": "Java",
  "framework": "Spring Boot",
  "especificaciones": {
    "base_datos": "PostgreSQL",
    "autenticacion": "JWT",
    "documentacion": "OpenAPI 3.0"
  },
  "compliance": {
    "estandares": ["PCI-DSS", "ISO-27001"],
    "incluir_auditoria": true,
    "encriptacion_datos": true
  },
  "opciones": {
    "generar_tests": true,
    "coverage_minimo": 80,
    "incluir_dockerfile": true
  }
}
```

**Response:**
```json
{
  "request_id": "req_9s8t7u6v5w4x",
  "estado": "COMPLETED",
  "archivos_generados": [
    {
      "path": "src/main/java/mx/banco/accounts/controller/AccountController.java",
      "tipo": "controller",
      "lineas": 156,
      "codigo": "package mx.banco.accounts.controller;\n\nimport org.springframework.web.bind.annotation.*;\n..."
    },
    {
      "path": "src/main/java/mx/banco/accounts/service/AccountService.java",
      "tipo": "service",
      "lineas": 203
    },
    {
      "path": "src/test/java/mx/banco/accounts/AccountControllerTest.java",
      "tipo": "test",
      "lineas": 189,
      "coverage": 85
    }
  ],
  "metricas": {
    "tiempo_generacion_ms": 3450,
    "lineas_totales": 892,
    "archivos_totales": 12,
    "complejidad_ciclomatica": 4.2
  },
  "compliance_check": {
    "PCI_DSS": "PASS",
    "ISO_27001": "PASS",
    "vulnerabilidades_detectadas": 0
  }
}
```

### Security Scanning

```http
POST /api/v1/nova-cell/security-scan
Content-Type: application/json
Authorization: Bearer <token>

{
  "codigo_fuente": "base64_encoded_source_code_here...",
  "lenguaje": "Java",
  "tipo_escaneo": "FULL",
  "estandares": ["OWASP-Top10", "PCI-DSS", "CWE-Top25"]
}
```

**Response:**
```json
{
  "scan_id": "scan_3x4y5z6a7b8c",
  "timestamp": "2025-01-10T11:45:00Z",
  "resultado": "ISSUES_FOUND",
  "resumen": {
    "total_issues": 3,
    "criticos": 0,
    "altos": 1,
    "medios": 2,
    "bajos": 0
  },
  "vulnerabilidades": [
    {
      "id": "VUL-001",
      "tipo": "SQL_INJECTION",
      "severidad": "HIGH",
      "archivo": "UserRepository.java",
      "linea": 45,
      "descripcion": "Posible SQL Injection en query dinámico",
      "cwe_id": "CWE-89",
      "owasp_category": "A03:2021",
      "remediacion": {
        "descripcion": "Usar PreparedStatement en lugar de concatenación",
        "codigo_sugerido": "PreparedStatement ps = conn.prepareStatement(\"SELECT * FROM users WHERE id = ?\");\nps.setLong(1, userId);"
      }
    }
  ],
  "recomendaciones": [
    "Implementar validación de entrada en todos los endpoints",
    "Actualizar dependencias a versiones sin vulnerabilidades conocidas",
    "Añadir rate limiting a APIs públicas"
  ]
}
```

### Testing Automation

```http
POST /api/v1/nova-cell/generate-tests
Content-Type: application/json
Authorization: Bearer <token>

{
  "archivo_fuente": "src/main/java/TransactionService.java",
  "tipo_tests": ["unit", "integration"],
  "framework": "JUnit5",
  "opciones": {
    "incluir_mocks": true,
    "coverage_objetivo": 90,
    "incluir_edge_cases": true,
    "incluir_performance_tests": false
  }
}
```

## 🛡️ Governance & Compliance API

### AISIA Evaluation

```http
POST /api/v1/governance/aisia-evaluate
Content-Type: application/json
Authorization: Bearer <token>

{
  "sistema_ia": {
    "nombre": "Sistema de Scoring Crediticio v3",
    "tipo": "modelo_predictivo",
    "proposito": "Evaluación automática de riesgo crediticio"
  },
  "datos": {
    "tipos_datos": ["personales", "financieros", "comportamentales"],
    "volumen_registros": 500000,
    "contiene_datos_sensibles": true
  },
  "impacto": {
    "usuarios_afectados": 100000,
    "decisiones_automatizadas": true,
    "impacto_financiero": "ALTO"
  },
  "contexto_regulatorio": {
    "normativas_aplicables": ["LFPDPPP", "CNBV", "EU-AI-Act"],
    "requiere_explicabilidad": true
  }
}
```

**Response:**
```json
{
  "evaluation_id": "aisia_9d8e7f6g5h4i",
  "fecha_evaluacion": "2025-01-10T12:00:00Z",
  "resultado": {
    "nivel_riesgo": "ALTO",
    "score_riesgo": 78,
    "categoria_eu_ai_act": "HIGH_RISK",
    "requiere_evaluacion_adicional": true
  },
  "hallazgos": [
    {
      "categoria": "BIAS_RISK",
      "descripcion": "Riesgo de sesgo en variables demográficas",
      "severidad": "ALTA",
      "mitigacion_requerida": true
    },
    {
      "categoria": "TRANSPARENCY",
      "descripcion": "Necesidad de mayor explicabilidad en decisiones",
      "severidad": "MEDIA"
    }
  ],
  "requisitos_compliance": [
    {
      "normativa": "LFPDPPP",
      "requisito": "Consentimiento explícito para tratamiento de datos",
      "estado": "PENDIENTE"
    },
    {
      "normativa": "CNBV",
      "requisito": "Validación de modelo por área independiente",
      "estado": "EN_PROCESO"
    }
  ],
  "proximos_pasos": [
    "Completar evaluación de sesgo algorítmico",
    "Implementar mecanismos de explicabilidad",
    "Obtener aprobación del Comité de Riesgos"
  ]
}
```

### Risk Assessment

```http
GET /api/v1/governance/risk-assessment/{system_id}
Authorization: Bearer <token>
```

**Response:**
```json
{
  "system_id": "sys_2a3b4c5d6e7f",
  "assessment_date": "2025-01-10",
  "risk_matrix": {
    "operational_risk": {
      "level": "MEDIUM",
      "score": 6.5,
      "factors": ["complejidad_tecnica", "dependencias_externas"]
    },
    "compliance_risk": {
      "level": "HIGH",
      "score": 8.2,
      "factors": ["datos_sensibles", "decisiones_automatizadas"]
    },
    "reputational_risk": {
      "level": "MEDIUM",
      "score": 5.8,
      "factors": ["visibilidad_publica", "impacto_clientes"]
    },
    "financial_risk": {
      "level": "LOW",
      "score": 3.2,
      "factors": ["costo_implementacion", "roi_esperado"]
    }
  },
  "overall_risk": {
    "level": "MEDIUM-HIGH",
    "score": 6.9,
    "trend": "DECREASING"
  },
  "mitigation_plan": {
    "controles_implementados": 12,
    "controles_pendientes": 5,
    "fecha_proxima_revision": "2025-02-10"
  }
}
```

### Audit Logging

```http
GET /api/v1/governance/audit-logs
Authorization: Bearer <token>
Query Parameters:
  - start_date: 2025-01-01
  - end_date: 2025-01-10
  - entity_type: prompt
  - action: CREATE,UPDATE
  - page: 1
  - limit: 50
```

**Response:**
```json
{
  "pagination": {
    "page": 1,
    "limit": 50,
    "total_records": 237,
    "total_pages": 5
  },
  "logs": [
    {
      "log_id": "log_8h7g6f5e4d3c",
      "timestamp": "2025-01-10T09:15:30Z",
      "usuario": {
        "id": "usr_123",
        "nombre": "Maria Garcia",
        "departamento": "Data Science"
      },
      "accion": "CREATE",
      "entidad": {
        "tipo": "prompt",
        "id": "prmpt_7f8a9b2c3d4e5f6g",
        "nombre": "Asistente de Análisis Crediticio"
      },
      "detalles": {
        "ip_address": "10.0.1.45",
        "user_agent": "Mozilla/5.0...",
        "cambios": {
          "campos_modificados": ["titulo", "texto", "tags"]
        }
      },
      "resultado": "SUCCESS"
    }
  ]
}
```

## 📊 Analytics & Metrics API

### IMPACT Framework Metrics

```http
GET /api/v1/analytics/impact
Authorization: Bearer <token>
Query Parameters:
  - period: monthly
  - year: 2025
  - month: 1
```

**Response:**
```json
{
  "periodo": "2025-01",
  "framework": "IMPACT",
  "metricas": {
    "implementation": {
      "descripcion": "Velocidad y eficiencia de implementación",
      "kpis": {
        "tiempo_implementacion_promedio_dias": 7.3,
        "cobertura_equipos": "85%",
        "adopcion_semanal": "92%",
        "proyectos_activos": 47
      },
      "tendencia": "IMPROVING",
      "score": 8.5
    },
    "momentum": {
      "descripcion": "Velocidad de adopción y crecimiento",
      "kpis": {
        "nuevos_usuarios_mes": 127,
        "crecimiento_uso": "+27%",
        "engagement_rate": "72%",
        "retention_30_dias": "89%"
      },
      "tendencia": "STABLE",
      "score": 7.8
    },
    "performance": {
      "descripcion": "Rendimiento técnico y operacional",
      "kpis": {
        "latencia_p95_ms": 190,
        "uptime": "99.92%",
        "errores_por_millon": 23,
        "throughput_req_sec": 1250
      },
      "tendencia": "IMPROVING",
      "score": 9.2
    },
    "acceptance": {
      "descripcion": "Aceptación y satisfacción de usuarios",
      "kpis": {
        "nps_score": 52,
        "satisfaccion_usuarios": "4.6/5",
        "tasa_recomendacion": "78%",
        "tickets_soporte_resueltos": "94%"
      },
      "tendencia": "IMPROVING",
      "score": 8.1
    },
    "cost_effective": {
      "descripcion": "Eficiencia de costos y ROI",
      "kpis": {
        "roi_actual": "162%",
        "costo_por_transaccion": "$0.03",
        "ahorro_mensual": "$48,000",
        "payback_period_meses": 8
      },
      "tendencia": "STABLE",
      "score": 8.7
    },
    "trust": {
      "descripcion": "Confianza y cumplimiento",
      "kpis": {
        "compliance_score": "100%",
        "incidentes_seguridad": 0,
        "auditorias_pasadas": "5/5",
        "confianza_stakeholders": "86%"
      },
      "tendencia": "STABLE",
      "score": 9.5
    }
  },
  "score_global": 8.6,
  "recomendaciones": [
    "Aumentar cobertura de equipos al 95%",
    "Mejorar NPS mediante programa de feedback",
    "Optimizar latencia en servicios críticos"
  ]
}
```

### Usage Analytics

```http
GET /api/v1/analytics/usage
Authorization: Bearer <token>
Query Parameters:
  - start_date: 2025-01-01
  - end_date: 2025-01-10
  - group_by: endpoint
```

**Response:**
```json
{
  "periodo": {
    "inicio": "2025-01-01T00:00:00Z",
    "fin": "2025-01-10T23:59:59Z"
  },
  "resumen": {
    "total_requests": 156789,
    "usuarios_unicos": 342,
    "endpoints_utilizados": 28,
    "tiempo_respuesta_promedio_ms": 234
  },
  "por_endpoint": [
    {
      "endpoint": "/api/v1/prompts",
      "metodo": "GET",
      "requests": 45678,
      "porcentaje": "29.1%",
      "tiempo_promedio_ms": 180
    },
    {
      "endpoint": "/api/v1/search/semantic",
      "metodo": "POST",
      "requests": 23456,
      "porcentaje": "15.0%",
      "tiempo_promedio_ms": 320
    }
  ],
  "por_departamento": [
    {
      "departamento": "Data Science",
      "requests": 67890,
      "porcentaje": "43.3%"
    },
    {
      "departamento": "Riesgos",
      "requests": 34567,
      "porcentaje": "22.0%"
    }
  ],
  "errores": {
    "total": 234,
    "tasa_error": "0.15%",
    "por_codigo": {
      "400": 89,
      "401": 45,
      "429": 67,
      "500": 33
    }
  }
}
```

## 🔔 Webhooks & Events

### Event Types

```yaml
eventos_disponibles:
  artefactos:
    - artifact.created
    - artifact.updated
    - artifact.approved
    - artifact.rejected
    - artifact.deprecated
  
  compliance:
    - compliance.violation
    - compliance.review_required
    - compliance.approved
  
  seguridad:
    - security.threat_detected
    - security.scan_completed
    - security.vulnerability_fixed
  
  sistema:
    - system.maintenance
    - system.update
    - system.error
```

### Subscription Management

```http
POST /api/v1/webhooks/subscribe
Content-Type: application/json
Authorization: Bearer <token>

{
  "nombre": "Notificaciones de Compliance",
  "callback_url": "https://myapp.banco.mx/webhooks/coe-ia",
  "eventos": [
    "artifact.approved",
    "compliance.violation",
    "security.threat_detected"
  ],
  "filtros": {
    "departamento": ["Riesgos", "Compliance"],
    "severidad_minima": "MEDIUM"
  },
  "configuracion": {
    "reintentos": 3,
    "timeout_segundos": 30,
    "incluir_payload_completo": true
  },
  "autenticacion": {
    "tipo": "HMAC_SHA256",
    "secret": "webhook_secret_key_here"
  }
}
```

**Response:**
```json
{
  "subscription_id": "sub_4k5l6m7n8o9p",
  "estado": "ACTIVE",
  "eventos_suscritos": 3,
  "callback_url": "https://myapp.banco.mx/webhooks/coe-ia",
  "proxima_verificacion": "2025-01-11T00:00:00Z",
  "webhook_test_url": "https://api.coe-ia.banco.mx/webhooks/test/sub_4k5l6m7n8o9p"
}
```

### Webhook Payload Example

```json
{
  "event_id": "evt_9q8r7s6t5u4v",
  "event_type": "artifact.approved",
  "timestamp": "2025-01-10T14:30:00Z",
  "subscription_id": "sub_4k5l6m7n8o9p",
  "data": {
    "artifact": {
      "id": "prmpt_7f8a9b2c3d4e5f6g",
      "tipo": "prompt",
      "nombre": "Asistente de Análisis Crediticio",
      "version": "2.1.0"
    },
    "aprobacion": {
      "aprobado_por": "risk_committee",
      "fecha": "2025-01-10T14:29:45Z",
      "comentarios": "Aprobado con recomendaciones menores"
    },
    "metadata": {
      "departamento": "Riesgos",
      "categoria": "credit-scoring",
      "nivel_riesgo": "MEDIUM"
    }
  },
  "signature": "sha256=7d4e3b2a1f9c8e7d6b5a4f3e2c1d0b9a8"
}
```

### WebSocket Real-time Events

```javascript
// Conexión WebSocket
const ws = new WebSocket('wss://events.coe-ia.banco.mx/v1/stream');

// Autenticación
ws.onopen = () => {
  ws.send(JSON.stringify({
    type: 'auth',
    token: 'your_jwt_token',
    subscribe_to: ['artifact.*', 'compliance.*']
  }));
};

// Recepción de eventos
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Evento recibido:', data);
  
  // Ejemplo de evento recibido
  // {
  //   "type": "artifact.updated",
  //   "timestamp": "2025-01-10T15:00:00Z",
  //   "data": {
  //     "artifact_id": "prmpt_7f8a9b2c3d4e5f6g",
  //     "changes": ["texto", "version"],
  //     "new_version": "2.2.0"
  //   }
  // }
};

// Manejo de errores
ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

// Reconexión automática
ws.onclose = () => {
  setTimeout(() => {
    console.log('Reconectando...');
    // Lógica de reconexión
  }, 5000);
};
```

## 📦 SDKs y Client Libraries

### Python SDK

```python
# Instalación
pip install coe-ia-sdk

# Uso básico
from coe_ia import Client
from coe_ia.models import PromptRequest, SearchQuery

# Inicializar cliente
client = Client(
    api_key="your_api_key",
    base_url="https://api.coe-ia.banco.mx",
    timeout=30
)

# Crear prompt
prompt = PromptRequest(
    titulo="Analizador de Riesgos",
    texto="Analiza el riesgo de transacciones...",
    categoria="risk-analysis",
    tags=["riesgo", "transacciones"]
)

response = client.prompts.create(prompt)
print(f"Prompt creado: {response.id}")

# Búsqueda semántica
query = SearchQuery(
    text="detectar fraude en pagos",
    limit=5,
    threshold=0.8
)

results = client.search.semantic(query)
for result in results:
    print(f"{result.titulo}: {result.score}")

# Métricas IMPACT
metrics = client.analytics.get_impact_metrics(
    period="monthly",
    year=2025,
    month=1
)
print(f"Score global: {metrics.score_global}")
```

### Java SDK

```java
// Maven dependency
<dependency>
    <groupId>mx.banco.coe</groupId>
    <artifactId>coe-ia-sdk</artifactId>
    <version>1.2.0</version>
</dependency>

// Uso
import mx.banco.coe.ia.Client;
import mx.banco.coe.ia.models.*;

public class Example {
    public static void main(String[] args) {
        // Inicializar cliente
        Client client = Client.builder()
            .apiKey("your_api_key")
            .baseUrl("https://api.coe-ia.banco.mx")
            .build();
        
        // Crear prompt
        PromptRequest prompt = PromptRequest.builder()
            .titulo("Asistente de Crédito")
            .texto("Evalúa solicitudes de crédito...")
            .categoria("credit")
            .build();
        
        PromptResponse response = client.prompts().create(prompt);
        System.out.println("Prompt ID: " + response.getId());
        
        // Generar código con Nova-Cell
        CodeGenerationRequest request = CodeGenerationRequest.builder()
            .requisitos("CRUD para gestión de cuentas")
            .lenguaje("Java")
            .framework("Spring Boot")
            .build();
        
        CodeGenerationResponse code = client.novaCell().generateCode(request);
        System.out.println("Archivos generados: " + code.getArchivosGenerados().size());
    }
}
```

### JavaScript/TypeScript SDK

```typescript
// Instalación
npm install @banco/coe-ia-sdk

// Uso con TypeScript
import { CoeIaClient, PromptRequest, ImpactMetrics } from '@banco/coe-ia-sdk';

// Inicializar cliente
const client = new CoeIaClient({
  apiKey: process.env.COE_IA_API_KEY,
  baseUrl: 'https://api.coe-ia.banco.mx'
});

// Función async para crear prompt
async function createPrompt() {
  const prompt: PromptRequest = {
    titulo: 'Asistente de Inversiones',
    texto: 'Ayuda a clientes con decisiones de inversión...',
    categoria: 'investment',
    tags: ['inversiones', 'asesoria']
  };
  
  try {
    const response = await client.prompts.create(prompt);
    console.log(`Prompt creado: ${response.id}`);
    
    // Obtener métricas
    const metrics: ImpactMetrics = await client.analytics.getImpactMetrics({
      period: 'monthly',
      year: 2025,
      month: 1
    });
    
    console.log(`Score IMPACT: ${metrics.scoreGlobal}`);
  } catch (error) {
    console.error('Error:', error);
  }
}

// WebSocket para eventos en tiempo real
const ws = client.events.connect();

ws.on('artifact.approved', (event) => {
  console.log('Artefacto aprobado:', event.data);
});

ws.on('error', (error) => {
  console.error('WebSocket error:', error);
});
```

### CLI Tool

```bash
# Instalación
npm install -g @banco/coe-ia-cli

# Configuración inicial
coe-ia configure
? API Key: your_api_key
? Environment: production

# Comandos disponibles
coe-ia --help

# Crear prompt
coe-ia prompt create \
  --title "Detector de Anomalías" \
  --category "fraud-detection" \
  --file prompt.txt

# Búsqueda semántica
coe-ia search \
  --query "análisis de riesgo crediticio" \
  --limit 10 \
  --threshold 0.75

# Generar código con Nova-Cell
coe-ia nova-cell generate \
  --requirements "API REST para gestión de clientes" \
  --language java \
  --framework spring-boot \
  --output ./generated

# Ver métricas IMPACT
coe-ia metrics impact --period monthly --format json

# Monitorear eventos en tiempo real
coe-ia events stream --filter "artifact.*" --follow
```

## 📚 Ejemplos y Tutoriales

### Caso de Uso 1: Workflow Completo de Prompt

```python
import asyncio
from coe_ia import AsyncClient
from coe_ia.models import *

async def complete_prompt_workflow():
    client = AsyncClient(api_key="your_api_key")
    
    # 1. Crear prompt
    prompt = await client.prompts.create(
        PromptRequest(
            titulo="Asesor Financiero Personal",
            texto="Analiza el perfil financiero del cliente...",
            categoria="advisory",
            compliance=ComplianceInfo(
                normativas=["CNBV", "CONDUSEF"],
                nivel_riesgo="MEDIUM"
            )
        )
    )
    print(f"✓ Prompt creado: {prompt.id}")
    
    # 2. Esperar aprobación (webhook simulado)
    await asyncio.sleep(2)
    
    # 3. Evaluar con AISIA
    evaluation = await client.governance.evaluate_aisia(
        AisiaRequest(
            artifact_id=prompt.id,
            datos_sensibles=True,
            impacto_usuarios=10000
        )
    )
    print(f"✓ Evaluación AISIA: Riesgo {evaluation.nivel_riesgo}")
    
    # 4. Generar tests
    tests = await client.nova_cell.generate_tests(
        TestGenerationRequest(
            artifact_id=prompt.id,
            coverage_objetivo=90,
            incluir_edge_cases=True
        )
    )
    print(f"✓ Tests generados: {len(tests.test_cases)} casos")
    
    # 5. Obtener métricas después de uso
    await asyncio.sleep(5)  # Simular uso
    
    metrics = await client.metrics.get_artifact_metrics(prompt.id)
    print(f"✓ Métricas: {metrics.total_usos} usos, {metrics.tasa_exito}% éxito")
    
    await client.close()

# Ejecutar
asyncio.run(complete_prompt_workflow())
```

### Caso de Uso 2: Pipeline de Seguridad

```javascript
// Pipeline completo de seguridad para código generado
const { CoeIaClient } = require('@banco/coe-ia-sdk');

async function securityPipeline(sourceCode) {
  const client = new CoeIaClient({
    apiKey: process.env.COE_IA_API_KEY
  });
  
  try {
    // 1. Escaneo de seguridad inicial
    console.log('🔍 Iniciando escaneo de seguridad...');
    const scanResult = await client.novaCell.securityScan({
      codigo_fuente: Buffer.from(sourceCode).toString('base64'),
      lenguaje: 'Java',
      estandares: ['OWASP-Top10', 'PCI-DSS']
    });
    
    console.log(`Vulnerabilidades encontradas: ${scanResult.resumen.total_issues}`);
    
    // 2. Si hay vulnerabilidades críticas, detener
    if (scanResult.resumen.criticos > 0) {
      throw new Error('Vulnerabilidades críticas detectadas');
    }
    
    // 3. Aplicar fixes automáticos para issues HIGH
    const fixes = [];
    for (const vuln of scanResult.vulnerabilidades) {
      if (vuln.severidad === 'HIGH' && vuln.remediacion.codigo_sugerido) {
        fixes.push({
          archivo: vuln.archivo,
          linea: vuln.linea,
          fix: vuln.remediacion.codigo_sugerido
        });
      }
    }
    
    console.log(`✅ ${fixes.length} fixes aplicados automáticamente`);
    
    // 4. Re-escanear después de fixes
    const rescan = await client.novaCell.securityScan({
      codigo_fuente: applyFixes(sourceCode, fixes),
      lenguaje: 'Java',
      estandares: ['OWASP-Top10', 'PCI-DSS']
    });
    
    // 5. Generar reporte de compliance
    const complianceReport = await client.governance.generateComplianceReport({
      scan_id: rescan.scan_id,
      incluir_remediaciones: true,
      formato: 'PDF'
    });
    
    console.log(`📊 Reporte de compliance generado: ${complianceReport.url}`);
    
    return {
      success: true,
      vulnerabilities_fixed: fixes.length,
      compliance_report: complianceReport.url,
      final_score: rescan.compliance_score
    };
    
  } catch (error) {
    console.error('❌ Error en pipeline de seguridad:', error.message);
    throw error;
  }
}

// Función auxiliar para aplicar fixes
function applyFixes(code, fixes) {
  // Implementación simplificada
  let fixedCode = code;
  for (const fix of fixes) {
    // Aplicar cada fix al código
    fixedCode = fixedCode.replace(fix.original, fix.fix);
  }
  return Buffer.from(fixedCode).toString('base64');
}
```

### Manejo de Errores

```python
from coe_ia import Client, CoeIaException
from coe_ia.errors import *
import time

def robust_api_call():
    client = Client(api_key="your_api_key")
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            # Intento de llamada API
            response = client.prompts.list(limit=100)
            return response
            
        except RateLimitException as e:
            # Error 429: Rate limit exceeded
            wait_time = e.retry_after or (retry_delay * (2 ** attempt))
            print(f"Rate limit alcanzado. Esperando {wait_time} segundos...")
            time.sleep(wait_time)
            
        except AuthenticationException as e:
            # Error 401: Token inválido o expirado
            print("Error de autenticación. Renovando token...")
            client.refresh_token()
            
        except ValidationException as e:
            # Error 400: Datos inválidos
            print(f"Error de validación: {e.errors}")
            # Corregir datos y reintentar
            break
            
        except NetworkException as e:
            # Error de red
            if attempt < max_retries - 1:
                print(f"Error de red. Reintentando en {retry_delay} segundos...")
                time.sleep(retry_delay)
            else:
                raise
                
        except CoeIaException as e:
            # Otros errores de la API
            print(f"Error de API: {e.code} - {e.message}")
            if e.is_retryable and attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise
    
    return None
```

## 🔐 Seguridad y Mejores Prácticas

### Headers de Seguridad

```http
# Request Headers Recomendados
X-Request-ID: uuid-v4
X-Client-Version: 1.2.0
X-Idempotency-Key: unique-key-for-request
Accept: application/json
Content-Type: application/json
User-Agent: coe-ia-sdk/1.2.0

# Response Headers de Seguridad
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'
```

### Validación de Webhooks

```python
import hmac
import hashlib

def validate_webhook_signature(payload, signature, secret):
    """
    Valida la firma HMAC del webhook
    """
    expected_signature = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    
    expected = f"sha256={expected_signature}"
    
    # Comparación segura contra timing attacks
    return hmac.compare_digest(expected, signature)

# Uso en endpoint webhook
@app.post("/webhook")
async def handle_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("X-Webhook-Signature")
    
    if not validate_webhook_signature(payload, signature, WEBHOOK_SECRET):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    # Procesar evento
    event = json.loads(payload)
    process_event(event)
```

## 📊 Códigos de Error

| Código | Tipo | Descripción | Acción Recomendada |
|--------|------|-------------|-------------------|
| **400** | `VALIDATION_ERROR` | Datos de entrada inválidos | Verificar formato y tipos de datos |
| **401** | `AUTHENTICATION_ERROR` | Token inválido o expirado | Renovar token de acceso |
| **403** | `AUTHORIZATION_ERROR` | Sin permisos para la operación | Verificar roles y permisos |
| **404** | `NOT_FOUND` | Recurso no encontrado | Verificar ID del recurso |
| **409** | `CONFLICT` | Conflicto con estado actual | Verificar estado del recurso |
| **429** | `RATE_LIMIT_ERROR` | Límite de requests excedido | Implementar backoff exponencial |
| **500** | `INTERNAL_ERROR` | Error interno del servidor | Reintentar con backoff |
| **503** | `SERVICE_UNAVAILABLE` | Servicio temporalmente no disponible | Reintentar más tarde |

## 🚀 Roadmap de APIs

### Q1 2025
- ✅ APIs Core (Knowledge Hub, Nova-Cell)
- ✅ Autenticación OAuth2/JWT
- ✅ SDKs Python, Java, JavaScript
- 🔄 GraphQL API (Beta)

### Q2 2025
- 📅 API Gateway v2 con rate limiting mejorado
- 📅 Soporte para batch operations
- 📅 Streaming APIs para procesamiento en tiempo real
- 📅 SDK para Go y .NET

### Q3 2025
- 📅 APIs de Machine Learning Operations
- 📅 Marketplace de modelos y artefactos
- 📅 APIs federadas multi-región

## 🆘 Soporte

### Recursos de Desarrollo

- **Portal de Desarrolladores**: [https://developers.coe-ia.banco.mx](https://developers.coe-ia.banco.mx)
- **API Status**: [https://status.coe-ia.banco.mx](https://status.coe-ia.banco.mx)
- **Postman Collection**: [Descargar](https://api.coe-ia.banco.mx/postman-collection.json)
- **OpenAPI Spec**: [https://api.coe-ia.banco.mx/openapi.yaml](https://api.coe-ia.banco.mx/openapi.yaml)

### Contacto

- **Email**: api-support@coe-ia.banco.mx
- **Slack**: #coe-ia-api-support
- **Teams**: Canal API CoE IA
- **Horario de Soporte**: Lun-Vie 9:00-18:00 CST

---

*API Documentation v1.2.0 | Centro de Excelencia de IA | Última actualización: 10 de enero de 2025*