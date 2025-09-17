# Reemplazos de Formularios HTML por Google Forms

## Estado: PENDIENTE

Los siguientes formularios HTML necesitan ser reemplazados por Google Forms embebidos:

### 1. Solicitud de Apoyo
- **Archivo**: `/docs/servicios/solicitar-apoyo.md`
- **Línea**: ~27
- **Buscar**: `<form id="support-request-form" class="support-form">`
- **Reemplazar con**:
```html
<iframe
  src="https://docs.google.com/forms/d/e/[FORM_ID_AQUI]/viewform?embedded=true"
  width="100%"
  height="900"
  frameborder="0"
  marginheight="0"
  marginwidth="0"
  style="border: 1px solid #e0e0e0; border-radius: 8px;">
  Cargando formulario...
</iframe>
```

### 2. Evaluación de Modelos LLM
- **Archivo**: `/docs/servicios/evaluacion-modelos-llm.md`
- **Línea**: ~119
- **Buscar**: `<form id="llm-evaluation-form" class="evaluation-form">`
- **Reemplazar con Google Form embed**

### 3. AISIA Assessment
- **Archivo**: `/docs/tools/aisia-assessment.md`
- **Línea**: ~250
- **Buscar**: `<form id="aisiaForm">`
- **Reemplazar con Google Form embed**

### 4. ROI Calculator
- **Archivo**: `/docs/tools/roi-calculator.md`
- **Línea**: ~117
- **Buscar**: `<form id="roiForm">`
- **Reemplazar con Google Form embed**

### 5. Opportunity Radar
- **Archivo**: `/docs/tools/opportunity-radar.md`
- **Línea**: ~330
- **Buscar**: `<form id="evaluation-form">`
- **Reemplazar con Google Form embed**

### 6. Intake Form
- **Archivo**: `/docs/start-here.md`
- **Línea**: ~159
- **Buscar**: `<form id="intake-form" style="margin-top: 1.5rem;">`
- **Reemplazar con Google Form embed**

## Pasos para Implementar:

### Paso 1: Crear los Google Forms

1. Ir a [Google Apps Script](https://script.google.com)
2. Crear un nuevo proyecto
3. Copiar el contenido de `/forms/CreateForms.gs`
4. Ejecutar la función `createAllForms()`
5. Anotar los IDs de cada formulario creado

### Paso 2: Actualizar los IDs

Actualizar este archivo con los IDs reales de Google Forms:

```javascript
const FORM_IDS = {
  "nova-coe-support": "[ID_REAL_AQUI]",
  "nova-llm-eval": "[ID_REAL_AQUI]",
  "nova-aisia": "[ID_REAL_AQUI]",
  "nova-roi": "[ID_REAL_AQUI]",
  "nova-opportunities": "[ID_REAL_AQUI]",
  "nova-intake": "[ID_REAL_AQUI]"
};
```

### Paso 3: Ejecutar Reemplazos

Usar el script de Python para actualizar automáticamente los archivos:

```bash
cd /Users/weber/Code/ai_coe/gov-portal-full/forms
python3 replace_forms.py
```

### Paso 4: Verificar

1. Revisar cada archivo modificado
2. Probar que los iframes cargan correctamente
3. Verificar autenticación corporativa funciona
4. Confirmar notificaciones se envían a `ai@novasolutionsystems.com`

## Configuración de Google Forms:

### Configuración Requerida para TODOS los Formularios:

- ✅ **Requerir inicio de sesión** con cuenta de la organización
- ✅ **Recopilar direcciones de correo** automáticamente
- ✅ **Limitar a usuarios** de novasolutionsystems.com
- ✅ **Enviar copia de respuestas** al usuario
- ✅ **Notificación al CoE** en ai@novasolutionsystems.com
- ✅ **Guardar en Google Sheets** compartido con el equipo
- ✅ **Mensaje de confirmación**: "Gracias por su solicitud. El equipo del CoE se pondrá en contacto dentro de las próximas 24 horas hábiles."
- ✅ **Colores corporativos**:
  - Primary: #003366
  - Secondary: #0066CC
  - Background: #FFFFFF

## Links Útiles:

- [Google Forms API Documentation](https://developers.google.com/forms/api)
- [Apps Script Forms Service](https://developers.google.com/apps-script/reference/forms)
- [Embed Google Forms](https://support.google.com/docs/answer/2839588)

## Notas:

- Los formularios HTML actuales tienen lógica JavaScript que se perderá
- Considerar usar Google Apps Script para lógica personalizada si es necesaria
- Las validaciones se pueden configurar directamente en Google Forms
- Los cálculos del ROI se pueden hacer con Google Sheets + Apps Script

---

**Estado**: Pendiente creación de formularios en Google Forms
**Fecha**: 2025-01-15
**Responsable**: Equipo CoE