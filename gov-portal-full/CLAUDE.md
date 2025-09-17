# CLAUDE.md - Documentación para Claude Code

## Instrucciones Importantes para el Desarrollo

### 🔴 FORMULARIOS - IMPORTANTE

**TODOS los nuevos formularios DEBEN generarse usando Google Forms**

#### Requisitos Obligatorios para Formularios:

1. **Usar Google Forms exclusivamente** - No crear formularios HTML personalizados
2. **Autenticación corporativa obligatoria** - Todos los formularios deben:
   - Requerir inicio de sesión con cuenta corporativa
   - Capturar automáticamente el email del usuario
   - Limitar respuestas a usuarios de la organización
3. **Notificaciones** - Configurar notificaciones automáticas a:
   - Email del CoE: `ai@novasolutionsystems.com`
   - Confirmación al usuario que envió el formulario
4. **Almacenamiento** - Las respuestas deben guardarse en Google Sheets compartido
5. **Branding** - Usar colores corporativos:
   - Primary: `#003366`
   - Secondary: `#0066CC`

#### Proceso para Nuevos Formularios:

1. Crear el formulario en Google Forms con los requisitos anteriores
2. Obtener el ID del formulario y la URL de embed
3. Actualizar el archivo `/forms/FORMS_INVENTORY.md` con la información
4. Embeber usando iframe:

```html
<iframe
  src="https://docs.google.com/forms/d/e/FORM_ID/viewform?embedded=true"
  width="100%"
  height="800"
  frameborder="0"
  marginheight="0"
  marginwidth="0"
  style="border: 1px solid #e0e0e0; border-radius: 8px;">
  Cargando formulario...
</iframe>
```

#### Formularios Existentes:

Ver `/forms/FORMS_INVENTORY.md` para la lista completa de formularios y sus IDs.

Scripts disponibles:
- `/forms/generate_google_forms.py` - Genera configuración para crear formularios
- `/forms/CreateForms.gs` - Google Apps Script para crear formularios automáticamente

### 🔵 VARIABLES Y CONFIGURACIÓN

#### Sistema de Variables

Todas las variables configurables están centralizadas en:
- **Archivo**: `/config/variables.yaml`
- **Script**: `/scripts/replace_variables.py`

Variables principales:
- `{{BANK_NAME}}` - Nombre de la institución (Nova)
- `{{COE_EMAIL}}` - Email del CoE (ai@novasolutionsystems.com)
- `{{GCHAT_URL}}` - URL de Google Chat
- `{{NOVA_PORTAL_URL}}` - URL del portal

**IMPORTANTE**: No hardcodear valores. Siempre usar variables del catálogo.

### 🟢 COMUNICACIÓN Y CANALES

#### Google Chat (NO Microsoft Teams)

Todos los canales de comunicación usan **Google Chat**, NO Microsoft Teams:
- URL principal: `https://chat.google.com/room/AAQAugDuKpE?cls=1`
- Canal: Centro de Excelencia IA

Al referenciar canales de comunicación, usar:
- "Google Chat" en lugar de "Teams"
- "canal de Google Chat" en lugar de "canal Teams"

### 🟡 ESTILOS Y TEMAS

#### Archivos CSS

Los estilos están organizados en `/docs/stylesheets/`:
- `nova-theme.css` - Tema principal con colores Nova
- `banking-theme.css` - Estilos específicos para banca
- `dark-mode-corporate.css` - Modo oscuro corporativo
- `contrast-fixes.css` - Mejoras de contraste general
- `menu-contrast-fix.css` - Fix específico para contraste de menús
- `navigation-fixes.css` - Correcciones de navegación
- `tabs-vertical-fix.css` - Fix para tabs verticales
- `mermaid-fixes.css` - Estilos para diagramas Mermaid
- `hero-text-override.css` - Override para texto hero

### 🟣 LINTING Y VALIDACIÓN

Al completar cualquier tarea de código:

1. **Ejecutar linters** (si están configurados):
   ```bash
   npm run lint
   npm run typecheck
   ruff check .
   ```

2. **Validar formularios**:
   - Verificar que todos los formularios usen Google Forms
   - Confirmar autenticación corporativa activa

3. **Verificar variables**:
   - No debe haber emails o URLs hardcodeados
   - Todo debe usar variables de `/config/variables.yaml`

### 🔶 ESTRUCTURA DE PROYECTOS

#### Directorios Principales:

- `/docs/` - Documentación MkDocs
- `/forms/` - Configuración y scripts de formularios
- `/config/` - Archivos de configuración (variables.yaml)
- `/scripts/` - Scripts de utilidad
- `/services/` - Microservicios (API, Dashboard, etc.)
- `/backstage/` - Portal Backstage
- `/infra/` - Configuración de infraestructura

### 🟠 COMMITS Y GIT

**NUNCA hacer commit automáticamente**. Solo commitear cuando el usuario lo solicite explícitamente.

Formato de commit:
```
tipo: descripción breve

Descripción detallada si es necesaria

Co-Authored-By: Claude <noreply@anthropic.com>
```

### 📝 NOTAS ADICIONALES

- **Nova** es el nombre de la institución (no "Banco")
- El portal usa arquitectura de microservicios con:
  - Supabase (base de datos y auth)
  - FastAPI (backend)
  - Next.js (frontend)
  - Temporal (workflows)
  - Backstage (portal de desarrollo)

- Framework IMPACT con 6 dimensiones para medir adopción de IA
- Nova-Cell es la plataforma principal de IA

---

**Última actualización**: 2025-01-15
**Mantenido por**: Centro de Excelencia IA - Nova