# Dashboard de Métricas IMPACT - Centro de Excelencia de IA (Nova-Cell 2.0)

<style>
/* --- Corporate Color Palette & General Styles --- */
:root {
    --banco-primary-blue: #003366;
    --banco-secondary-green: #008060;
    --banco-accent-gray: #f0f2f5;
    --banco-text-dark: #1c1e21;
    --banco-text-light: #ffffff;
    --banco-border-color: #dce1e6;
    --trend-up-color: #008060;
    --trend-down-color: #d93025;
    --alert-critical-bg: #fbeae5;
    --alert-warning-bg: #fff8e1;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

/* --- Dashboard Layout --- */
.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 25px;
}

/* --- Card Component --- */
.card {
    background-color: var(--banco-text-light);
    border: 1px solid var(--banco-border-color);
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.card-title {
    font-size: 1.1em;
    font-weight: 600;
    color: var(--banco-primary-blue);
    margin-bottom: 15px;
}
.kpi-value {
    font-size: 2.5em;
    font-weight: 700;
    color: var(--banco-text-dark);
    margin-bottom: 10px;
}
.kpi-unit {
    font-size: 1.2em;
    font-weight: 500;
    color: #555;
    margin-left: 5px;
}
.kpi-context {
    font-size: 0.9em;
    color: #657786;
}
.trend {
    font-weight: 600;
    font-size: 0.95em;
}
.trend-up {
    color: var(--trend-up-color);
}
.trend-down {
    color: var(--trend-down-color);
}

/* --- Filters & Alerts --- */
.filters-container {
    display: flex;
    gap: 15px;
    align-items: center;
    background-color: var(--banco-accent-gray);
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 25px;
    flex-wrap: wrap;
}
.filter-label {
    font-weight: 600;
    color: var(--banco-text-dark);
}
.filter-button {
    background-color: white;
    border: 1px solid var(--banco-border-color);
    padding: 8px 12px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9em;
}
.filter-button:hover {
    background-color: #f7f7f7;
}
.alert-section {
    margin-bottom: 25px;
}
.alert {
    padding: 15px;
    border-radius: 6px;
    margin-bottom: 10px;
    border: 1px solid;
}
.alert-critical {
    background-color: var(--alert-critical-bg);
    border-color: var(--trend-down-color);
    color: #5d1b16;
}
.alert-warning {
    background-color: var(--alert-warning-bg);
    border-color: #ffc107;
    color: #664d03;
}

/* --- Tables --- */
table {
    width: 100%;
    border-collapse: collapse;
}
th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid var(--banco-border-color);
}
th {
    background-color: var(--banco-accent-gray);
    font-weight: 600;
    color: var(--banco-primary-blue);
}
tr:hover {
    background-color: #f9f9f9;
}
</style>

## Vista Ejecutiva: Resumen General de IMPACT

Este dashboard provee una visión 360° del rendimiento y valor del Centro de Excelencia de IA, basado en el framework IMPACT. Las métricas reflejan el estado actual de nuestros proyectos, plataformas y su alineación con los objetivos estratégicos del banco.

<div class="dashboard-grid">
    <div class="card">
        <div class="card-title">ROI Total de Proyectos IA</div>
        <div>
            <span class="kpi-value">315</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            <span class="trend trend-up">▲ 12%</span> vs. Trimestre Anterior
        </div>
    </div>
    <div class="card">
        <div class="card-title">Modelos en Producción</div>
        <div>
            <span class="kpi-value">82</span>
        </div>
        <div class="kpi-context">
            <span class="trend trend-up">▲ 5 nuevos</span> este mes
        </div>
    </div>
    <div class="card">
        <div class="card-title">Adopción por Unidades de Negocio</div>
        <div>
            <span class="kpi-value">75</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            12 de 16 unidades de negocio activas
        </div>
    </div>
    <div class="card">
        <div class="card-title">Nivel de Confianza (Trust Score)</div>
        <div>
            <span class="kpi-value">9.2</span><span class="kpi-unit">/ 10</span>
        </div>
        <div class="kpi-context">
            Promedio de auditorías de equidad y seguridad
        </div>
    </div>
</div>

---

### Controles y Filtros

<div class="filters-container">
    <span class="filter-label">Periodo:</span>
    <button class="filter-button">Últimos 30 días</button>
    <button class="filter-button">Este Trimestre</button>
    <button class="filter-button">Año Actual</button>
    <span class="filter-label" style="margin-left: 20px;">Unidad de Negocio:</span>
    <button class="filter-button">Todas</button>
    <button class="filter-button">Banca Minorista</button>
    <button class="filter-button">Banca Corporativa</button>
    <button class="filter-button">Riesgos</button>
</div>

### Alertas y Notificaciones

<div class="alert-section">
    <div class="alert alert-critical">
        <strong>CRÍTICO:</strong> El modelo de Detección de Fraude v2.1 (TDC) muestra una degradación en la precisión del 8% en las últimas 48 horas. Se requiere intervención inmediata.
    </div>
    <div class="alert alert-warning">
        <strong>ADVERTENCIA:</strong> El tiempo de inferencia para el modelo de Scoring de Crédito ha aumentado un 15% por encima del SLA. Investigar posible sobrecarga en la infraestructura.
    </div>
