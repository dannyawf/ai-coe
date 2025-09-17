---
tags:
  - gobernanza
  - política
  - ética
  - cumplimiento
  - ISO-42001
  - CNBV
  - regulación
search:
  boost: 2
---

# Política de Uso Responsable de Inteligencia Artificial

<div class="nova-card-hero nova-scale-in">
  <h2 style="margin: 0; font-size: 1.8rem;">🏛️ Política Corporativa de IA</h2>
  <p style="margin: 0.5rem 0 0; opacity: 0.9;">Marco de governance para uso responsable y ético de Inteligencia Artificial</p>
</div>

<div class="nova-grid nova-grid--2" style="margin: 2rem 0;">
  <div class="nova-card-metric">
    <strong>📋 Versión:</strong> 1.0 <span class="nova-badge nova-badge--primary">Vigente</span>
  </div>
  <div class="nova-card-metric">
    <strong>📅 Fecha:</strong> 09 de septiembre de 2025
  </div>
  <div class="nova-card-metric">
    <strong>👤 Autor:</strong> Centro de Excelencia de IA (CoE IA)
  </div>
  <div class="nova-card-metric">
    <strong>✅ Aprobado por:</strong> Consejo de Dirección
  </div>
  <div class="nova-card-metric">
    <strong>🔄 Próxima revisión:</strong> 09 de marzo de 2026
  </div>
  <div class="nova-card-metric">
    <strong>🔒 Clasificación:</strong> <span class="nova-badge nova-badge--warning">INTERNO</span>
  </div>
</div>

## 1. Objetivo

Establecer los lineamientos, controles y principios éticos que rigen el uso responsable de sistemas de Inteligencia Artificial en el Banco, garantizando el cumplimiento regulatorio, la gestión eficaz de riesgos y la creación de valor de forma sostenible y ética.

Esta política asegura que toda implementación de IA se alinee con nuestra cultura organizacional, cumpla con los estándares ISO/IEC 42001, ISO/IEC 23053, ISO/IEC 23894 y la regulación mexicana bancaria (CNBV, Banxico, LFPDPPP).

## 2. Alcance

### Aplica a:
- Todos los colaboradores del Banco sin excepción
- Proveedores y terceros que desarrollen o implementen sistemas de IA
- Todos los sistemas, aplicaciones y procesos que utilicen IA
- Datos utilizados para entrenar, validar o ejecutar modelos de IA
- Plataforma Nova-Cell como herramienta corporativa aprobada
- Procesos de desarrollo aumentado con IA

### No aplica a:
- Sistemas de automatización tradicionales sin componentes de machine learning
- Herramientas estadísticas convencionales sin capacidades de aprendizaje
- Calculadoras financieras básicas sin algoritmos adaptativos

## 3. Definiciones

- **Inteligencia Artificial (IA)**: Sistema tecnológico que puede, para un conjunto dado de objetivos definidos por humanos, realizar predicciones, recomendaciones o decisiones que influyen en entornos reales o virtuales.
- **Sistema de IA de Alto Riesgo**: Aquellos que impactan decisiones crediticias, detección de fraude, cumplimiento regulatorio o atención automatizada al cliente.
- **Nova-Cell**: Plataforma corporativa aprobada para desarrollo aumentado con IA, que proporciona governance, seguridad y trazabilidad completa.
- **Shadow AI**: Uso no autorizado de herramientas de IA externas (ChatGPT, Claude, Gemini) fuera del marco de governance corporativo.
- **AISIA (AI System Impact Assessment)**: Evaluación obligatoria del impacto de sistemas de IA antes de su implementación en producción.
- **Framework IMPACT**: Sistema de métricas corporativo que evalúa Implementation, Momentum, Performance, Acceptance, Cost-Effective y Trust.

## 4. Principios Rectores

1. **Transparencia y Explicabilidad**: Todo sistema de IA debe ser auditable y sus decisiones explicables a reguladores, clientes y colaboradores.

