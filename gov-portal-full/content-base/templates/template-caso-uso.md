# Plantilla: Caso de Uso de IA - [NOMBRE_CASO_USO]

## Identificación
- **ID**: CU-[ÁREA]-[NÚMERO]
- **Nombre**: [Nombre descriptivo del caso de uso]
- **Área Solicitante**: [Departamento/Unidad]
- **Sponsor**: [Nombre y cargo del sponsor]
- **Fecha Propuesta**: [FECHA]
- **Estado**: [IDEACIÓN/EVALUACIÓN/PILOTO/PRODUCCIÓN]
- **Prioridad**: [ALTA/MEDIA/BAJA]

## 1. Resumen Ejecutivo

### Descripción
[Descripción concisa del caso de uso en 2-3 oraciones, explicando QUÉ se quiere hacer y POR QUÉ]

### Propuesta de Valor
- **Problema a resolver**: [Pain point específico]
- **Solución propuesta**: [Cómo la IA lo resuelve]
- **Beneficio principal**: [Impacto esperado]

## 2. Análisis de Negocio

### Situación Actual (AS-IS)
- **Proceso actual**: [Descripción del proceso manual/actual]
- **Volumen**: [Transacciones/casos por día/mes]
- **Tiempo de ciclo**: [Duración actual del proceso]
- **FTEs dedicados**: [Número de personas]
- **Costo operativo**: $[Monto anual/mensual]
- **Tasa de error**: [%]

### Situación Deseada (TO-BE)
- **Proceso con IA**: [Cómo funcionará con Nova-Cell]
- **Tiempo de ciclo esperado**: [Reducción esperada]
- **FTEs optimizados**: [Liberación de capacidad]
- **Costo proyectado**: $[Nuevo costo]
- **Mejora en calidad**: [% reducción de errores]

### Análisis Costo-Beneficio
| Concepto | Valor Actual | Valor con IA | Mejora |
|----------|-------------|--------------|--------|
| Tiempo proceso | [X hrs] | [Y hrs] | -[Z]% |
| Costo por transacción | $[X] | $[Y] | -$[Z] |
| Accuracy | [X]% | [Y]% | +[Z]% |
| Satisfacción cliente | [X]/10 | [Y]/10 | +[Z] |

## 3. Viabilidad Técnica con Nova-Cell

### Capacidades de IA Requeridas
- [ ] **Procesamiento de Lenguaje Natural**
  - Tipo: [Comprensión/Generación/Clasificación]
  - Complejidad: [Baja/Media/Alta]
  
- [ ] **Visión Computacional**
  - Tipo: [OCR/Clasificación/Detección]
  - Complejidad: [Baja/Media/Alta]
  
- [ ] **Análisis Predictivo**
  - Tipo: [Clasificación/Regresión/Clustering]
  - Complejidad: [Baja/Media/Alta]

- [ ] **Automatización de Procesos**
  - Tipo: [RPA/Orquestación/Decisión]
  - Complejidad: [Baja/Media/Alta]

### Arquitectura Propuesta
```yaml
Entrada:
  - Fuente: [Sistema/API/Manual]
  - Formato: [Estructurado/No estructurado]
  - Volumen: [Registros/día]

Procesamiento_Nova_Cell:
  - Modelo_Principal: [GPT-5/Claude/Gemini]
  - Modelo_Respaldo: [Alternativa]
  - Agentes:
    - Agente_1: [Función]
    - Agente_2: [Función]
  
Salida:
  - Destino: [Sistema/Usuario/API]
  - Formato: [JSON/PDF/Dashboard]
  - Frecuencia: [Real-time/Batch]
```

### Integraciones Necesarias
| Sistema | Tipo | Criticidad | Complejidad |
|---------|------|-----------|-------------|
| [Sistema 1] | [API/DB/File] | [Alta/Media/Baja] | [Simple/Media/Compleja] |
| [Sistema 2] | [API/DB/File] | [Alta/Media/Baja] | [Simple/Media/Compleja] |

## 4. Datos

### Requerimientos de Datos
- **Datos de entrenamiento**: [Disponibles/Por generar]
- **Volumen necesario**: [Número de ejemplos]
- **Calidad actual**: [Alta/Media/Baja]
- **Preparación requerida**: [Limpieza/Etiquetado/Augmentation]

### Consideraciones de Privacidad
- [ ] Contiene PII (Datos personales)
- [ ] Requiere anonimización
- [ ] Cumple con LFPDPPP
- [ ] Necesita consentimiento adicional

## 5. Evaluación con AI Opportunity Radar

### Dimensiones de Evaluación

#### Impacto de Negocio (0-10)
- **Ahorro de costos**: [Score] - [Justificación]
- **Mejora de ingresos**: [Score] - [Justificación]
- **Experiencia cliente**: [Score] - [Justificación]
- **Reducción de riesgo**: [Score] - [Justificación]
- **Score promedio**: [X.X]

#### Factibilidad Técnica (0-10)
- **Disponibilidad de datos**: [Score]
- **Madurez de la tecnología**: [Score]
- **Complejidad de integración**: [Score]
- **Skills disponibles**: [Score]
- **Score promedio**: [X.X]

#### Alineación Estratégica (0-10)
- **Fit con estrategia**: [Score]
- **Prioridad del negocio**: [Score]
- **Innovación**: [Score]
- **Score promedio**: [X.X]