</div>

---

## I - Implementation (Implementación)
*Mide la velocidad y eficiencia con la que desplegamos soluciones de IA desde la ideación hasta la producción.*

<div class="dashboard-grid">
    <div class="card">
        <div class="card-title">Tiempo Promedio de Despliegue</div>
        <div>
            <span class="kpi-value">52</span><span class="kpi-unit">días</span>
        </div>
        <div class="kpi-context">
            <span class="trend trend-up">▼ 8%</span> más rápido que el H1
        </div>
    </div>
    <div class="card">
        <div class="card-title">Proyectos en Pipeline</div>
        <div>
            <span class="kpi-value">25</span>
        </div>
        <div class="kpi-context">
            8 en desarrollo, 12 en validación, 5 en ideación
        </div>
    </div>
    <div class="card">
        <div class="card-title">Tasa de Éxito de Despliegue</div>
        <div>
            <span class="kpi-value">98</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            Despliegues sin necesidad de rollback
        </div>
    </div>
</div>

### Pipeline de Proyectos IA
```mermaid
graph LR
    A[Ideación: 5] --> B[Desarrollo: 8]
    B --> C[Validación: 12]
    C --> D[Producción: 82]
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ff9,stroke:#333,stroke-width:2px
    style C fill:#9f9,stroke:#333,stroke-width:2px
    style D fill:#99f,stroke:#333,stroke-width:2px
```

---

## M - Momentum (Impulso)
*Evalúa la adopción, crecimiento y escalabilidad de la plataforma Nova-Cell 2.0 y sus soluciones.*

<div class="dashboard-grid">
    <div class="card">
        <div class="card-title">Llamadas a API / día (promedio)</div>
        <div>
            <span class="kpi-value">1.2M</span>
        </div>
        <div class="kpi-context">
            <span class="trend trend-up">▲ 25%</span> Crecimiento MoM
        </div>
    </div>
    <div class="card">
        <div class="card-title">Usuarios Activos en Plataforma</div>
        <div>
            <span class="kpi-value">450+</span>
        </div>
        <div class="kpi-context">
            Data Scientists, Analistas, Jefes de Producto
        </div>
    </div>
    <div class="card">
        <div class="card-title">Nuevos Casos de Uso Iniciados</div>
        <div>
            <span class="kpi-value">8</span>
        </div>
        <div class="kpi-context">
            Este trimestre
        </div>
    </div>
</div>

### Tendencia de Adopción (Últimos 6 Meses)
```mermaid
xychart-beta
    title "Crecimiento de Usuarios Activos Nova-Cell 2.0"
    x-axis "Mes" ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
    y-axis "Usuarios Activos"
    bar "Usuarios Nuevos" [45, 52, 68, 75, 82, 95]
    line "Usuarios Totales" [250, 302, 370, 445, 527, 622]
```

---

## P - Performance (Rendimiento)
*Monitorea la calidad técnica, precisión y eficiencia operativa de los modelos en producción.*

<div class="dashboard-grid">
    <div class="card">
        <div class="card-title">Precisión Ponderada de Modelos</div>
        <div>
            <span class="kpi-value">94.6</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            Promedio de todos los modelos críticos
        </div>
    </div>
    <div class="card">
        <div class="card-title">Latencia de Inferencia (p95)</div>
        <div>
            <span class="kpi-value">120</span><span class="kpi-unit">ms</span>
        </div>
        <div class="kpi-context">
            <span class="trend trend-up">Dentro del SLA de 200ms</span>
        </div>
    </div>
    <div class="card">
        <div class="card-title">Uptime de la Plataforma</div>
        <div>
            <span class="kpi-value">99.98</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            Últimos 90 días
        </div>
    </div>
</div>

### Detección de Deriva de Modelos (Model Drift)
```mermaid
xychart-beta
  title "Modelos Críticos con Deriva Detectada (Últimos 6 Meses)"
  x-axis "Mes" ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
  y-axis "Nº de Modelos"
  bar "Modelos con Deriva" [2, 1, 3, 2, 5, 4]
  line "Umbral de Alerta" [4, 4, 4, 4, 4, 4]
```

---

## A - Acceptance (Aceptación)
*Mide cómo las unidades de negocio adoptan, utilizan y perciben el valor de las soluciones de IA.*

<div class="dashboard-grid">
    <div class="card">
        <div class="card-title">NPS de Unidades de Negocio</div>
        <div>
            <span class="kpi-value">+45</span>
        </div>
        <div class="kpi-context">
            <span class="trend trend-up">▲ 8 puntos</span> vs. encuesta anterior
        </div>
    </div>
    <div class="card">
        <div class="card-title">Tasa de Adopción de Features</div>
        <div>
            <span class="kpi-value">68</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            Features clave usadas activamente por usuarios target
        </div>
    </div>
    <div class="card">
        <div class="card-title">Satisfacción del Usuario</div>
        <div>
            <span class="kpi-value">4.3</span><span class="kpi-unit">/ 5</span>
        </div>
        <div class="kpi-context">
            Promedio de evaluaciones post-implementación
        </div>
    </div>
