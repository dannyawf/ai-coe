/**
 * Google Apps Script para crear automáticamente los formularios del CoE
 * Ejecutar en Google Apps Script: https://script.google.com
 */

// Configuración de los formularios
const FORMS_CONFIG = {
  "nova-coe-support": {
    title: "Nova CoE - Solicitud de Apoyo",
    description: "Solicite apoyo del Centro de Excelencia de IA para su proyecto",
    responseEmail: "ai@novasolutionsystems.com"
  },
  "nova-llm-eval": {
    title: "Nova CoE - Evaluación de Modelos LLM",
    description: "Solicite una evaluación técnica de modelos de lenguaje para su caso de uso",
    responseEmail: "ai@novasolutionsystems.com"
  },
  "nova-aisia": {
    title: "Nova CoE - Evaluación AISIA",
    description: "Evalúe la madurez de IA de su organización con el framework AISIA",
    responseEmail: "ai@novasolutionsystems.com"
  },
  "nova-roi": {
    title: "Nova CoE - Calculadora ROI",
    description: "Calcule el retorno de inversión de su iniciativa de IA",
    responseEmail: "ai@novasolutionsystems.com"
  },
  "nova-intake": {
    title: "Nova CoE - Registro de Proyecto IA",
    description: "Registre su proyecto de IA para obtener apoyo del CoE",
    responseEmail: "ai@novasolutionsystems.com"
  }
};

/**
 * Función principal para crear todos los formularios
 */
function createAllForms() {
  const results = {};

  // Crear formulario de Solicitud de Apoyo
  results["nova-coe-support"] = createSupportForm();

  // Crear formulario de Evaluación LLM
  results["nova-llm-eval"] = createLLMEvalForm();

  // Crear formulario AISIA
  results["nova-aisia"] = createAISIAForm();

  // Crear formulario ROI
  results["nova-roi"] = createROIForm();

  // Crear formulario Intake
  results["nova-intake"] = createIntakeForm();

  // Guardar URLs en una hoja de cálculo
  saveFormURLs(results);

  Logger.log("Todos los formularios creados exitosamente:");
  Logger.log(results);

  return results;
}

/**
 * Crear formulario de Solicitud de Apoyo
 */
function createSupportForm() {
  const form = FormApp.create('Nova CoE - Solicitud de Apoyo');

  // Configuración básica
  form.setDescription('Solicite apoyo del Centro de Excelencia de IA para su proyecto');
  form.setCollectEmail(true);
  form.setRequireLogin(true);
  form.setLimitOneResponsePerUser(false);
  form.setProgressBar(true);
  form.setConfirmationMessage('Gracias por su solicitud. El equipo del CoE se pondrá en contacto dentro de las próximas 24 horas hábiles.');

  // Tipo de Solicitud
  form.addMultipleChoiceItem()
    .setTitle('Tipo de Solicitud')
    .setChoiceValues([
      'Consultoría Técnica',
      'Arquitectura de Solución',
      'Capacitación',
      'Evaluación de Modelo',
      'Soporte Nova-Cell',
      'Otro'
    ])
    .setRequired(true);

  // Nombre del Proyecto
  form.addTextItem()
    .setTitle('Nombre del Proyecto')
    .setRequired(true);

  // Descripción
  form.addParagraphTextItem()
    .setTitle('Descripción del Proyecto')
    .setHelpText('Describa brevemente su proyecto y el tipo de apoyo que necesita')
    .setRequired(true);

  // Área/Departamento
  form.addListItem()
    .setTitle('Área/Departamento')
    .setChoiceValues([
      'Banca Digital',
      'Risk Management',
      'Customer Service',
      'Operations',
      'IT/Tecnología',
      'Innovación',
      'Compliance',
      'Otro'
    ])
    .setRequired(true);

  // Urgencia
  form.addScaleItem()
    .setTitle('Urgencia')
    .setBounds(1, 5)
    .setLabels('Baja', 'Crítica')
    .setRequired(true);

  // Timeline
  form.addMultipleChoiceItem()
    .setTitle('Timeline Esperado')
    .setChoiceValues([
      'Esta semana',
      'Próximas 2 semanas',
      'Este mes',
      'Próximos 3 meses',
      'Sin urgencia específica'
    ])
    .setRequired(true);

  // Configurar notificaciones
  setupFormNotifications(form, FORMS_CONFIG["nova-coe-support"].responseEmail);

  return {
    id: form.getId(),
    url: form.getPublishedUrl(),
    editUrl: form.getEditUrl()
  };
}

