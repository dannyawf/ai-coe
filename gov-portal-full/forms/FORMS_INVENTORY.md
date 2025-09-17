# Inventario de Formularios - Portal CoE IA

## Formularios Identificados

### 1. **Formulario de Solicitud de Apoyo**
- **Ubicación**: `/docs/servicios/solicitar-apoyo.md`
- **ID HTML**: `support-request-form`
- **Campos**:
  - Tipo de solicitud (consultoría, arquitectura, capacitación, etc.)
  - Descripción del proyecto
  - Equipo solicitante
  - Urgencia
  - Área/Departamento
  - Contacto principal

### 2. **Formulario de Evaluación de Modelos LLM**
- **Ubicación**: `/docs/servicios/evaluacion-modelos-llm.md`
- **ID HTML**: `llm-evaluation-form`
- **Campos**:
  - Modelo a evaluar
  - Caso de uso
  - Métricas de evaluación requeridas
  - Tipo de datos
  - Requisitos de seguridad
  - Presupuesto estimado

### 3. **AISIA Assessment Form**
- **Ubicación**: `/docs/tools/aisia-assessment.md`
- **ID HTML**: `aisiaForm`
- **Campos**:
  - Dimensiones de evaluación AISIA
  - Nivel de madurez actual
  - Objetivos de mejora
  - Restricciones regulatorias
  - Timeline esperado

### 4. **ROI Calculator Form**
- **Ubicación**: `/docs/tools/roi-calculator.md`
- **ID HTML**: `roiForm`
- **Campos**:
  - Costos de implementación
  - Beneficios esperados
  - Timeline del proyecto
  - Número de usuarios impactados
  - Métricas de éxito

### 5. **Opportunity Radar Evaluation Form**
- **Ubicación**: `/docs/tools/opportunity-radar.md`
- **ID HTML**: `evaluation-form`
- **Campos**:
  - Área de oportunidad
  - Impacto potencial
  - Complejidad técnica
  - Recursos disponibles
  - Prioridad del negocio

### 6. **Intake Form (Start Here)**
- **Ubicación**: `/docs/start-here.md`
- **ID HTML**: `intake-form`
- **Campos**:
  - Nombre del proyecto
  - Objetivo principal
  - Etapa actual (explorar, experimentar, construir, etc.)
  - Tecnologías involucradas
  - Equipo responsable

### 7. **Formulario de Caso de Uso (Anexo A)**
- **Ubicación**: `/docs/annexes/anexo-a-formulario-caso-uso.md`
- **Tipo**: Template de documento
- **Campos**:
  - Información del proyecto
  - Justificación de negocio
  - Arquitectura técnica
  - Plan de implementación
  - Evaluación de riesgos
  - Métricas de éxito

### 8. **Checklist AISIA (Anexo B)**
- **Ubicación**: `/docs/annexes/anexo-b-checklist-aisia.md`
- **Tipo**: Checklist interactivo
- **Campos**:
  - Criterios de evaluación por dimensión
  - Estado de cumplimiento
  - Evidencias requeridas
  - Plan de remediación

### 9. **Formulario de Red Teaming**
- **Ubicación**: `/docs/servicios/red-teaming.md`
- **Tipo**: Email link (mailto)
- **Campos sugeridos**:
  - Sistema a evaluar
  - Tipo de evaluación requerida
  - Alcance del testing
  - Restricciones de seguridad

## URLs de Google Forms a Generar

| Formulario | Nombre en Google Forms | ID Sugerido |
|------------|------------------------|-------------|
| Solicitud de Apoyo | Nova CoE - Solicitud de Apoyo | nova-coe-support |
| Evaluación LLM | Nova CoE - Evaluación Modelos LLM | nova-llm-eval |
| AISIA Assessment | Nova CoE - Evaluación AISIA | nova-aisia |
| ROI Calculator | Nova CoE - Calculadora ROI | nova-roi |
| Opportunity Radar | Nova CoE - Radar de Oportunidades | nova-opportunities |
| Intake Form | Nova CoE - Registro de Proyecto | nova-intake |
| Caso de Uso | Nova CoE - Formulario Caso de Uso | nova-use-case |
| Checklist AISIA | Nova CoE - Checklist AISIA | nova-checklist |
| Red Teaming | Nova CoE - Solicitud Red Teaming | nova-redteam |

## Configuración Requerida

Todos los formularios deben:
1. Requerir autenticación con correo corporativo
2. Capturar automáticamente el email del usuario
3. Enviar confirmación al solicitante
4. Notificar al equipo CoE correspondiente
5. Guardar respuestas en Google Sheets compartido
6. Incluir el logo de Nova
7. Usar los colores corporativos (#003366, #0066CC)