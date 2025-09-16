# 🆘 Solicitar Apoyo del CoE

## Tu Portal Único para Soporte en IA

### 🎯 ¿Cómo Podemos Ayudarte?

<div class="support-grid">

### 🚀 Necesito empezar un proyecto
Identificación de oportunidades, definición de casos de uso, y roadmap de implementación.

### 🛠️ Tengo un problema técnico
Troubleshooting, debugging, optimización de modelos, y resolución de issues.

### 📚 Requiero capacitación
Workshops, bootcamps, certificaciones, y programas de formación personalizados.

### 🔍 Busco evaluación/auditoría
Assessment de modelos, revisión de arquitectura, auditoría de seguridad, y compliance.

</div>

---

## 📝 Formulario de Solicitud de Apoyo

<form id="support-request-form" class="support-form">

### Información del Solicitante

<div class="form-section">
<div class="form-row">
<div class="form-group">
<label for="nombre">Nombre completo*</label>
<input type="text" id="nombre" name="nombre" required>
</div>
<div class="form-group">
<label for="email">Email corporativo*</label>
<input type="email" id="email" name="email" required pattern=".*@banco\.mx$">
</div>
</div>

<div class="form-row">
<div class="form-group">
<label for="telefono">Teléfono/Extensión*</label>
<input type="tel" id="telefono" name="telefono" required>
</div>
<div class="form-group">
<label for="squad">Squad/Departamento*</label>
<select id="squad" name="squad" required>
<option value="">Seleccionar...</option>
<option value="digital">Banca Digital</option>
<option value="riesgos">Riesgos</option>
<option value="operaciones">Operaciones</option>
<option value="ti">Tecnología</option>
<option value="innovacion">Innovación</option>
<option value="datos">Data & Analytics</option>
<option value="comercial">Comercial</option>
<option value="rh">Recursos Humanos</option>
</select>
</div>
</div>

<div class="form-group">
<label for="gerente">Gerente/Sponsor*</label>
<input type="text" id="gerente" name="gerente" required>
</div>
</div>

### Tipo de Solicitud

<div class="form-section">
<div class="form-group">
<label>Categoría de apoyo requerido*</label>
<div class="radio-cards">
<label class="radio-card">
<input type="radio" name="categoria" value="consultoria" required>
<div class="card-content">
<span class="card-icon">💡</span>
<span class="card-title">Consultoría</span>
<span class="card-desc">Estrategia, casos de uso, roadmap</span>
</div>
</label>
<label class="radio-card">
<input type="radio" name="categoria" value="desarrollo">
<div class="card-content">
<span class="card-icon">⚙️</span>
<span class="card-title">Desarrollo</span>
<span class="card-desc">PoC, MVP, implementación</span>
</div>
</label>
<label class="radio-card">
<input type="radio" name="categoria" value="soporte">
<div class="card-content">
<span class="card-icon">🔧</span>
<span class="card-title">Soporte Técnico</span>
<span class="card-desc">Troubleshooting, optimización</span>
</div>
</label>
<label class="radio-card">
<input type="radio" name="categoria" value="capacitacion">
<div class="card-content">
<span class="card-icon">🎓</span>
<span class="card-title">Capacitación</span>
<span class="card-desc">Training, workshops, certificación</span>
</div>
</label>
<label class="radio-card">
<input type="radio" name="categoria" value="evaluacion">
<div class="card-content">
<span class="card-icon">📊</span>
<span class="card-title">Evaluación</span>
<span class="card-desc">Assessment, auditoría, validación</span>
</div>
</label>
<label class="radio-card">
<input type="radio" name="categoria" value="gobernanza">
<div class="card-content">
<span class="card-icon">📋</span>
<span class="card-title">Gobernanza</span>
<span class="card-desc">Compliance, políticas, frameworks</span>
</div>
</label>
</div>
</div>