2. **Supervisión Humana Obligatoria**: Ningún sistema de IA puede operar sin supervisión humana calificada y capacidad de intervención.

3. **Seguridad y Privacidad por Diseño**: Protección integral de datos personales y cumplimiento de LFPDPPP desde la concepción del sistema.

4. **Equidad y No Discriminación**: Prevención activa de sesgos algorítmicos que puedan resultar en discriminación hacia clientes o colaboradores.

5. **Confiabilidad y Robustez**: Sistemas probados exhaustivamente con planes de contingencia para escenarios adversos.

6. **Cumplimiento Regulatorio Integral**: Adherencia a CNBV, Banxico, INAI y estándares internacionales ISO 42001.

## 5. Política

### 5.1 Usos Permitidos de IA

#### Desarrollo Aumentado (Nova-Cell):
- [ ] Aceleración de desarrollo de software con supervisión humana
- [ ] Generación de código con revisión obligatoria
- [ ] Automatización de testing y documentación técnica
- [ ] Refactorización de sistemas legacy

#### Procesos de Negocio Críticos:
- [ ] Scoring crediticio con explicabilidad garantizada
- [ ] Detección de fraude y lavado de dinero (AML)
- [ ] Análisis de riesgo de mercado y operativo
- [ ] Personalización de productos bancarios

#### Operaciones y Eficiencia:
- [ ] Automatización de procesos repetitivos
- [ ] Análisis predictivo para mantenimiento
- [ ] Optimización de recursos y costos
- [ ] Mejora de experiencia del cliente

#### Prohibiciones Absolutas:
- ❌ Uso de Shadow AI (ChatGPT, Claude, Gemini fuera de Nova-Cell)
- ❌ Procesamiento de datos personales sin consentimiento
- ❌ Sistemas de IA sin supervisión humana en decisiones críticas
- ❌ Modelos sin documentación técnica completa
- ❌ Implementación sin evaluación AISIA previa
- ❌ Uso de datos para entrenamiento de modelos externos
- ❌ Algoritmos que no permitan auditoría de decisiones

### 5.2 Gestión de Riesgos de IA

#### Riesgos Críticos Identificados:
1. **Sesgo Algorítmico**: Discriminación en decisiones crediticias o de servicio
2. **Degradación de Modelos**: Pérdida de precisión por cambios en datos (model drift)
3. **Ataques Adversarios**: Manipulación maliciosa de modelos
4. **Privacidad de Datos**: Re-identificación o filtración de información personal
5. **Dependencia Tecnológica**: Concentración en proveedores específicos
6. **Riesgo Operativo**: Fallas sistémicas en procesos automatizados

#### Controles Obligatorios:
- [ ] Evaluación AISIA para todos los sistemas de alto riesgo
- [ ] Monitoreo continuo de métricas de desempeño y sesgo
- [ ] Planes de contingencia y rollback para cada sistema
- [ ] Auditorías internas trimestrales de modelos en producción
- [ ] Documentación técnica actualizada permanentemente

### 5.3 Validación y Testing de Modelos

#### Requisitos Mínimos Pre-Producción:
- [ ] Validación cruzada con datos históricos (mínimo 2 años)
- [ ] Análisis de sesgo por demografías relevantes
- [ ] Pruebas de robustez ante escenarios adversos
- [ ] Validación por segunda línea de defensa (Risk Management)
- [ ] Aprobación del Comité de IA para sistemas críticos

#### Testing Continuo en Producción:
- [ ] Monitoreo diario de métricas clave de desempeño
- [ ] Alertas automáticas por degradación de modelo
- [ ] Comparación A/B contra métodos tradicionales
- [ ] Revisión mensual de decisiones rechazadas o apeladas

### 5.4 Protección de Datos y Privacidad