/**
 * Crear formulario de Evaluación LLM
 */
function createLLMEvalForm() {
  const form = FormApp.create('Nova CoE - Evaluación de Modelos LLM');

  form.setDescription('Solicite una evaluación técnica de modelos de lenguaje para su caso de uso');
  form.setCollectEmail(true);
  form.setRequireLogin(true);
  form.setProgressBar(true);

  // Modelos a evaluar
  form.addCheckboxItem()
    .setTitle('Modelo(s) a Evaluar')
    .setChoiceValues([
      'GPT-4',
      'GPT-3.5 Turbo',
      'Claude 3',
      'Llama 2',
      'Gemini Pro',
      'Modelo Propio',
      'Otro'
    ])
    .setRequired(true);

  // Caso de uso
  form.addListItem()
    .setTitle('Caso de Uso Principal')
    .setChoiceValues([
      'Chatbot/Asistente Virtual',
      'Análisis de Documentos',
      'Generación de Contenido',
      'Clasificación de Texto',
      'Extracción de Información',
      'Traducción',
      'Resumen Automático',
      'Q&A sobre Documentos',
      'Otro'
    ])
    .setRequired(true);

  // Volumen de datos
  form.addMultipleChoiceItem()
    .setTitle('Volumen de Datos Estimado')
    .setChoiceValues([
      '< 1,000 documentos',
      '1,000 - 10,000 documentos',
      '10,000 - 100,000 documentos',
      '> 100,000 documentos'
    ])
    .setRequired(true);

  // Métricas requeridas
  form.addCheckboxItem()
    .setTitle('Métricas de Evaluación Requeridas')
    .setChoiceValues([
      'Precisión',
      'Latencia',
      'Costo por Token',
      'Seguridad/Privacy',
      'Sesgo/Fairness',
      'Explicabilidad',
      'Robustez'
    ])
    .setRequired(true);

  // Presupuesto
  form.addMultipleChoiceItem()
    .setTitle('Presupuesto Mensual Estimado (USD)')
    .setChoiceValues([
      '< $1,000',
      '$1,000 - $5,000',
      '$5,000 - $20,000',
      '> $20,000',
      'Por definir'
    ])
    .setRequired(false);

  setupFormNotifications(form, FORMS_CONFIG["nova-llm-eval"].responseEmail);

  return {
    id: form.getId(),
    url: form.getPublishedUrl(),
    editUrl: form.getEditUrl()
  };
}

/**
 * Crear formulario AISIA Assessment
 */
function createAISIAForm() {
  const form = FormApp.create('Nova CoE - Evaluación AISIA');

  form.setDescription('Evalúe la madurez de IA de su organización con el framework AISIA');
  form.setCollectEmail(true);
  form.setRequireLogin(true);
  form.setProgressBar(true);

  // Área a evaluar
  form.addTextItem()
    .setTitle('Área/Departamento a Evaluar')
    .setRequired(true);

  // Dimensiones AISIA
  const dimensions = [
    'Adopción - Nivel Actual',
    'Impacto - Beneficios Medidos',
    'Seguridad - Controles Implementados',
    'Innovación - Capacidad de Experimentación',
    'Alineación - Con Estrategia de Negocio'
  ];

  dimensions.forEach(dimension => {
    form.addScaleItem()
      .setTitle(dimension)
      .setBounds(1, 5)
      .setLabels('Muy Bajo', 'Muy Alto')
      .setRequired(true);
  });

  // Desafíos principales
  form.addCheckboxItem()
    .setTitle('Principales Desafíos')
    .setChoiceValues([
      'Falta de talento',
      'Presupuesto limitado',
      'Resistencia al cambio',
      'Restricciones regulatorias',
      'Deuda técnica',
      'Calidad de datos',
      'Seguridad/Privacy'
    ])
    .setRequired(false);

  // Comentarios adicionales
  form.addParagraphTextItem()
    .setTitle('Comentarios Adicionales')
    .setHelpText('Comparta cualquier información adicional relevante')
    .setRequired(false);

  setupFormNotifications(form, FORMS_CONFIG["nova-aisia"].responseEmail);

  return {
    id: form.getId(),
    url: form.getPublishedUrl(),
    editUrl: form.getEditUrl()
  };
}