<div class="form-group">
<label for="prioridad">Prioridad*</label>
<select id="prioridad" name="prioridad" required>
<option value="">Seleccionar...</option>
<option value="critica">🔴 Crítica - Bloqueante para producción (SLA: 4 horas)</option>
<option value="alta">🟠 Alta - Impacto significativo (SLA: 24 horas)</option>
<option value="media">🟡 Media - Importante pero no urgente (SLA: 48 horas)</option>
<option value="baja">🟢 Baja - Mejora o consulta general (SLA: 5 días)</option>
</select>
</div>
</div>

### Descripción de la Solicitud

<div class="form-section">
<div class="form-group">
<label for="titulo">Título/Resumen*</label>
<input type="text" id="titulo" name="titulo" required maxlength="100" placeholder="Descripción breve del apoyo requerido">
</div>

<div class="form-group">
<label for="descripcion">Descripción detallada* (mín. 100 caracteres)</label>
<textarea id="descripcion" name="descripcion" required minlength="100" rows="6" placeholder="Por favor describe:
- Contexto y situación actual
- Problema o necesidad específica
- Resultado esperado
- Restricciones o consideraciones especiales"></textarea>
</div>

<div class="form-group">
<label for="impacto">Impacto en el negocio*</label>
<textarea id="impacto" name="impacto" required rows="3" placeholder="¿Cómo afecta esto al negocio? ¿Cuántos usuarios impactados? ¿Pérdida potencial?"></textarea>
</div>
</div>

### Información Adicional

<div class="form-section">
<div class="form-row">
<div class="form-group">
<label for="proyecto">Proyecto/Iniciativa relacionada</label>
<input type="text" id="proyecto" name="proyecto" placeholder="Nombre del proyecto si aplica">
</div>
<div class="form-group">
<label for="presupuesto">Presupuesto disponible</label>
<select id="presupuesto" name="presupuesto">
<option value="">No definido</option>
<option value="0-10k">< $10,000 USD</option>
<option value="10-50k">$10,000 - $50,000 USD</option>
<option value="50-100k">$50,000 - $100,000 USD</option>
<option value="100k+">> $100,000 USD</option>
</select>
</div>
</div>

<div class="form-row">
<div class="form-group">
<label for="fecha_requerida">Fecha requerida</label>
<input type="date" id="fecha_requerida" name="fecha_requerida" min="2025-01-20">
</div>
<div class="form-group">
<label for="duracion">Duración estimada</label>
<select id="duracion" name="duracion">
<option value="">No definido</option>
<option value="dias">Días</option>
<option value="semanas">Semanas</option>
<option value="meses">Meses</option>
<option value="ongoing">Ongoing</option>
</select>
</div>
</div>

<div class="form-group">
<label>Servicios específicos requeridos (opcional)</label>
<div class="checkbox-group">
<label><input type="checkbox" name="servicios" value="arquitectura"> Diseño de arquitectura</label>
<label><input type="checkbox" name="servicios" value="poc"> Desarrollo de PoC</label>
<label><input type="checkbox" name="servicios" value="mlops"> Implementación MLOps</label>
<label><input type="checkbox" name="servicios" value="seguridad"> Evaluación de seguridad</label>
<label><input type="checkbox" name="servicios" value="training"> Training del equipo</label>
<label><input type="checkbox" name="servicios" value="mentoring"> Mentoring/Coaching</label>
</div>
</div>

<div class="form-group">
<label for="archivos">Adjuntar documentación (opcional)</label>
<input type="file" id="archivos" name="archivos" multiple accept=".pdf,.doc,.docx,.xlsx,.pptx,.png,.jpg">
<small>Máximo 5 archivos, 10MB cada uno</small>
</div>

<div class="form-group">
<label for="comentarios">Comentarios adicionales</label>
<textarea id="comentarios" name="comentarios" rows="3"></textarea>
</div>
</div>

### Confirmación