#### Cumplimiento LFPDPPP:
- [ ] Aviso de privacidad específico para uso de IA
- [ ] Consentimiento explícito para tratamiento automatizado
- [ ] Derecho de explicación para decisiones automatizadas
- [ ] Portabilidad de datos y derecho al olvido

#### Seguridad Técnica:
- [ ] Encriptación end-to-end de datos de entrenamiento
- [ ] Segregación de ambientes (desarrollo/testing/producción)
- [ ] Logs completos de acceso y modificaciones
- [ ] Residencia de datos en territorio mexicano (AWS Querétaro)

### 5.5 Supervisión Humana y Escalamiento

#### Niveles de Supervisión Requerida:
1. **Nivel 1 - Automatización Total**: Procesos de bajo riesgo con revisión periódica
2. **Nivel 2 - Supervisión Activa**: Decisiones revisadas antes de ejecución
3. **Nivel 3 - Aprobación Humana**: Decisión final siempre humana
4. **Nivel 4 - Asistencia IA**: Humano decide con recomendaciones de IA

#### Proceso de Escalamiento:
- Alertas inmediatas por comportamiento anómalo del modelo
- Escalamiento automático a Risk Officer ante métricas críticas
- Procedimiento de parada de emergencia (kill switch) disponible 24/7
- Notificación a reguladores según sea requerido

## 6. Roles y Responsabilidades

| Rol | Responsabilidad | Frecuencia |
|-----|-----------------|------------|
| **CEO/Consejo** | Aprobar estrategia IA y políticas corporativas | Trimestral |
| **Chief AI Officer** | Supervisión estratégica del programa de IA | Semanal |
| **Comité de IA** | Aprobación de casos de uso y supervisión de gobierno | Mensual |
| **Centro de Excelencia IA** | Desarrollo de capacidades y estándares técnicos | Diario |
| **Risk Officers IA** | Validación de modelos y gestión de riesgos | Diario |
| **Product Owners** | Implementación responsable en sus áreas | Diario |
| **Data Scientists** | Desarrollo técnico con ética y transparencia | Diario |
| **Compliance Officer** | Verificación de cumplimiento regulatorio | Semanal |
| **Auditoría Interna** | Validación independiente de controles | Trimestral |

### Responsabilidades Específicas por Línea de Defensa:

#### Primera Línea (Unidades de Negocio):
- Implementar casos de uso alineados a esta política
- Documentar y mantener actualizado el inventario de modelos
- Reportar incidentes o degradación de desempeño
- Capacitar a usuarios finales en uso responsable

#### Segunda Línea (Gestión de Riesgos):
- Validar independientemente todos los modelos críticos
- Monitorear métricas IMPACT y alertar desviaciones
- Mantener el registro de riesgos de IA actualizado
- Reportar al regulador según corresponda

#### Tercera Línea (Auditoría Interna):
- Auditar cumplimiento de esta política anualmente
- Validar efectividad de controles implementados
- Certificar procesos para estándar ISO 42001
- Evaluar independientemente la cultura de IA responsable

## 7. Proceso de Aprobación de Casos de Uso

### 7.1 Clasificación por Nivel de Riesgo

#### Alto Riesgo (Requiere aprobación del Comité de IA):
- Decisiones crediticias automatizadas
- Sistemas de detección de fraude y AML
- Procesos de KYC automatizados
- Trading algorítmico
- Atención al cliente con toma de decisiones

#### Medio Riesgo (Requiere aprobación del CoE IA):
- Análisis de datos para insights de negocio
- Automatización de procesos internos
- Herramientas de desarrollo (Nova-Cell)
- Sistemas de recomendación no críticos

#### Bajo Riesgo (Aprobación automática con registro):
- Herramientas de productividad personal
- Análisis descriptivo de datos anonimizados
- Mejoras de interfaz de usuario

### 7.2 Documentación Requerida