/**
 * Crear formulario ROI Calculator
 */
function createROIForm() {
  const form = FormApp.create('Nova CoE - Calculadora ROI');

  form.setDescription('Calcule el retorno de inversión de su iniciativa de IA');
  form.setCollectEmail(true);
  form.setRequireLogin(true);
  form.setProgressBar(true);

  // Nombre del proyecto
  form.addTextItem()
    .setTitle('Nombre del Proyecto')
    .setRequired(true);

  // Costos
  form.addTextItem()
    .setTitle('Costo de Implementación Inicial (USD)')
    .setValidation(FormApp.createTextValidation()
      .requireNumberGreaterThanOrEqualTo(0)
      .build())
    .setRequired(true);

  form.addTextItem()
    .setTitle('Costo Operativo Mensual (USD)')
    .setValidation(FormApp.createTextValidation()
      .requireNumberGreaterThanOrEqualTo(0)
      .build())
    .setRequired(true);

  // Beneficios
  form.addTextItem()
    .setTitle('Ahorro Mensual Esperado (USD)')
    .setValidation(FormApp.createTextValidation()
      .requireNumberGreaterThanOrEqualTo(0)
      .build())
    .setRequired(true);

  form.addTextItem()
    .setTitle('Incremento de Ingresos Mensual (USD)')
    .setHelpText('Opcional: ingresos adicionales generados')
    .setValidation(FormApp.createTextValidation()
      .requireNumberGreaterThanOrEqualTo(0)
      .build())
    .setRequired(false);

  // Impacto
  form.addTextItem()
    .setTitle('Número de Usuarios/Clientes Impactados')
    .setValidation(FormApp.createTextValidation()
      .requireNumberGreaterThanOrEqualTo(1)
      .build())
    .setRequired(true);

  // Timeline
  form.addTextItem()
    .setTitle('Tiempo de Implementación (meses)')
    .setValidation(FormApp.createTextValidation()
      .requireNumberBetween(1, 36)
      .build())
    .setRequired(true);

  // Beneficios no monetarios
  form.addCheckboxItem()
    .setTitle('Beneficios No Monetarios')
    .setChoiceValues([
      'Mejora en satisfacción del cliente',
      'Reducción de errores',
      'Mayor velocidad de procesamiento',
      'Mejor cumplimiento regulatorio',
      'Innovación en productos',
      'Ventaja competitiva'
    ])
    .setRequired(false);

  setupFormNotifications(form, FORMS_CONFIG["nova-roi"].responseEmail);

  return {
    id: form.getId(),
    url: form.getPublishedUrl(),
    editUrl: form.getEditUrl()
  };
}

/**
 * Crear formulario Intake
 */
function createIntakeForm() {
  const form = FormApp.create('Nova CoE - Registro de Proyecto IA');

  form.setDescription('Registre su proyecto de IA para obtener apoyo del CoE');
  form.setCollectEmail(true);
  form.setRequireLogin(true);
  form.setProgressBar(true);

  // Nombre del proyecto
  form.addTextItem()
    .setTitle('Nombre del Proyecto')
    .setRequired(true);

  // Etapa actual
  form.addMultipleChoiceItem()
    .setTitle('Etapa Actual del Proyecto')
    .setChoiceValues([
      '1. Explorar - Identificando oportunidades',
      '2. Experimentar - Proof of Concept',
      '3. Construir - Desarrollo activo',
      '4. Validar - Testing y QA',
      '5. Desplegar - Implementación',
      '6. Escalar - Expansión'
    ])
    .setRequired(true);

  // Objetivo
  form.addParagraphTextItem()
    .setTitle('Objetivo Principal')
    .setHelpText('Describa el objetivo principal y el impacto esperado')
    .setRequired(true);

  // Tecnologías
  form.addCheckboxItem()
    .setTitle('Tecnologías de IA a Utilizar')
    .setChoiceValues([
      'LLMs/GenAI',
      'Computer Vision',
      'NLP Clásico',
      'Machine Learning',
      'Deep Learning',
      'Robotic Process Automation',
      'Speech Recognition',
      'Otro'
    ])
    .setRequired(true);

  // Nova-Cell
  const novaCellItem = form.addMultipleChoiceItem();
  novaCellItem.setTitle('¿Requiere acceso a Nova-Cell?')
    .setChoiceValues(['Sí', 'No', 'No estoy seguro'])
    .setRequired(true);

  // Equipo
  form.addParagraphTextItem()
    .setTitle('Equipo del Proyecto')
    .setHelpText('Liste los nombres y roles de los miembros del equipo')
    .setRequired(true);

  setupFormNotifications(form, FORMS_CONFIG["nova-intake"].responseEmail);

  return {
    id: form.getId(),
    url: form.getPublishedUrl(),
    editUrl: form.getEditUrl()
  };
}