<div class="form-section">
<div class="form-group">
<label class="checkbox-label">
<input type="checkbox" name="urgente" value="si">
<strong>⚡ Marcar como URGENTE</strong> (requiere justificación y aprobación gerencial)
</label>
</div>

<div class="form-group">
<label class="checkbox-label">
<input type="checkbox" name="terminos" required>
Confirmo que la información proporcionada es correcta y que cuento con la aprobación de mi gerente para esta solicitud*
</label>
</div>
</div>

<div class="form-actions">
<button type="submit" class="btn-primary">Enviar Solicitud</button>
<button type="button" class="btn-secondary" onclick="saveDraft()">Guardar Borrador</button>
<button type="reset" class="btn-tertiary">Limpiar Formulario</button>
</div>

</form>

---

## ⏱️ SLAs de Respuesta

### Tiempos de Respuesta Comprometidos

| Prioridad | Primera Respuesta | Asignación de Recursos | Resolución/Plan de Acción |
|-----------|------------------|----------------------|---------------------------|
| 🔴 **Crítica** | 1 hora | 4 horas | 24 horas |
| 🟠 **Alta** | 4 horas | 24 horas | 48 horas |
| 🟡 **Media** | 24 horas | 48 horas | 5 días hábiles |
| 🟢 **Baja** | 48 horas | 5 días hábiles | 10 días hábiles |

### Horario de Atención

- **Soporte Regular:** Lunes a Viernes, 9:00 - 18:00 hrs
- **Soporte Extendido:** Lunes a Viernes, 7:00 - 22:00 hrs (con cargo adicional)
- **Soporte 24/7:** Solo para servicios críticos con contrato enterprise

---

## 🔄 Proceso de Atención

```mermaid
graph LR
    A[Solicitud<br/>Recibida] --> B{Validación<br/>Inicial}
    B -->|Completa| C[Asignación<br/>de Ticket]
    B -->|Incompleta| D[Solicitar<br/>Información]
    C --> E[Evaluación<br/>Técnica]
    E --> F{Tipo de<br/>Apoyo}
    F -->|Simple| G[Resolución<br/>Directa]
    F -->|Complejo| H[Asignación<br/>de Equipo]
    H --> I[Plan de<br/>Trabajo]
    I --> J[Ejecución]
    J --> K[Entrega y<br/>Validación]
    G --> K
    K --> L[Cierre de<br/>Ticket]
    
    style A fill:#667eea
    style C fill:#764ba2
    style K fill:#51cf66
```

---

## 📊 Tracking de tu Solicitud

### Estados de la Solicitud

<div class="status-cards">

<div class="status-card">
<span class="status-icon">📥</span>
<h4>Recibida</h4>
<p>Tu solicitud ha sido registrada en nuestro sistema</p>
</div>

<div class="status-card">
<span class="status-icon">👀</span>
<h4>En Revisión</h4>
<p>Estamos evaluando los requerimientos y recursos necesarios</p>
</div>

<div class="status-card">
<span class="status-icon">👥</span>
<h4>Asignada</h4>
<p>Un especialista ha sido asignado a tu solicitud</p>
</div>

<div class="status-card">
<span class="status-icon">⚙️</span>
<h4>En Progreso</h4>
<p>Trabajando activamente en la solución</p>
</div>

<div class="status-card">
<span class="status-icon">✅</span>
<h4>Resuelta</h4>
<p>Solución entregada, pendiente tu validación</p>
</div>

<div class="status-card">
<span class="status-icon">🔒</span>
<h4>Cerrada</h4>
<p>Ticket cerrado con éxito</p>
</div>

</div>

### Consulta el Estado de tu Ticket

<div class="ticket-lookup">
<input type="text" placeholder="Ingresa tu número de ticket (ej: COE-2025-0123)" class="ticket-input">
<button class="btn-primary">Consultar Estado</button>
</div>

---

## 💬 Canales Alternativos de Contacto

### Para Consultas Rápidas

<div class="contact-grid">