#### Para Todos los Casos de Uso:
1. Business case con ROI esperado
2. Evaluación AISIA completa
3. Plan de implementación por fases
4. Análisis de riesgos y mitigaciones
5. Plan de testing y validación
6. Estrategia de monitoreo continuo
7. Plan de contingencia y rollback

#### Para Sistemas de Alto Riesgo (Adicional):
8. Análisis independiente de sesgo
9. Pruebas de estrés y escenarios adversos
10. Plan de explicabilidad para reguladores
11. Evaluación de impacto en clientes
12. Dictamen legal de cumplimiento regulatorio

### 7.3 Proceso de Revisión

1. **Solicitud Formal** (Product Owner)
   - Llenar formulario de solicitud completo
   - Adjuntar documentación requerida
   - Obtener endorsement de línea directiva

2. **Evaluación Técnica** (CoE IA - 5 días hábiles)
   - Revisión de arquitectura y diseño
   - Validación de cumplimiento técnico
   - Análisis de viabilidad y riesgos

3. **Evaluación de Riesgos** (Risk Management - 5 días hábiles)
   - Análisis independiente de riesgos
   - Validación de controles propuestos
   - Recomendaciones de mitigación

4. **Evaluación Regulatoria** (Compliance - 3 días hábiles)
   - Verificación de cumplimiento normativo
   - Análisis de impacto regulatorio
   - Aprobación legal preliminar

5. **Decisión Final** (Comité IA o CoE según riesgo)
   - Aprobación, rechazo o aprobación condicionada
   - Definición de métricas de seguimiento
   - Establecimiento de fecha de revisión

## 8. Monitoreo y Auditoría

### 8.1 Métricas IMPACT (Automatizadas)

#### Implementation (Implementación):
- Tasa de adopción por área de negocio
- Usuarios activos diarios/mensuales
- Time to First Value (<15 minutos objetivo)
- Cobertura de Definition of Done (DoD)

#### Momentum (Impulso):
- Tendencia de crecimiento semanal
- Retención de usuarios (>70% objetivo)
- Viralidad interna y casos de uso emergentes
- Profundidad de uso por usuario

#### Performance (Desempeño):
- Mejora en velocidad de procesos (2.2x-2.5x objetivo)
- Reducción en cycle time de desarrollo
- Aumento en throughput operativo
- Mejora en flow efficiency (+20% objetivo)

#### Acceptance (Aceptación):
- Tasa de aceptación de recomendaciones IA (25-40% zona óptima)
- Calidad del output generado
- Reducción en densidad de bugs (-40% objetivo)
- Review pass rate en procesos automatizados

#### Cost-Effective (Costo-Beneficio):
- ROI mensual acumulado (break-even semana 11)
- Costo por hora de trabajo ahorrada
- Valor económico generado (150% ROI año 1)
- Reducción en costos operativos

#### Trust (Confianza):
- Developer/User NPS (+20 puntos objetivo)
- Confidence score en decisiones automatizadas
- Developer Experience Index (DX)
- Reducción en carga cognitiva reportada

### 8.2 KPIs Regulatorios

#### Cobertura y Documentación:
- **Coverage Rate**: 100% de modelos en inventario corporativo
- **Documentation Score**: Completitud de documentación técnica (>95%)
- **Compliance Rate**: % de modelos que cumplen todos los controles

#### Gestión de Incidentes:
- **Incident Rate**: Incidentes relacionados con IA por mes (<2 objetivo)
- **Remediation Time**: Tiempo promedio de resolución (<24 horas críticos)
- **Audit Findings**: Número de hallazgos por auditoría (<5 objetivo)

#### Explicabilidad y Transparencia:
- **Explainability Score**: % de decisiones explicables bajo demanda
- **Appeal Success Rate**: % de apelaciones exitosas de decisiones IA
- **Regulator Response Time**: Tiempo de respuesta a requerimientos (≤5 días)

### 8.3 Programa de Auditorías

#### Auditoría Interna (Trimestral):
- Revisión de cumplimiento de políticas
- Validación de controles técnicos
- Evaluación de cultura de IA responsable
- Testing de procedimientos de escalamiento

