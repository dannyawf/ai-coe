---
title: Herramienta de Evaluación de Impacto de Sistemas de IA (AISIA)
tags:
  - herramientas
  - evaluación
  - riesgos
  - compliance
search:
  boost: 3
---

# Herramienta de Evaluación de Impacto de Sistemas de IA (AISIA)

<div class="nova-card">
  <div class="nova-accent-border">
    <h2>🎯 Evaluación Obligatoria para Sistemas de IA</h2>
    <p>Esta herramienta es un requisito obligatorio según la <strong>Política de Uso Responsable de IA</strong> para todos los nuevos sistemas de IA antes de su desarrollo. Su propósito es identificar, analizar y mitigar los riesgos potenciales asociados a un sistema de IA, garantizando el cumplimiento regulatorio y ético.</p>
  </div>
</div>

## 📊 Herramienta Interactiva AISIA

<div style="background-color: #f4f7f9; padding: 30px; border-radius: 12px; margin: 20px 0;">
  <iframe srcdoc='<!DOCTYPE html>
<html lang="es-MX">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Herramienta de Evaluación de Impacto de Sistemas de IA (AISIA)</title>
    <style>
        :root {
            --primary-color: #005587;
            --secondary-color: #0096d6;
            --accent-color: #f5a623;
            --background-color: #f4f7f9;
            --text-color: #333;
            --border-color: #dce3e8;
            --card-bg: #ffffff;
            --success-color: #28a745;
            --warning-color: #ffc107;
            --danger-color: #dc3545;
            --font-family: "Arial", sans-serif;
        }

        body {
            font-family: var(--font-family);
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: auto;
            background: var(--card-bg);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }

        h1, h2, h3, h4 {
            color: var(--primary-color);
            margin-top: 0;
        }

        h1 {
            font-size: 2.2rem;
            border-bottom: 3px solid var(--primary-color);
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        
        h2 {
            font-size: 1.8rem;
            margin-top: 40px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }
        
        h3 {
            font-size: 1.4rem;
            color: var(--secondary-color);
            margin-top: 30px;
        }

        .form-section {
            margin-bottom: 30px;
            padding: 20px;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background-color: #fafcff;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 8px;
            font-size: 1.1rem;
        }

        input[type="text"],
        input[type="date"],
        textarea,
        select {
            width: 100%;
            padding: 12px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        input[type="text"]:focus,
        textarea:focus,
        select:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 5px rgba(0, 85, 135, 0.2);
        }

        textarea {
            resize: vertical;
            min-height: 120px;
        }
        
        small {
            display: block;
            color: #6c757d;
            margin-top: 5px;
        }

        .question-group {
            margin-bottom: 15px;
            padding: 15px;
            border-left: 4px solid var(--border-color);
            background-color: var(--card-bg);
        }
        
        .question-group:hover {
            border-left-color: var(--secondary-color);
        }

        .question-group label {
            font-weight: normal;
            font-size: 1rem;
        }
        
        .question-group input[type="radio"],
        .question-group input[type="checkbox"] {
            margin-right: 10px;
        }

        .btn {
            background-color: var(--primary-color);
            color: white;
            padding: 15px 25px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1.2rem;
            font-weight: bold;
            transition: background-color 0.3s;
            display: block;
            width: 100%;
            margin-top: 20px;
        }

        .btn:hover {
            background-color: #003f6b;
        }

        #dashboard {
            display: none;
            padding: 30px;
            margin-top: 40px;
            border: 2px solid var(--primary-color);
            border-radius: 12px;
            background-color: #f0f8ff;
        }
        
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        
        .dashboard-metric {
            background: var(--card-bg);
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        
        .dashboard-metric h4 {
            margin: 0 0 10px 0;
            color: var(--secondary-color);
        }
        
        .dashboard-metric .value {
            font-size: 2.5rem;
            font-weight: bold;
        }
        
        .risk-badge {
            padding: 8px 15px;
            border-radius: 20px;
            color: white;
            font-weight: bold;
            font-size: 1.5rem;
            display: inline-block;
        }
        
        .risk-bajo { background-color: var(--success-color); }
        .risk-limitado { background-color: var(--warning-color); color: #333; }
        .risk-alto { background-color: var(--accent-color); color: #333; }
        .risk-inaceptable { background-color: var(--danger-color); }

        .recommendations ul {
            list-style-type: "✅ ";
            padding-left: 20px;
        }
        .recommendations li {
            margin-bottom: 10px;
        }
        
        .critical-note {
            background-color: #fff3cd;
            border: 1px solid #ffeeba;
            color: #856404;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>🏛️ Herramienta de Evaluación de Impacto de Sistemas de IA (AISIA)</h1>
        <p>Esta herramienta es un requisito obligatorio según la <strong>Política de Uso Responsable de IA</strong> para todos los nuevos sistemas de IA antes de su desarrollo. Su propósito es identificar, analizar y mitigar los riesgos potenciales asociados a un sistema de IA, garantizando el cumplimiento regulatorio y ético. El resultado de esta evaluación determinará la ruta a seguir en el <strong>PROC-GOV-001: Procedimiento de Validación de Modelos</strong>.</p>
        
        <form id="aisiaForm">
            <!-- SECCIÓN 1: FORMULARIO DE EVALUACIÓN INICIAL -->
            <div class="form-section">
                <h2>1. Formulario de Evaluación Inicial</h2>
                <div class="form-group">
                    <label for="aiSystemName">Nombre del Sistema de IA</label>
                    <input type="text" id="aiSystemName" name="aiSystemName" placeholder="Ej: Modelo de Scoring para Crédito de Consumo v2.1" required>
                </div>
                <div class="form-group">
                    <label for="purpose">Propósito y Alcance del Sistema</label>
                    <textarea id="purpose" name="purpose" placeholder="Ej: El sistema tiene como objetivo predecir la probabilidad de incumplimiento de pago para nuevos solicitantes de tarjetas de crédito. Se utilizará en el proceso de originación para automatizar la decisión de aprobación/rechazo para solicitudes de bajo monto (<$50,000 MXN) y como recomendación para montos superiores." required></textarea>
                    <small>Describa el problema de negocio que resuelve y los límites de su aplicación.</small>
                </div>
                <div class="form-group">
                    <label for="stakeholders">Stakeholders Involucrados</label>
                    <input type="text" id="stakeholders" name="stakeholders" placeholder="Ej: Product Owner (Tarjetas de Crédito), Risk Officer (Riesgo Crediticio), Data Science Team, Cumplimiento Normativo" required>
                    <small>Liste los roles y áreas clave que participan o son impactados por el sistema.</small>
                </div>
                <div class="form-group">
                    <label for="dataUsed">Datos Utilizados</label>
                    <textarea id="dataUsed" name="dataUsed" placeholder="Ej: Datos sociodemográficos del cliente (edad, estado civil, etc.), historial crediticio interno y de buró, ingresos comprobados, datos transaccionales de cuentas del banco. No se utilizan datos sensibles como origen étnico, religión o preferencias políticas." required></textarea>
                    <small>Describa las categorías de datos para entrenamiento y operación, indicando si se usan datos personales o sensibles según la LFPDPPP.</small>
                </div>
            </div>

            <!-- SECCIÓN 2: MATRIZ DE CLASIFICACIÓN DE RIESGO -->
            <div class="form-section" id="riskMatrix">
                <h2>2. Matriz de Clasificación de Riesgo</h2>
                <p>Responda las siguientes preguntas para calcular automáticamente el nivel de riesgo del sistema. Este cálculo se basa en los criterios del EU AI Act, la regulación bancaria mexicana (CNBV) y el impacto en derechos fundamentales.</p>

                <h3>2.1 Criterios de Riesgo Inaceptable (Basado en EU AI Act)</h3>
                <div class="question-group">
                    <label>¿El sistema utiliza técnicas subliminales o manipuladoras que puedan causar daño físico o psicológico?</label>
                    <input type="radio" name="unacceptable1" value="yes" data-score="100"> Sí
                    <input type="radio" name="unacceptable1" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿El sistema explota vulnerabilidades de grupos específicos (edad, discapacidad) para distorsionar su comportamiento de manera perjudicial?</label>
                    <input type="radio" name="unacceptable2" value="yes" data-score="100"> Sí
                    <input type="radio" name="unacceptable2" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿El sistema realiza "social scoring" o calificación social de personas que pueda conducir a un tratamiento perjudicial o desfavorable en contextos no relacionados?</label>
                    <input type="radio" name="unacceptable3" value="yes" data-score="100"> Sí
                    <input type="radio" name="unacceptable3" value="no" data-score="0" checked> No
                </div>

                <h3>2.2 Criterios de Alto Riesgo (CNBV y Casos de Uso Bancarios Críticos)</h3>
                <div class="question-group">
                    <label>¿El sistema toma decisiones o es un componente clave en la determinación del acceso a productos de crédito (originación, scoring, fijación de precios)?</label>
                    <input type="radio" name="highrisk1" value="yes" data-score="30"> Sí
                    <input type="radio" name="highrisk1" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿El sistema se utiliza para la prevención, detección o investigación de lavado de dinero (AML/PLD) o financiamiento al terrorismo?</label>
                    <input type="radio" name="highrisk2" value="yes" data-score="25"> Sí
                    <input type="radio" name="highrisk2" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿El sistema se utiliza para procesos de identificación y conocimiento del cliente (KYC)?</label>
                    <input type="radio" name="highrisk3" value="yes" data-score="20"> Sí
                    <input type="radio" name="highrisk3" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿El sistema toma decisiones sobre el acceso a empleo, gestión de personal o terminación de relaciones laborales dentro del banco?</label>
                    <input type="radio" name="highrisk4" value="yes" data-score="25"> Sí
                    <input type="radio" name="highrisk4" value="no" data-score="0" checked> No
                </div>
                 <div class="question-group">
                    <label>¿El sistema determina el acceso a servicios públicos o privados esenciales (ej. seguros, fianzas)?</label>
                    <input type="radio" name="highrisk5" value="yes" data-score="20"> Sí
                    <input type="radio" name="highrisk5" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿El sistema realiza trading algorítmico o gestiona inversiones de forma automatizada?</label>
                    <input type="radio" name="highrisk6" value="yes" data-score="30"> Sí
                    <input type="radio" name="highrisk6" value="no" data-score="0" checked> No
                </div>

                <h3>2.3 Evaluación de Impacto en Derechos y Privacidad (LFPDPPP)</h3>
                <div class="question-group">
                    <label>¿El sistema procesa datos personales sensibles (salud, biométricos, ideología, etc.)?</label>
                    <input type="radio" name="impact1" value="yes" data-score="20"> Sí
                    <input type="radio" name="impact1" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿Las decisiones del sistema son completamente automatizadas y tienen un efecto legal o significativo en las personas (ej. rechazo de un servicio)?</label>
                    <input type="radio" name="impact2" value="yes" data-score="15"> Sí
                    <input type="radio" name="impact2" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿Es difícil o imposible para un cliente apelar o solicitar una revisión humana de una decisión tomada por el sistema?</label>
                    <input type="radio" name="impact3" value="yes" data-score="15"> Sí
                    <input type="radio" name="impact3" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿El sistema podría generar o amplificar sesgos discriminatorios contra grupos protegidos?</label>
                    <input type="radio" name="impact4" value="yes" data-score="25"> Sí
                    <input type="radio" name="impact4" value="no" data-score="0" checked> No
                </div>

                <h3>2.4 Criterios de Riesgo Limitado y Mínimo</h3>
                 <div class="question-group">
                    <label>¿El sistema interactúa directamente con los clientes (ej. chatbot, sistema de recomendación) sin tomar decisiones críticas?</label>
                    <input type="radio" name="limited1" value="yes" data-score="10"> Sí
                    <input type="radio" name="limited1" value="no" data-score="0" checked> No
                </div>
                <div class="question-group">
                    <label>¿El sistema automatiza procesos internos de back-office que no tienen impacto directo en clientes (ej. clasificación de documentos, optimización de rutas)?</label>
                    <input type="radio" name="limited2" value="yes" data-score="5"> Sí
                    <input type="radio" name="limited2" value="no" data-score="0" checked> No
                </div>
                 <div class="question-group">
                    <label>¿El sistema se utiliza como herramienta de asistencia para un humano que toma la decisión final (ej. asistente de codificación, generador de resúmenes)?</label>
                    <input type="radio" name="limited3" value="yes" data-score="5"> Sí
                    <input type="radio" name="limited3" value="no" data-score="0" checked> No
                </div>
            </div>

            <!-- SECCIÓN 3: EVALUACIÓN DE IMPACTO DETALLADA -->
            <div class="form-section">
                <h2>3. Evaluación de Impacto Detallada</h2>
                <h3>Impacto en Clientes y Empleados</h3>
                <div class="form-group">
                    <label for="impact_clients">¿Cómo podría afectar este sistema a los clientes de manera positiva y negativa?</label>
                    <textarea id="impact_clients" name="impact_clients" placeholder="Positivo: decisiones de crédito más rápidas y accesibles. Negativo: posibles rechazos incorrectos, falta de transparencia en la decisión, perpetuación de sesgos históricos."></textarea>
                </div>
                <h3>Riesgos de Discriminación y Sesgo</h3>
                <div class="form-group">
                    <label for="impact_bias">¿Qué grupos demográficos podrían verse afectados de manera desproporcionada y cómo se planea medir y mitigar este riesgo?</label>
                    <textarea id="impact_bias" name="impact_bias" placeholder="Ej: Mujeres, jóvenes, residentes de ciertas zonas geográficas. Se medirá la paridad demográfica y la igualdad de oportunidades en las tasas de aprobación. Se utilizarán técnicas como re-weighting y adversarial debiasing."></textarea>
                </div>
                <h3>Transparencia y Explicabilidad</h3>
                <div class="form-group">
                    <label for="impact_explainability">¿Cómo se explicarán las decisiones del sistema a los clientes, empleados y reguladores?</label>
                    <textarea id="impact_explainability" name="impact_explainability" placeholder="Ej: Se utilizarán SHAP values para generar explicaciones locales para cada decisión. Se prepararán resúmenes en lenguaje natural para los clientes afectados, indicando los 3 principales factores de la decisión, según lo exige la LFPDPPP."></textarea>
                </div>
                <h3>Seguridad y Robustez</h3>
                <div class="form-group">
                    <label for="impact_security">¿Cuáles son los principales riesgos de seguridad (ataques adversarios, envenenamiento de datos) y cuál es el plan de contingencia ante una falla del sistema?</label>
                    <textarea id="impact_security" name="impact_security" placeholder="Riesgos: manipulación de datos de entrada para obtener un crédito indebido. Plan de contingencia: monitoreo de drift, alertas automáticas y un kill switch que revierte al proceso manual si las métricas de performance caen por debajo del 95% del baseline."></textarea>
                </div>
            </div>
            
            <!-- SECCIÓN 4: CONTROLES Y MITIGACIONES -->
            <div class="form-section">
                <h2>4. Controles y Mitigaciones Propuestos</h2>
                <p>Marque los controles que planea implementar. Esto es un plan inicial que será validado por la segunda línea de defensa.</p>
                
                <h3>Controles Técnicos</h3>
                <div class="form-group">
                    <input type="checkbox" id="ctrl_tech1" name="ctrl_tech1"> <label for="ctrl_tech1">Monitoreo continuo de métricas de desempeño y sesgo (ISO 23894).</label><br>
                    <input type="checkbox" id="ctrl_tech2" name="ctrl_tech2"> <label for="ctrl_tech2">Implementación de herramientas de explicabilidad (SHAP, LIME).</label><br>
                    <input type="checkbox" id="ctrl_tech3" name="ctrl_tech3"> <label for="ctrl_tech3">Pruebas de robustez y ataques adversarios.</label><br>
                    <input type="checkbox" id="ctrl_tech4" name="ctrl_tech4"> <label for="ctrl_tech4">Encriptación de datos en tránsito y en reposo.</label><br>
                </div>

                <h3>Salvaguardas Operacionales</h3>
                <div class="form-group">
                    <input type="checkbox" id="ctrl_op1" name="ctrl_op1"> <label for="ctrl_op1">Supervisión humana obligatoria para decisiones críticas (Nivel 3 o 4).</label><br>
                    <input type="checkbox" id="ctrl_op2" name="ctrl_op2"> <label for="ctrl_op2">Proceso claro de apelación y revisión humana para clientes.</label><br>
                    <input type="checkbox" id="ctrl_op3" name="ctrl_op3"> <label for="ctrl_op3">Plan de contingencia y rollback documentado y probado.</label><br>
                    <input type="checkbox" id="ctrl_op4" name="ctrl_op4"> <label for="ctrl_op4">Capacitación específica para los usuarios finales del sistema.</label><br>
                </div>

                <h3>Requisitos de Documentación (ISO 42001)</h3>
                <div class="form-group">
                    <input type="checkbox" id="ctrl_doc1" name="ctrl_doc1"> <label for="ctrl_doc1">Creación de una "Model Card" detallada.</label><br>
                    <input type="checkbox" id="ctrl_doc2" name="ctrl_doc2"> <label for="ctrl_doc2">Documentación completa de la fuente de datos y preprocesamiento.</label><br>
                    <input type="checkbox" id="ctrl_doc3" name="ctrl_doc3"> <label for="ctrl_doc3">Registro de logs inmutables para cada decisión del modelo.</label><br>
                </div>
            </div>

            <button type="button" class="btn" onclick="calculateAndShowResults()">Calcular Riesgo y Generar Dashboard</button>
        </form>

        <!-- SECCIÓN 5: DASHBOARD DE RESULTADOS -->
        <div id="dashboard">
            <h2>5. Dashboard de Resultados AISIA</h2>
            <div class="dashboard-grid">
                <div class="dashboard-metric">
                    <h4>Score de Riesgo AISIA</h4>
                    <div class="value" id="riskScore">0</div>
                </div>
                <div class="dashboard-metric">
                    <h4>Nivel de Riesgo Asignado</h4>
                    <div class="value">
                        <span id="riskLevel" class="risk-badge">N/A</span>
                    </div>
                </div>
            </div>
            
            <div id="recommendations" style="margin-top: 30px;">
                <h3>Recomendaciones y Próximos Pasos</h3>
                <div id="recommendations-content"></div>
            </div>

            <div class="critical-note">
                <h4>Flujo de Aprobación Requerido</h4>
                <p>El nivel de riesgo asignado determina el proceso de validación y aprobación. Consulte el diagrama para entender la ruta que seguirá su proyecto.</p>
            </div>
             <div class="critical-note" style="margin-top:20px;">
                <h4>Alineación con Frameworks</h4>
                <p>Este sistema, una vez aprobado, será monitoreado continuamente a través del <strong>Framework IMPACT</strong> del CoE. La documentación generada servirá como base para las auditorías de cumplimiento con <strong>ISO/IEC 42001</strong> y la <strong>regulación de la CNBV</strong>.</p>
            </div>
        </div>
    </div>

    <script>
        function calculateRiskScore() {
            let totalScore = 0;
            const form = document.getElementById("aisiaForm");
            const checkedInputs = form.querySelectorAll("#riskMatrix input:checked");
            
            checkedInputs.forEach(input => {
                const score = parseInt(input.dataset.score, 10);
                if (!isNaN(score)) {
                    totalScore += score;
                }
            });
            
            return totalScore;
        }

        function calculateAndShowResults() {
            const score = calculateRiskScore();
            let level = "";
            let levelClass = "";
            let recommendations = "";

            if (score >= 100) {
                level = "Inaceptable";
                levelClass = "risk-inaceptable";
                recommendations = `
                    <p><strong>Acción Requerida:</strong> El proyecto se clasifica como de Riesgo Inaceptable según la Política de Uso Responsable de IA.</p>
                    <ul>
                        <li>Este caso de uso está <strong>PROHIBIDO</strong> y no puede continuar.</li>
                        <li>Contacte inmediatamente al CoE de IA y a Compliance para discutir la redefinición fundamental del proyecto.</li>
                        <li>Ref: Política de Uso Responsable de IA, Sección 5.1 - Prohibiciones Absolutas.</li>
                    </ul>`;
            } else if (score >= 40) {
                level = "Alto";
                levelClass = "risk-alto";
                recommendations = `
                    <p><strong>Acción Requerida:</strong> El proyecto se clasifica como de Alto Riesgo y requiere el máximo nivel de escrutinio.</p>
                    <ul>
                        <li>Se debe seguir la <strong>ruta de validación exhaustiva</strong> del procedimiento PROC-GOV-001.</li>
                        <li>La aprobación final es competencia del <strong>Comité de IA</strong>.</li>
                        <li>Se requiere un análisis independiente de sesgo y pruebas de estrés.</li>
                        <li>Es mandatorio un plan de explicabilidad para reguladores y un dictamen legal.</li>
                        <li>Todos los controles técnicos, operacionales y de documentación deben ser implementados.</li>
                    </ul>`;
            } else if (score >= 15) {
                level = "Limitado";
                levelClass = "risk-limitado";
                recommendations = `
                    <p><strong>Acción Requerida:</strong> El proyecto se clasifica como de Riesgo Limitado/Medio.</p>
                    <ul>
                        <li>Se debe seguir la <strong>ruta de validación estándar</strong> del procedimiento PROC-GOV-001.</li>
                        <li>La aprobación final es competencia del <strong>CoE de IA</strong> y el Risk Officer asignado.</li>
                        <li>Se requieren controles de transparencia claros para los usuarios (ej. notificar que interactúan con una IA).</li>
                        <li>La documentación técnica (Model Card) es obligatoria.</li>
                    </ul>`;
            } else {
                level = "Bajo";
                levelClass = "risk-bajo";
                recommendations = `
                    <p><strong>Acción Requerida:</strong> El proyecto se clasifica como de Riesgo Bajo/Mínimo.</p>
                    <ul>
                        <li>El proceso de aprobación es simplificado.</li>
                        <li>El sistema debe ser registrado en el inventario de modelos de IA.</li>
                        <li>Aunque el riesgo es bajo, debe cumplir con todas las políticas corporativas de seguridad y datos.</li>
                        <li>Se requiere documentación técnica básica.</li>
                    </ul>`;
            }

            document.getElementById("riskScore").innerText = score;
            const riskLevelElement = document.getElementById("riskLevel");
            riskLevelElement.innerText = level;
            riskLevelElement.className = "risk-badge " + levelClass;
            document.getElementById("recommendations-content").innerHTML = recommendations;

            const dashboard = document.getElementById("dashboard");
            dashboard.style.display = "block";
            dashboard.scrollIntoView({ behavior: "smooth" });
        }

        // Add live calculation feedback
        document.querySelectorAll("#riskMatrix input").forEach(input => {
            input.addEventListener("change", () => {
                const score = calculateRiskScore();
                console.log("Current score:", score);
            });
        });
    </script>

</body>
</html>' width="100%" height="2400" style="border: none; border-radius: 8px;">
  </iframe>
</div>

## 🔄 Flujo de Aprobación según Nivel de Riesgo

```mermaid
graph TD
    A[Inicio: AISIA Completada] --> B{Nivel de Riesgo?}
    B -- Inaceptable --> C[PROYECTO RECHAZADO]
    B -- Alto/Crítico --> D[Validación Exhaustiva PROC-GOV-001<br>Requiere aprobación del Comité de IA]
    B -- Limitado/Medio --> E[Validación Estándar PROC-GOV-001<br>Requiere aprobación del CoE IA]
    B -- Bajo/Mínimo --> F[Registro y Monitoreo Simplificado<br>Aprobación automática con registro]
    D --> G[Implementación en Producción]
    E --> G
    F --> G
```

## 📋 Guía de Uso de la Herramienta

### 1. Cuándo Usar AISIA

!!! warning "Obligatorio para Todos los Nuevos Sistemas"
    Esta evaluación es **mandatoria** antes de iniciar el desarrollo de cualquier sistema de IA según la Política de Uso Responsable de IA, sin importar su complejidad aparente.

### 2. Quién Debe Completar AISIA

- **Product Owner**: Responsable principal de completar la evaluación
- **Risk Officer**: Revisión y validación de la evaluación
- **Data Scientist/ML Engineer**: Soporte técnico para las secciones de arquitectura
- **Compliance Officer**: Validación de cumplimiento regulatorio

### 3. Proceso Paso a Paso

1. **Preparación**: Recopile toda la información sobre el sistema propuesto
2. **Completar Formulario**: Llene todas las secciones de la herramienta
3. **Calcular Riesgo**: Use el botón para obtener la clasificación automática
4. **Documentar Resultados**: Guarde el PDF del resultado para el expediente
5. **Iniciar Validación**: Proceda según el nivel de riesgo asignado

## 📊 Interpretación de Resultados

### Niveles de Riesgo y Acciones

| Nivel | Score | Acción Requerida | Aprobador |
|-------|-------|------------------|-----------|
| **Inaceptable** | ≥100 | Proyecto prohibido, requiere redefinición | N/A - Rechazado |
| **Alto** | 40-99 | Validación exhaustiva PROC-GOV-001 | Comité de IA |
| **Limitado** | 15-39 | Validación estándar PROC-GOV-001 | CoE IA + Risk Officer |
| **Bajo** | <15 | Registro simplificado | Automático con registro |

## 🔗 Integración con Otros Procesos

### Conexión con PROC-GOV-001

La herramienta AISIA es el punto de entrada al procedimiento de validación de modelos:

```mermaid
graph LR
    A[AISIA Assessment] --> B[Clasificación de Riesgo]
    B --> C{Ruta de Validación}
    C --> D[Track Simplificado]
    C --> E[Track Estándar]
    C --> F[Track Exhaustivo]
    D --> G[Producción]
    E --> G
    F --> G
```

### Alineación con Framework IMPACT

Los resultados de AISIA alimentan directamente las métricas del Framework IMPACT:

- **Implementation**: Tiempo desde AISIA hasta producción
- **Momentum**: Número de sistemas evaluados mensualmente
- **Performance**: Precisión en la clasificación de riesgo
- **Acceptance**: Tasa de aprobación post-AISIA
- **Cost-Effective**: ROI de los controles implementados
- **Trust**: Cumplimiento con regulaciones

## 📚 Referencias y Normativa

### Estándares Internacionales
- **ISO/IEC 23053**: Framework para ML
- **ISO/IEC 23894**: Gestión de riesgos en IA
- **ISO/IEC 42001**: Sistema de gestión de IA

### Regulación Aplicable
- **EU AI Act**: Clasificación de riesgos
- **CNBV**: Circular Única de Bancos
- **LFPDPPP**: Protección de datos personales

## 🆘 Soporte y Contacto

Para dudas sobre el uso de la herramienta AISIA:

- **Email**: aisia-support@banco.mx
- **Teams**: Canal #aisia-evaluaciones
- **Wiki**: wiki.banco.mx/aisia
- **Helpdesk CoE**: Ext. 4242

---

*Herramienta AISIA v2.0 | Centro de Excelencia de IA | Última actualización: 09 de enero de 2025*