<div class="contact-card">
<h4>💬 Chat en Vivo</h4>
<p>Disponible en horario de oficina</p>
<a href="#" class="btn-secondary">Iniciar Chat</a>
</div>

<div class="contact-card">
<h4>📧 Email Directo</h4>
<p>ai@novasolutionsystems.com</p>
<p>Respuesta en 24 horas</p>
</div>

<div class="contact-card">
<h4>📞 Hotline</h4>
<p>+52 55 1234 5678 ext. 1000</p>
<p>Lun-Vie 9:00-18:00</p>
</div>

<div class="contact-card">
<h4>💼 Teams</h4>
<p>#coe-ia-support</p>
<a href="https://teams.microsoft.com/channel/coe-support" class="btn-secondary">Ir al Canal</a>
</div>

</div>

### Office Hours Semanales

**Sesiones abiertas de consulta sin cita previa:**
- 🗓️ **Martes:** 10:00 - 11:00 hrs - Temas técnicos
- 🗓️ **Jueves:** 15:00 - 16:00 hrs - Estrategia y gobernanza
- 🗓️ **Viernes:** 12:00 - 13:00 hrs - Open Q&A

[Unirse a Office Hours](https://teams.microsoft.com/meet/office-hours){.md-button}

---

## 📈 Métricas de Satisfacción

### Nuestro Desempeño (Último Mes)

<div class="metrics-grid">

<div class="metric">
<span class="metric-value">4.7/5</span>
<span class="metric-label">Satisfacción General</span>
</div>

<div class="metric">
<span class="metric-value">92%</span>
<span class="metric-label">SLA Cumplido</span>
</div>

<div class="metric">
<span class="metric-value">18 hrs</span>
<span class="metric-label">Tiempo Promedio Resolución</span>
</div>

<div class="metric">
<span class="metric-value">156</span>
<span class="metric-label">Tickets Resueltos</span>
</div>

</div>

---

## ❓ Preguntas Frecuentes

<details>
<summary><strong>¿Necesito aprobación de mi gerente para solicitar apoyo?</strong></summary>
Sí, todas las solicitudes requieren aprobación gerencial, especialmente si implican asignación de recursos o presupuesto.
</details>

<details>
<summary><strong>¿Cuánto cuesta el servicio de apoyo?</strong></summary>
El apoyo básico está incluido en el servicio del CoE. Proyectos específicos o dedicación exclusiva pueden tener costos adicionales que se cotizarán caso por caso.
</details>

<details>
<summary><strong>¿Puedo solicitar apoyo para proyectos ya en curso?</strong></summary>
Sí, podemos apoyar en cualquier fase del proyecto, desde ideación hasta optimización post-producción.
</details>

<details>
<summary><strong>¿Qué pasa si mi solicitud es rechazada?</strong></summary>
Te proporcionaremos feedback detallado y alternativas. Puedes reenviar la solicitud con las modificaciones sugeridas.
</details>

<details>
<summary><strong>¿Cómo escalo una solicitud si no recibo respuesta?</strong></summary>
Puedes escalar contactando a ai@novasolutionsystems.com o llamando a la extensión 9999.
</details>

---

## 📚 Recursos de Autoservicio

### Antes de Solicitar Apoyo, Consulta:

<div class="resource-cards">

<div class="resource-card">
<h4>📖 Knowledge Base</h4>
<p>+500 artículos técnicos</p>
<a href="../recursos/knowledge-base">Explorar →</a>
</div>

<div class="resource-card">
<h4>🎥 Video Tutoriales</h4>
<p>+100 horas de contenido</p>
<a href="../recursos/videos">Ver Videos →</a>
</div>

<div class="resource-card">
<h4>💬 Comunidad</h4>
<p>+1,000 miembros activos</p>
<a href="../comunidad">Unirse →</a>
</div>

<div class="resource-card">
<h4>🔧 Herramientas</h4>
<p>Calculadoras y templates</p>
<a href="../herramientas">Acceder →</a>
</div>

</div>

---

<style>
.support-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.support-grid h3 {
    color: #667eea;
    margin-bottom: 0.5rem;
}

.support-form {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.form-section {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #e0e0e0;
}

.form-section:last-child {
    border-bottom: none;
}

.form-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
}

.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #2c3e50;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 1rem;
}