#### Auditoría Externa (Anual):
- Certificación ISO 42001 por tercero independiente
- Validación de modelo de gobierno
- Benchmarking contra mejores prácticas
- Preparación para supervisión regulatoria

#### Auditoría de Modelos (Mensual para críticos, Trimestral para otros):
- Performance vs métricas definidas
- Análisis de drift en datos y predicciones
- Revisión de logs de decisiones
- Validación de explicabilidad

### 8.4 Reportería Ejecutiva

#### Dashboard en Tiempo Real:
- Métricas IMPACT consolidadas
- Alertas de riesgos críticos
- Estado de cumplimiento regulatorio
- ROI acumulado por caso de uso

#### Reporte Mensual al Comité de IA:
- Resumen ejecutivo de métricas
- Casos de uso nuevos y actualizaciones
- Incidentes y acciones correctivas
- Proyección de ROI trimestral

#### Reporte Trimestral al Consejo:
- Evolución de la estrategia de IA
- Impacto en objetivos de negocio
- Estado de cumplimiento regulatorio
- Inversiones y ROI consolidado

## 9. Gestión de Excepciones

### 9.1 Proceso de Excepción

#### Cuándo Aplica:
- Urgencia operativa crítica que requiere implementación acelerada
- Limitaciones técnicas temporales que impiden cumplimiento total
- Requerimientos regulatorios emergentes no contemplados

#### NO Aplican Excepciones Para:
- ❌ Uso de Shadow AI en sistemas críticos
- ❌ Procesamiento de datos personales sin consentimiento
- ❌ Sistemas sin supervisión humana en decisiones de alto impacto
- ❌ Modelos que discriminen por características protegidas

### 9.2 Procedimiento de Aprobación

1. **Solicitud Formal** (Product Owner/Risk Officer)
   - Justificación detallada de la necesidad
   - Análisis de riesgos específicos
   - Plan de mitigación temporal
   - Cronograma para cumplimiento completo

2. **Evaluación de Riesgos** (Segunda Línea - 2 días hábiles)
   - Validación de justificación
   - Análisis de impacto potencial
   - Recomendación de controles compensatorios

3. **Aprobación** (Chief AI Officer o Comité según criticidad)
   - Aprobación excepcional por tiempo limitado
   - Definición de controles compensatorios obligatorios
   - Establecimiento de fecha límite para regularización

4. **Documentación** (CoE IA)
   - Registro en sistema de gestión de excepciones
   - Notificación a stakeholders relevantes
   - Programación de seguimiento y cierre

### 9.3 Seguimiento de Excepciones

#### Monitoreo Intensivo:
- Revisión semanal de excepciones activas
- Alertas automáticas por vencimiento
- Reporte mensual al Comité de IA
- Escalamiento por incumplimiento de fechas límite

#### Vigencia Máxima:
- **Excepciones críticas**: 30 días calendario
- **Excepciones no críticas**: 90 días calendario
- **Sin renovación automática**: Requiere nueva justificación completa

## 10. Capacitación y Certificación

### 10.1 Programa Obligatorio por Rol

#### Todos los Colaboradores (Tier 1 - 4 horas anuales):
- Principios de IA responsable
- Identificación y reporte de Shadow AI
- Derechos de clientes en decisiones automatizadas
- Canal de escalamiento de incidentes

#### Product Owners y Gestores (Tier 2 - 16 horas anuales):
- Evaluación AISIA paso a paso
- Gestión de riesgos de IA
- Interpretación de métricas IMPACT
- Proceso de aprobación de casos de uso

#### Desarrolladores y Data Scientists (Tier 3 - 32 horas anuales):
- Desarrollo ético de IA
- Técnicas de mitigación de sesgo
- Explicabilidad e interpretabilidad
- Testing de robustez y seguridad