/**
 * Configurar notificaciones por email para el formulario
 */
function setupFormNotifications(form, emailAddress) {
  try {
    // Crear trigger para enviar notificación al equipo CoE
    ScriptApp.newTrigger('sendFormNotification')
      .forForm(form)
      .onFormSubmit()
      .create();

    // Guardar email de notificación en propiedades
    PropertiesService.getScriptProperties()
      .setProperty(form.getId() + '_notify', emailAddress);

  } catch (e) {
    Logger.log('Error configurando notificaciones: ' + e);
  }
}

/**
 * Función para enviar notificaciones
 */
function sendFormNotification(e) {
  const formId = e.source.getId();
  const emailAddress = PropertiesService.getScriptProperties()
    .getProperty(formId + '_notify');

  if (!emailAddress) return;

  const form = FormApp.openById(formId);
  const response = e.response;
  const respondentEmail = response.getRespondentEmail();

  // Construir mensaje
  let message = `Nueva respuesta en: ${form.getTitle()}\n\n`;
  message += `De: ${respondentEmail}\n`;
  message += `Fecha: ${new Date()}\n\n`;
  message += `Respuestas:\n`;

  const itemResponses = response.getItemResponses();
  itemResponses.forEach(itemResponse => {
    message += `${itemResponse.getItem().getTitle()}: ${itemResponse.getResponse()}\n`;
  });

  // Enviar email
  MailApp.sendEmail({
    to: emailAddress,
    subject: `[Nova CoE] Nueva respuesta: ${form.getTitle()}`,
    body: message
  });
}

/**
 * Guardar URLs de formularios en una hoja de cálculo
 */
function saveFormURLs(results) {
  // Crear nueva hoja de cálculo
  const spreadsheet = SpreadsheetApp.create('Nova CoE - URLs de Formularios');
  const sheet = spreadsheet.getActiveSheet();

  // Encabezados
  sheet.getRange(1, 1, 1, 5).setValues([
    ['Form ID', 'Título', 'URL Publicada', 'URL de Edición', 'Embed Code']
  ]);

  // Datos
  let row = 2;
  for (const [key, value] of Object.entries(results)) {
    const config = FORMS_CONFIG[key];
    const embedCode = `<iframe src="${value.url}?embedded=true" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Cargando...</iframe>`;

    sheet.getRange(row, 1, 1, 5).setValues([
      [key, config.title, value.url, value.editUrl, embedCode]
    ]);
    row++;
  }

  // Formato
  sheet.getRange(1, 1, 1, 5).setFontWeight('bold');
  sheet.setFrozenRows(1);
  sheet.autoResizeColumns(1, 5);

  Logger.log('Hoja de cálculo creada: ' + spreadsheet.getUrl());

  return spreadsheet.getUrl();
}

/**
 * Función para obtener las URLs de los formularios existentes
 */
function getFormURLs() {
  const forms = DriveApp.getFilesByType(MimeType.GOOGLE_FORMS);
  const results = {};

  while (forms.hasNext()) {
    const file = forms.next();
    const name = file.getName();

    // Buscar formularios del CoE
    if (name.startsWith('Nova CoE')) {
      const form = FormApp.openById(file.getId());
      results[name] = {
        id: form.getId(),
        url: form.getPublishedUrl(),
        editUrl: form.getEditUrl(),
        embedCode: `<iframe src="${form.getPublishedUrl()}?embedded=true" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Cargando...</iframe>`
      };
    }
  }

  Logger.log(results);
  return results;
}