</div>

### Distribución de Proyectos por Unidad de Negocio
```mermaid
pie title Proyectos de IA Activos por Unidad de Negocio
    "Banca Minorista" : 40
    "Riesgos" : 25
    "Banca Corporativa" : 15
    "Operaciones" : 12
    "Marketing" : 8
```

---

## C - Cost-Effective (Costo-Efectividad)
*Cuantifica el impacto financiero, incluyendo ahorros, ingresos generados y eficiencia operacional.*

<div class="dashboard-grid">
    <div class="card">
        <div class="card-title">Ahorro por Detección de Fraude</div>
        <div>
            <span class="kpi-value">$8.2M</span><span class="kpi-unit">MXN</span>
        </div>
        <div class="kpi-context">
            Acumulado en el año fiscal
        </div>
    </div>
    <div class="card">
        <div class="card-title">Horas-Hombre Ahorradas</div>
        <div>
            <span class="kpi-value">15,000+</span>
        </div>
        <div class="kpi-context">
            Por automatización de procesos (anualizado)
        </div>
    </div>
    <div class="card">
        <div class="card-title">Costo por Inferencia</div>
        <div>
            <span class="kpi-value">$0.0012</span><span class="kpi-unit">MXN</span>
        </div>
        <div class="kpi-context">
            <span class="trend trend-up">▼ 5%</span> optimización de infraestructura
        </div>
    </div>
</div>

### Detalle de Impacto Financiero (Q2)

| Iniciativa de IA | Unidad de Negocio | Ahorro / Ingreso Generado (MXN) | ROI de la Iniciativa |
|------------------|-------------------|----------------------------------|----------------------|
| Scoring Alternativo de Crédito | Banca Minorista | $12.5M (Ingreso) | **450%** |
| Optimización de Campañas | Marketing | $4.8M (Ingreso) | **320%** |
| Clasificación de Documentos | Operaciones | $3.1M (Ahorro) | **280%** |
| Prevención de Fuga de Clientes | Banca Corporativa | $7.9M (Retención) | **410%** |
| Detección de Anomalías | Riesgos | $5.3M (Prevención) | **380%** |
| Chatbot de Servicio | Contact Center | $2.8M (Ahorro) | **290%** |

---

## T - Trust (Confianza)
*Asegura que nuestras soluciones de IA son seguras, éticas, justas, transparentes y cumplen con la regulación.*

<div class="dashboard-grid">
    <div class="card">
        <div class="card-title">Auditorías de Sesgo (Bias) Pasadas</div>
        <div>
            <span class="kpi-value">100</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            De modelos en producción
        </div>
    </div>
    <div class="card">
        <div class="card-title">Cobertura de Explicabilidad (XAI)</div>
        <div>
            <span class="kpi-value">85</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            De modelos de decisión crítica con reportes SHAP/LIME
        </div>
    </div>
    <div class="card">
        <div class="card-title">Cumplimiento Regulatorio (CNBV)</div>
        <div>
            <span class="kpi-value">100</span><span class="kpi-unit">%</span>
        </div>
        <div class="kpi-context">
            Cero incidentes reportados en auditorías
        </div>
    </div>
</div>

### Matriz de Cumplimiento Regulatorio

| Regulación | Estado | Última Auditoría | Próxima Revisión |
|------------|--------|------------------|------------------|
| **CNBV - Disposiciones CUB** | ✅ Cumple | 15-May-2024 | 15-Nov-2024 |
| **ISO/IEC 42001:2023** | ✅ Cumple | 30-Jun-2024 | 30-Dec-2024 |
| **LFPDPPP** | ✅ Cumple | 20-Apr-2024 | 20-Oct-2024 |
| **EU AI Act (preparación)** | 🔄 En proceso | N/A | Mar-2025 |

---

## Configuración y Acceso

### Perfiles de Usuario

- **Ejecutivos**: Vista resumida con KPIs principales y tendencias
- **Gerentes de Unidad**: Métricas específicas de su área + benchmarks
- **Data Scientists**: Performance técnico detallado + drift monitoring
- **Risk Officers**: Compliance, auditorías y métricas de confianza

### Actualización de Datos

- **Tiempo Real**: Métricas de performance y disponibilidad
- **Diario**: Métricas de adopción y uso
- **Semanal**: Métricas financieras y de impacto
- **Mensual**: NPS, satisfacción y auditorías

### Exportación y Reportes

Todos los datos pueden exportarse en formatos:
- PDF para reportes ejecutivos
- Excel para análisis detallado
- API REST para integración con otros sistemas

---

*Dashboard generado el 09 de Enero de 2025 | Versión 2.0 | Centro de Excelencia de IA*