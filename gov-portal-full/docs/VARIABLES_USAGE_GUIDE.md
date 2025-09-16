# 📋 Guía de Uso del Sistema de Variables

## Descripción General

El sistema de variables permite centralizar y gestionar todos los datos genéricos del portal del Centro de Excelencia AI, facilitando la personalización para diferentes instituciones bancarias.

## 📁 Estructura

```
gov-portal-full/
├── config/
│   └── variables.yaml       # Catálogo centralizado de variables
├── scripts/
│   └── replace_variables.py # Script de reemplazo automático
└── docs/
    └── VARIABLES_USAGE_GUIDE.md # Esta guía
```

## 🏷️ Variables Disponibles

### Institución
- `{{BANK_NAME}}` - Nombre corto del banco
- `{{BANK_FULL_NAME}}` - Razón social completa
- `{{BANK_DOMAIN}}` - Dominio principal
- `{{BANK_WEBSITE}}` - URL del sitio web

### Centro de Excelencia
- `{{COE_NAME}}` - Nombre del CoE
- `{{COE_EMAIL}}` - Email general
- `{{COE_SUPPORT_EMAIL}}` - Email de soporte
- `{{COE_ADMIN_EMAIL}}` - Email administrativo
- `{{COE_PHONE}}` - Teléfono principal
- `{{COE_EXTENSION}}` - Extensión telefónica

### Nova-Cell Platform
- `{{NOVA_NAME}}` - Nombre de la plataforma
- `{{NOVA_VERSION}}` - Versión actual
- `{{NOVA_SUPPORT_EMAIL}}` - Soporte técnico
- `{{NOVA_PORTAL_URL}}` - URL del portal
- `{{NOVA_API_URL}}` - URL de la API
- `{{NOVA_DOCS_URL}}` - Documentación

### Comunicación
- `{{SLACK_WORKSPACE}}` - Workspace de Slack
- `{{SLACK_URL}}` - URL de Slack
- `{{TEAMS_URL}}` - Google Chat
- `{{GITHUB_URL}}` - Repositorio GitHub

## 🔧 Uso del Script

### Instalación de dependencias

```bash
pip install pyyaml
```

### Comandos Básicos

#### 1. Listar todas las variables
```bash
python scripts/replace_variables.py --list
```

#### 2. Buscar variables en un archivo
```bash
python scripts/replace_variables.py --find docs/index.md
```

#### 3. Simulación (dry-run)
```bash
python scripts/replace_variables.py --dry-run
```

#### 4. Aplicar reemplazos
```bash
python scripts/replace_variables.py
```

#### 5. Procesar tipos específicos
```bash
python scripts/replace_variables.py --patterns "*.md" "*.yaml"
```

## 📝 Cómo Usar Variables en Contenido

### En Markdown
```markdown
Para soporte técnico, contacta a {{COE_SUPPORT_EMAIL}}
o llama al {{COE_PHONE}} ext. {{COE_EXTENSION}}
```

### En YAML
```yaml
contact:
  email: "{{COE_EMAIL}}"
  phone: "{{COE_PHONE}}"
  slack: "{{SLACK_URL}}"
```

### En TypeScript/React
```typescript
const config = {
  apiUrl: "{{NOVA_API_URL}}",
  supportEmail: "{{NOVA_SUPPORT_EMAIL}}"
}
```

## 🔄 Proceso de Personalización

### 1. Editar variables.yaml
```yaml
organization:
  name: "Mi Banco"
  domain: "mibanco.com"

coe:
  emails:
    support: "ayuda@mibanco.com"
```

### 2. Ejecutar reemplazo
```bash
# Primero en modo dry-run
python scripts/replace_variables.py --dry-run

# Si todo está bien, aplicar
python scripts/replace_variables.py
```

### 3. Verificar cambios
```bash
git diff
```

## ⚠️ Consideraciones Importantes

1. **Backups**: El script crea archivos `.backup` automáticamente
2. **Git**: Excluir archivos backup en `.gitignore`
3. **CI/CD**: Integrar el reemplazo en el pipeline de deployment
4. **Validación**: Siempre ejecutar en dry-run primero

## 🚀 Integración en CI/CD

### GitHub Actions Example
```yaml
- name: Replace Variables
  run: |
    python scripts/replace_variables.py \
      --config config/production.yaml
```

### Docker Build
```dockerfile
COPY config/variables.yaml /app/config/
RUN python /app/scripts/replace_variables.py
```

## 📊 Variables por Categoría

### Emails (13 variables)
- CoE: 5 emails
- Nova-Cell: 4 emails
- Herramientas: 2 emails
- Compliance: 2 emails

### URLs (15 variables)
- Nova-Cell: 4 URLs
- Dashboard: 3 URLs
- Ambientes: 6 URLs
- Legal: 2 URLs

### Comunicación (6 variables)
- Slack: 4 variables
- Teams: 2 variables

## 🔍 Troubleshooting

### Variable no reemplazada
- Verificar que existe en `variables.yaml`
- Confirmar formato correcto: `{{VARIABLE_NAME}}`
- Mayúsculas y guiones bajos únicamente

### Error de encoding
- Asegurar UTF-8 en todos los archivos
- Usar `--patterns` para excluir binarios

### Reemplazo incorrecto
- Revisar nombres únicos de variables
- Evitar variables muy genéricas

## 📚 Mejores Prácticas

1. **Naming Convention**: Usar SNAKE_CASE en mayúsculas
2. **Prefijos**: Agrupar por categoría (COE_, NOVA_, etc.)
3. **Documentación**: Comentar variables complejas en YAML
4. **Versionado**: Mantener histórico de cambios
5. **Testing**: Validar en ambiente de desarrollo primero

## 🤝 Soporte

Para dudas o sugerencias sobre el sistema de variables:
- Crear issue en el repositorio
- Contactar al equipo de DevOps
- Revisar logs en `scripts/replace_variables.log`

---
*Sistema de Variables v1.0.0 - Centro de Excelencia AI*