### Matriz de Priorización
```
Alta Factibilidad + Alto Impacto = QUICK WIN ✅
Alta Factibilidad + Bajo Impacto = FILL-IN
Baja Factibilidad + Alto Impacto = STRATEGIC
Baja Factibilidad + Bajo Impacto = AVOID ❌
```

**Clasificación de este caso**: [QUICK WIN/STRATEGIC/FILL-IN/AVOID]

## 6. Riesgos y Mitigación

### Análisis de Riesgos
| Riesgo | Probabilidad | Impacto | Estrategia de Mitigación |
|--------|-------------|---------|-------------------------|
| Calidad de datos insuficiente | [A/M/B] | [A/M/B] | [Plan de acción] |
| Resistencia al cambio | [A/M/B] | [A/M/B] | [Plan de acción] |
| Sesgo algorítmico | [A/M/B] | [A/M/B] | [Plan de acción] |
| Fallo de integración | [A/M/B] | [A/M/B] | [Plan de acción] |
| Incumplimiento regulatorio | [A/M/B] | [A/M/B] | [Plan de acción] |

### Consideraciones Éticas
- [ ] Transparencia en decisiones automatizadas
- [ ] Equidad y no discriminación validada
- [ ] Supervisión humana apropiada
- [ ] Explicabilidad de resultados

## 7. Plan de Implementación

### Fase 1: POC (4 semanas)
**Objetivo**: Validar viabilidad técnica
- Semana 1-2: Setup y configuración Nova-Cell
- Semana 3: Desarrollo de prompts y agentes
- Semana 4: Pruebas con datos sintéticos
- **Criterio de éxito**: Accuracy > [X]%

### Fase 2: Piloto (8 semanas)
**Objetivo**: Validar valor de negocio
- Semana 1-2: Integración con sistemas
- Semana 3-4: Pruebas con datos reales
- Semana 5-6: Ajustes y optimización
- Semana 7-8: Medición de resultados
- **Criterio de éxito**: ROI positivo proyectado

### Fase 3: Producción (4 semanas)
**Objetivo**: Despliegue completo
- Semana 1: Preparación ambiente productivo
- Semana 2: Migración y go-live
- Semana 3-4: Estabilización y soporte
- **Criterio de éxito**: SLA cumplido

## 8. Métricas de Éxito

### KPIs Operativos
- **Tiempo de procesamiento**: Reducción > [X]%
- **Accuracy**: > [X]%
- **Volumen procesado**: [X] transacciones/día
- **Disponibilidad**: > 99.5%

### KPIs de Negocio
- **ROI**: Positivo en semana [X]
- **Ahorro anual**: $[Monto]
- **NPS impactado**: +[X] puntos
- **FTEs liberados para valor**: [X]

### Métricas IMPACT (Nova)
- **I**mplementation: Coverage [X]%
- **M**omentum: Weekly frequency [X]
- **P**erformance: Productivity +[X]%
- **A**cceptance: User satisfaction [X]/10
- **C**ost-effective: Cost per transaction -[X]%
- **T**rust: Confidence in outputs [X]%

## 9. Equipo y Governance

### Equipo Core
| Rol | Nombre | Dedicación | Responsabilidad |
|-----|--------|------------|-----------------|
| Product Owner | [Nombre] | 50% | Visión y prioridades |
| Risk Officer IA | [Nombre] | 30% | Compliance y riesgos |
| Tech Lead | [Nombre] | 100% | Implementación técnica |
| SME Negocio | [Nombre] | 40% | Conocimiento del proceso |
| Data Scientist | [Nombre] | 80% | Modelos y prompts |

### Estructura de Gobierno
- **Comité Directivo**: Mensual
- **Comité Operativo**: Semanal
- **Daily Standups**: Durante implementación

## 10. Presupuesto Estimado

### Costos de Implementación
| Concepto | Monto | Notas |
|----------|-------|-------|
| Licencias Nova-Cell | $[X] | [Usuarios/transacciones] |
| Desarrollo | $[X] | [Horas consultoría] |
| Infraestructura | $[X] | [Cloud/On-prem] |
| Capacitación | $[X] | [Usuarios a entrenar] |
| **Total** | **$[X]** | |

### Beneficios Esperados (Anual)
| Concepto | Monto | Cálculo |
|----------|-------|---------|
| Ahorro FTEs | $[X] | [N FTEs × Costo] |
| Reducción errores | $[X] | [Costo error × Reducción] |
| Mejora productividad | $[X] | [Tiempo × Valor] |
| **Total** | **$[X]** | |

**Payback Period**: [X] meses

## 11. Criterios de Aprobación

### Go/No-Go Checklist
- [ ] ROI > 30% anual
- [ ] Riesgo regulatorio aceptable
- [ ] Tecnología probada
- [ ] Sponsor comprometido
- [ ] Equipo disponible
- [ ] Presupuesto aprobado
- [ ] Alineación estratégica confirmada

## 12. Próximos Pasos
1. [ ] Presentar a Comité de IA
2. [ ] Obtener aprobación presupuestal
3. [ ] Asignar equipo
4. [ ] Iniciar POC
5. [ ] Definir plan de comunicación

## Anexos
- **Anexo A**: Proceso detallado AS-IS
- **Anexo B**: Mockups de solución
- **Anexo C**: Análisis de datos disponibles
- **Anexo D**: Benchmark de industria

---

### Notas para el Evaluador:
- Verificar alineación con portfolio de casos de uso
- Validar no duplicación con iniciativas existentes
- Confirmar disponibilidad de recursos
- Evaluar interdependencias con otros proyectos
- Considerar ventana de implementación óptima