#### Líderes y Risk Officers (Tier 4 - 40 horas anuales):
- Gobernanza avanzada de IA
- Cumplimiento regulatorio internacional
- Gestión de crisis en sistemas de IA
- Estrategia de IA empresarial

### 10.2 Certificación Interna

#### Requisitos para Certificación:
- Completar capacitación de tier correspondiente
- Aprobar examen teórico (>80%)
- Demostrar aplicación práctica en proyecto real
- Evaluación de pares o supervisor directo

#### Vigencia y Renovación:
- **Vigencia**: 2 años para certificación inicial
- **Renovación**: 12 meses con capacitación de actualización
- **Recertificación obligatoria**: Ante cambios regulatorios mayores

### 10.3 Red de AI Champions

#### Selección de Champions:
- Nominación por líderes de área
- Demostración de competencias técnicas y de liderazgo
- Compromiso de dedicar 10% tiempo a evangelización
- Certificación Tier 4 completada

#### Responsabilidades:
- Capacitación peer-to-peer en su área
- Identificación de nuevos casos de uso
- Soporte local para implementación de políticas
- Feedback al CoE sobre necesidades de capacitación

## 11. Sanciones por Incumplimiento

### 11.1 Clasificación de Faltas

#### Faltas Leves:
- Uso inadvertido de herramientas IA no aprobadas sin datos sensibles
- Demora en reportar incidentes menores
- Documentación incompleta en modelos de bajo riesgo
- **Sanción**: Capacitación adicional + seguimiento mensual

#### Faltas Graves:
- Uso deliberado de Shadow AI con datos corporativos
- Implementación de sistemas sin aprobación requerida
- Omisión de controles de sesgo en sistemas críticos
- Falsificación de métricas de desempeño
- **Sanción**: Sanción disciplinaria + suspensión de privilegios IA + re-certificación obligatoria

#### Faltas Muy Graves:
- Filtración de datos por uso inadecuado de IA
- Implementación de sistemas discriminatorios
- Desactivación deliberada de controles de seguridad
- Ocultación de incidentes a reguladores
- **Sanción**: Proceso disciplinario mayor + posible terminación + reporte a autoridades

### 11.2 Proceso Disciplinario

#### Investigación:
1. Reporte de incidente
2. Suspensión precautoria de accesos si aplica
3. Investigación por Auditoría Interna + RRHH
4. Determinación de responsabilidades
5. Aplicación de sanción correspondiente

#### Derecho de Defensa:
- Notificación formal de cargos
- Derecho a presentar descargos
- Acompañamiento sindical si aplica
- Recurso de apelación ante Consejo Disciplinario

### 11.3 Sanciones Organizacionales

#### Para Áreas/Departamentos:
- **Primera instancia**: Plan de mejora obligatorio + auditoría adicional
- **Reincidencia**: Suspensión temporal de nuevos proyectos IA
- **Incumplimiento sistemático**: Intervención directa del CoE + cambio de liderazgo

#### Para Terceros/Proveedores:
- **Primera instancia**: Plan de acción correctivo + penalidades contractuales
- **Reincidencia**: Suspensión temporal de servicios
- **Falta grave**: Rescisión de contrato + inclusión en lista negra

## 12. Gestión del Cambio y Migración de Shadow AI

### 12.1 Estrategia de Migración

#### Identificación Proactiva:
- Auditoría de herramientas instaladas en dispositivos corporativos
- Monitoreo de tráfico de red hacia servicios de IA externos
- Encuestas anónimas de uso actual de IA
- Incentivos para auto-reporte voluntario

#### Migración Sin Penalizaciones (Período de Gracia: 90 días):
- Amnistía completa para reporte voluntario de Shadow AI
- Soporte prioritario para migración a Nova-Cell
- Capacitación acelerada en herramientas aprobadas
- Reconocimiento por adopción temprana de políticas

### 12.2 Plan de Comunicación