.radio-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin-top: 0.5rem;
}

.radio-card {
    position: relative;
    cursor: pointer;
}

.radio-card input[type="radio"] {
    position: absolute;
    opacity: 0;
}

.card-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    transition: all 0.3s;
    text-align: center;
}

.radio-card input[type="radio"]:checked + .card-content {
    border-color: #667eea;
    background: #f0f4ff;
}

.card-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.card-title {
    font-weight: 600;
    margin-bottom: 0.25rem;
}

.card-desc {
    font-size: 0.85rem;
    color: #666;
}

.checkbox-group {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 0.75rem;
    margin-top: 0.5rem;
}

.checkbox-label {
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
}

.form-actions {
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
    margin-top: 2rem;
}

.btn-primary {
    background: #667eea;
    color: white;
    padding: 0.75rem 2rem;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
}

.btn-secondary {
    background: #2f9477;
    color: white;
    padding: 0.75rem 2rem;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
}

.btn-tertiary {
    background: transparent;
    color: #667eea;
    padding: 0.75rem 2rem;
    border: 1px solid #667eea;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
}

.status-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
}

.status-card {
    text-align: center;
    padding: 1.5rem 1rem;
    background: #f5f7fa;
    border-radius: 8px;
}

.status-icon {
    font-size: 2rem;
    display: block;
    margin-bottom: 0.5rem;
}

.ticket-lookup {
    display: flex;
    gap: 1rem;
    max-width: 500px;
    margin: 2rem 0;
}

.ticket-input {
    flex: 1;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 6px;
}

.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.contact-card {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    text-align: center;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.metric {
    text-align: center;
    padding: 1.5rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 8px;
}

.metric-value {
    display: block;
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.metric-label {
    font-size: 0.9rem;
    opacity: 0.95;
}

.resource-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.resource-card {
    background: #f5f7fa;
    padding: 1.5rem;
    border-radius: 8px;
    border-left: 4px solid #667eea;
}

@media (max-width: 768px) {
    .form-row {
        grid-template-columns: 1fr;
    }
    
    .radio-cards {
        grid-template-columns: 1fr;
    }
    
    .form-actions {
        flex-direction: column;
    }
    
    .ticket-lookup {
        flex-direction: column;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('support-request-form');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Generate ticket number
            const ticketNumber = 'COE-2025-' + Math.floor(Math.random() * 10000).toString().padStart(4, '0');
            
            // Success message
            alert(`✅ Solicitud enviada correctamente\n\nTu número de ticket es: ${ticketNumber}\n\nRecibirás confirmación por email en las próximas horas según el SLA de tu prioridad seleccionada.`);
            
            // Reset form
            form.reset();
        });
    }
});

function saveDraft() {
    // Save form data to localStorage
    const form = document.getElementById('support-request-form');
    const formData = new FormData(form);
    const data = {};
    
    for (let [key, value] of formData.entries()) {
        data[key] = value;
    }
    
    localStorage.setItem('support-draft', JSON.stringify(data));
    alert('✅ Borrador guardado exitosamente');
}

// Load draft on page load
window.addEventListener('load', function() {
    const draft = localStorage.getItem('support-draft');
    if (draft) {
        const data = JSON.parse(draft);
        const form = document.getElementById('support-request-form');
        
        // Offer to load draft
        if (confirm('Tienes un borrador guardado. ¿Deseas cargarlo?')) {
            for (let key in data) {
                const field = form.elements[key];
                if (field) {
                    field.value = data[key];
                }
            }
        }
    }
});
</script>

---

**Centro de Excelencia de IA** | Siempre listos para apoyarte | ai@novasolutionsystems.com