#### Mensajería Clave:
- "IA para potenciar tu trabajo, no para reemplazarte"
- "Nova-Cell: la herramienta segura y potente que necesitas"
- "Cumplimiento regulatorio = protección para todos"
- "Tus datos e ideas están seguros con nosotros"

#### Canales de Comunicación:
- Townhalls trimestrales con CEO
- Newsletter semanal del CoE IA
- Workshops prácticos por área de negocio
- Casos de éxito internos publicados
- Champions locales como embajadores

### 12.3 Medición del Cambio Cultural

#### Indicadores Tempranos (0-6 meses):
- Reducción de tráfico a herramientas no aprobadas
- Incremento en adoption rate de Nova-Cell
- Aumento en preguntas/consultas sobre IA responsable
- Participación en capacitaciones voluntarias

#### Indicadores de Progreso (6-18 meses):
- NPS de herramientas corporativas vs externas
- % de áreas con al menos un caso de uso activo
- Tiempo de aprobación de nuevos casos de uso
- Incidentes de Shadow AI reportados vs detectados

#### Indicadores de Madurez (18+ meses):
- IA integrada en procesos core de negocio
- Innovación espontánea en casos de uso
- Cero incidentes de Shadow AI crítico
- IA como ventaja competitiva reconocida

## 13. Referencias Regulatorias y Técnicas

### 13.1 Marco Regulatorio Internacional
- **ISO/IEC 42001:2023** - Sistema de Gestión de IA (AIMS)
- **ISO/IEC 23053** - Framework de IA basado en Machine Learning
- **ISO/IEC 23894** - Gestión de Riesgos en IA
- **ISO/IEC 27001** - Gestión de Seguridad de la Información
- **EU AI Act** - Regulación Europea de IA (referencia futura)
- **NIST AI Risk Management Framework** - Framework de gestión de riesgos

### 13.2 Marco Regulatorio Nacional
- **CNBV Circular 4/2020** - Gestión de riesgos tecnológicos
- **Banxico Circular 2/2019** - Disposiciones para instituciones fintech
- **LFPDPPP** - Ley Federal de Protección de Datos Personales en Posesión de Particulares
- **Ley Fintech** - Marco regulatorio para tecnología financiera
- **Lineamientos INAI** - Protección de datos en tratamientos automatizados

### 13.3 Políticas Corporativas Relacionadas
- Política de Gestión de Riesgos Operacionales
- Política de Protección de Datos Personales
- Política de Seguridad de la Información
- Política de Gestión de Terceros
- Código de Ética Corporativo

## 14. Control de Cambios

| Versión | Fecha | Autor | Descripción del Cambio |
|---------|-------|-------|----------------------|
| 1.0 | 09/09/2025 | CoE IA | Versión inicial alineada con ISO 42001 y regulación mexicana |

## 15. Anexos

### Anexo A: Formulario de Solicitud de Caso de Uso IA
[Enlace al formulario digital en SharePoint corporativo]

### Anexo B: Checklist de Evaluación AISIA
[Lista de verificación para evaluación de impacto de sistemas IA]

### Anexo C: Matriz de Clasificación de Riesgos IA
[Herramienta de evaluación automática de nivel de riesgo]

### Anexo D: Plantillas de Documentación Técnica
[Templates obligatorios para documentación de modelos]

### Anexo E: Guía de Respuesta a Incidentes IA
[Procedimiento paso a paso para gestión de crisis]

### Anexo F: Directorio de Contactos de Emergencia
[Lista de contactos para escalamiento 24/7]

---

*Esta política entra en vigencia inmediatamente tras su aprobación y será revisada trimestralmente o ante cambios regulatorios significativos. Para consultas o aclaraciones, contactar al Centro de Excelencia de IA a través del [Canal Centro de Excelencia IA en Google Chat](https://chat.google.com/room/AAQAugDuKpE?cls=1).*

**Documento controlado - Prohibida su reproducción sin autorización del CoE IA**