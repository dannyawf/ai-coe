---
title: AI Opportunity Radar Tool
tags:
  - herramientas
  - estrategia
  - evaluación
  - innovación
search:
  boost: 3
---

# AI Opportunity Radar Tool - Identificación y Priorización Estratégica

<div class="nova-card">
  <div class="nova-accent-border">
    <h2>🚀 Radar de Oportunidades de IA para Banca</h2>
    <p>Herramienta visual e interactiva para identificar, evaluar y priorizar oportunidades de IA estratégicas, con análisis multidimensional y alineación con el Framework IMPACT del CoE.</p>
  </div>
</div>

## 📊 Herramienta Interactiva de Evaluación

<div style="background-color: #f4f7f9; padding: 30px; border-radius: 12px; margin: 20px 0;">
  <iframe srcdoc='<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Opportunity Radar Tool - Banco Nova</title>
    <!-- Chart.js CDN for interactive charts -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.0.0"></script>
    <style>
        /* Basic styling for readability and layout */
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f7f6;
            color: #333;
            line-height: 1.6;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        }
        h1, h2, h3 {
            color: #0056b3;
            border-bottom: 2px solid #e0e7eb;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        h1 {
            text-align: center;
            color: #004085;
            font-size: 2.5em;
            margin-bottom: 20px;
            border-bottom: none;
        }
        .section {
            margin-bottom: 40px;
            padding: 20px;
            background-color: #fdfdfd;
            border-radius: 6px;
            border: 1px solid #e0e7eb;
        }
        .form-group {
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .form-group label {
            flex: 0 0 200px; /* Fixed width for labels */
            font-weight: bold;
            color: #555;
        }
        .form-group input[type="range"] {
            flex-grow: 1;
            width: auto;
            -webkit-appearance: none;
            height: 8px;
            border-radius: 5px;
            background: #d3d3d3;
            outline: none;
            opacity: 0.7;
            transition: opacity .2s;
        }
        .form-group input[type="range"]:hover {
            opacity: 1;
        }
        .form-group input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #007bff;
            cursor: pointer;
        }
        .form-group input[type="range"]::-moz-range-thumb {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #007bff;
            cursor: pointer;
        }
        .form-group input[type="number"] {
            width: 70px;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            text-align: center;
        }
        .form-group input[type="text"] {
            flex-grow: 1;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-group span.score-display {
            min-width: 30px;
            text-align: center;
            font-weight: bold;
            color: #007bff;
        }
        .button-group {
            margin-top: 25px;
            text-align: right;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
            margin-left: 10px;
        }
        button:hover {
            background-color: #0056b3;
        }
        button:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }
        .select-group {
            margin-bottom: 20px;
        }
        .select-group label {
            font-weight: bold;
            margin-right: 10px;
        }
        select {
            padding: 8px 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 1rem;
            min-width: 250px;
        }
        .chart-container {
            width: 100%;
            max-width: 800px;
            margin: 20px auto;
            position: relative;
        }
        .summary-box {
            background-color: #e9f7fe;
            border-left: 5px solid #007bff;
            padding: 15px 20px;
            margin-top: 20px;
            border-radius: 4px;
        }
        .summary-box p {
            margin: 5px 0;
        }
        .summary-box strong {
            color: #0056b3;
        }
        .grid-2-col {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }
        .grid-3-col {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 20px;
        }
        .card {
            background-color: #fdfdfd;
            border: 1px solid #e0e7eb;
            border-radius: 6px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .card h4 {
            color: #0056b3;
            margin-top: 0;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        .recommendation-list {
            list-style-type: disc;
            padding-left: 20px;
        }
        .recommendation-list li {
            margin-bottom: 8px;
            color: #444;
        }
        .badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 4px;
            font-weight: bold;
            font-size: 0.9em;
            margin-left: 10px;
        }
        .badge-quick-win { background-color: #28a745; color: white; }
        .badge-strategic { background-color: #007bff; color: white; }
        .badge-transform { background-color: #ffc107; color: #333; }
        .badge-experimental { background-color: #6c757d; color: white; }
        .matrix-item {
            padding: 10px;
            border: 1px solid #eee;
            text-align: center;
            background-color: #f8f8f8;
            border-radius: 4px;
            margin-bottom: 5px;
        }
        .matrix-header {
            font-weight: bold;
            background-color: #e0e7eb;
            padding: 10px;
            text-align: center;
            border-radius: 4px;
        }
        .prioritization-matrix {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            grid-template-rows: auto auto auto;
            gap: 5px;
            margin-top: 20px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        .prioritization-matrix .cell {
            padding: 10px;
            border: 1px solid #ddd;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 80px;
            font-size: 0.9em;
            background-color: #fefefe;
        }
        .prioritization-matrix .cell.header {
            font-weight: bold;
            background-color: #e9ecef;
            color: #333;
        }
        .prioritization-matrix .cell.y-axis-label {
            background-color: #f2f2f2;
            font-weight: bold;
            writing-mode: vertical-lr;
            text-orientation: mixed;
            transform: rotate(180deg);
            padding: 10px 5px;
        }
        .prioritization-matrix .cell.x-axis-label {
            background-color: #f2f2f2;
            font-weight: bold;
            padding: 5px 10px;
        }
        .prioritization-matrix .cell.empty {
            background-color: transparent;
            border: none;
        }
        .prioritization-matrix .cell span {
            display: block;
            margin-bottom: 3px;
        }
        .prioritization-matrix .cell .opportunity-name {
            font-weight: bold;
            color: #007bff;
            font-size: 0.8em;
            margin-bottom: 2px;
        }
        .prioritization-matrix .cell .opportunity-score {
            font-size: 0.7em;
            color: #666;
        }
        .matrix-legend {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            color: #666;
        }
        .matrix-legend span {
            margin: 0 10px;
        }

    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 AI Opportunity Radar Tool - Banco Nova</h1>
        <p style="text-align: center; font-size: 1.1em; color: #666;">Identifica, evalúa y prioriza oportunidades de IA estratégicas para el Banco.</p>

        <div class="section">
            <h2>1. Evaluación de Oportunidades de IA</h2>
            <div class="select-group">
                <label for="opportunity-select">Seleccionar Oportunidad Existente:</label>
                <select id="opportunity-select">
                    <option value="">-- Crear Nueva Oportunidad --</option>
                </select>
                <button onclick="loadOpportunityFromSelect()">Cargar</button>
            </div>

            <form id="evaluation-form">
                <h3>Detalles de la Oportunidad</h3>
                <div class="form-group">
                    <label for="opportunity-name">Nombre de la Oportunidad:</label>
                    <input type="text" id="opportunity-name" placeholder="Ej: Scoring Crediticio Avanzado" required>
                </div>
                <div class="form-group">
                    <label for="opportunity-description">Descripción Breve:</label>
                    <input type="text" id="opportunity-description" placeholder="Ej: Mejora la precisión de evaluación de riesgo crediticio">
                </div>

                <h3>Dimensiones del Radar (Scoring 0-100)</h3>
                <div class="form-group">
                    <label for="impactoNegocio">Impacto en Negocio (Revenue/Cost):</label>
                    <input type="range" id="impactoNegocio" min="0" max="100" value="50" oninput="updateScore('impactoNegocio')">
                    <input type="number" id="impactoNegocio-num" min="0" max="100" value="50" oninput="updateRange('impactoNegocio')">
                    <span id="impactoNegocio-score" class="score-display">50</span>
                </div>
                <div class="form-group">
                    <label for="viabilidadTecnica">Viabilidad Técnica:</label>
                    <input type="range" id="viabilidadTecnica" min="0" max="100" value="50" oninput="updateScore('viabilidadTecnica')">
                    <input type="number" id="viabilidadTecnica-num" min="0" max="100" value="50" oninput="updateRange('viabilidadTecnica')">
                    <span id="viabilidadTecnica-score" class="score-display">50</span>
                </div>
                <div class="form-group">
                    <label for="alineacionEstrategica">Alineación Estratégica:</label>
                    <input type="range" id="alineacionEstrategica" min="0" max="100" value="50" oninput="updateScore('alineacionEstrategica')">
                    <input type="number" id="alineacionEstrategica-num" min="0" max="100" value="50" oninput="updateRange('alineacionEstrategica')">
                    <span id="alineacionEstrategica-score" class="score-display">50</span>
                </div>
                <div class="form-group">
                    <label for="madurezDatos">Madurez de Datos:</label>
                    <input type="range" id="madurezDatos" min="0" max="100" value="50" oninput="updateScore('madurezDatos')">
                    <input type="number" id="madurezDatos-num" min="0" max="100" value="50" oninput="updateRange('madurezDatos')">
                    <span id="madurezDatos-score" class="score-display">50</span>
                </div>
                <div class="form-group">
                    <label for="riesgoRegulatorio">Riesgo Regulatorio:</label>
                    <input type="range" id="riesgoRegulatorio" min="0" max="100" value="50" oninput="updateScore('riesgoRegulatorio')">
                    <input type="number" id="riesgoRegulatorio-num" min="0" max="100" value="50" oninput="updateRange('riesgoRegulatorio')">
                    <span id="riesgoRegulatorio-score" class="score-display">50</span>
                </div>
                <div class="form-group">
                    <label for="complejidadImplementacion">Complejidad de Implementación:</label>
                    <input type="range" id="complejidadImplementacion" min="0" max="100" value="50" oninput="updateScore('complejidadImplementacion')">
                    <input type="number" id="complejidadImplementacion-num" min="0" max="100" value="50" oninput="updateRange('complejidadImplementacion')">
                    <span id="complejidadImplementacion-score" class="score-display">50</span>
                </div>
                <div class="form-group">
                    <label for="adopcionEsperada">Adopción Esperada (Usuarios/Clientes):</label>
                    <input type="range" id="adopcionEsperada" min="0" max="100" value="50" oninput="updateScore('adopcionEsperada')">
                    <input type="number" id="adopcionEsperada-num" min="0" max="100" value="50" oninput="updateRange('adopcionEsperada')">
                    <span id="adopcionEsperada-score" class="score-display">50</span>
                </div>
                <div class="form-group">
                    <label for="timeToValue">Time to Value (Meses, 0=rápido, 100=lento):</label>
                    <input type="range" id="timeToValue" min="0" max="100" value="50" oninput="updateScore('timeToValue')">
                    <input type="number" id="timeToValue-num" min="0" max="100" value="50" oninput="updateRange('timeToValue')">
                    <span id="timeToValue-score" class="score-display">50</span>
                </div>

                <div class="summary-box">
                    <p><strong>Score Total Ponderado:</strong> <span id="total-score">0</span></p>
                    <p><strong>Clasificación Automática:</strong> <span id="classification">N/A</span> <span id="classification-badge" class="badge"></span></p>
                </div>

                <div class="button-group">
                    <button type="button" onclick="addOrUpdateOpportunity()">Guardar Oportunidad</button>
                    <button type="button" onclick="resetForm()">Nueva Oportunidad</button>
                </div>
            </form>
        </div>

        <div class="section">
            <h2>2. Dashboard de Comparación y Priorización</h2>
            <div class="select-group">
                <label for="compare-opportunities-select">Oportunidades a Comparar:</label>
                <select id="compare-opportunities-select" multiple size="5" onchange="updateComparisonChart()">
                    <!-- Options will be populated by JS -->
                </select>
                <button onclick="updateComparisonChart()">Actualizar Gráfico</button>
            </div>

            <div class="chart-container">
                <canvas id="radarChart"></canvas>
            </div>

            <div class="grid-2-col">
                <div class="card">
                    <h4>Matriz de Priorización (Impacto vs Esfuerzo)</h4>
                    <div class="prioritization-matrix">
                        <div class="cell empty"></div>
                        <div class="cell x-axis-label">Bajo Esfuerzo</div>
                        <div class="cell x-axis-label">Alto Esfuerzo</div>

                        <div class="cell y-axis-label">Alto Impacto</div>
                        <div class="cell" id="matrix-high-impact-low-effort"></div>
                        <div class="cell" id="matrix-high-impact-high-effort"></div>

                        <div class="cell y-axis-label">Bajo Impacto</div>
                        <div class="cell" id="matrix-low-impact-low-effort"></div>
                        <div class="cell" id="matrix-low-impact-high-effort"></div>
                    </div>
                    <div class="matrix-legend">
                        <span>Impacto (Alto/Bajo)</span>
                        <span>Esfuerzo (Bajo/Alto)</span>
                    </div>
                </div>
                <div class="card">
                    <h4>Roadmap Sugerido & Análisis de Gaps</h4>
                    <div id="roadmap-suggestions">
                        <p>Selecciona oportunidades para ver el roadmap sugerido y el análisis de gaps.</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>3. Integración con el CoE IA</h2>
            <div class="grid-3-col">
                <div class="card">
                    <h4>Alineación con Framework IMPACT</h4>
                    <p>Las oportunidades son evaluadas bajo criterios que alimentan directamente el Framework IMPACT del CoE IA:</p>
                    <ul class="recommendation-list">
                        <li><strong>Impacto en Negocio:</strong> Contribuye a <em>Performance (Eficiencia)</em> y <em>Cost-Effective (ROI)</em>.</li>
                        <li><strong>Time to Value:</strong> Clave para <em>Implementation (Time to First Value)</em>.</li>
                        <li><strong>Adopción Esperada:</strong> Relacionado con <em>Acceptance (Tasa de Aceptación)</em>.</li>
                        <li><strong>Alineación Estratégica:</strong> Asegura la coherencia con la visión del CoE IA.</li>
                    </ul>
                </div>
                <div class="card">
                    <h4>Conexión con Proceso AISIA</h4>
                    <p>La evaluación de <strong>Riesgo Regulatorio</strong> y <strong>Viabilidad Técnica</strong> es crucial para el proceso AISIA:</p>
                    <ul class="recommendation-list">
                        <li>Oportunidades con <strong>Alto Riesgo Regulatorio</strong> (>70) deben ser priorizadas para revisión AISIA.</li>
                        <li>El <strong>AI Risk Officer</strong> y <strong>AI Governance Lead</strong> deben ser consultados.</li>
                        <li>Referencia: Anexo B - Checklist de Evaluación AISIA.</li>
                    </ul>
                </div>
                <div class="card">
                    <h4>Referencias a Playbooks</h4>
                    <p>Según los resultados de la evaluación:</p>
                    <ul class="recommendation-list">
                        <li><strong>Baja Madurez de Datos:</strong> Consultar Knowledge Hub para guías de calidad de datos.</li>
                        <li><strong>Alta Complejidad:</strong> Involucrar al AI Platform Team (Nova-Cell) y MLOps Engineer.</li>
                        <li><strong>Baja Adopción:</strong> Contactar al AI Training Lead para programas de capacitación.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>4. Exportar Resultados</h2>
            <button onclick="exportOpportunities()">Exportar Todas las Oportunidades (JSON)</button>
            <button onclick="printReport()">Imprimir Reporte Actual</button>
        </div>
    </div>

    <script>
        // Global state for opportunities
        let opportunities = [];
        let radarChart;

        // Define the 8 dimensions for the radar chart and evaluation
        const dimensions = [
            "impactoNegocio",
            "viabilidadTecnica",
            "alineacionEstrategica",
            "madurezDatos",
            "riesgoRegulatorio",
            "complejidadImplementacion",
            "adopcionEsperada",
            "timeToValue"
        ];

        // Labels for the radar chart
        const dimensionLabels = {
            "impactoNegocio": "Impacto en Negocio",
            "viabilidadTecnica": "Viabilidad Técnica",
            "alineacionEstrategica": "Alineación Estratégica",
            "madurezDatos": "Madurez de Datos",
            "riesgoRegulatorio": "Riesgo Regulatorio",
            "complejidadImplementacion": "Complejidad de Implementación",
            "adopcionEsperada": "Adopción Esperada",
            "timeToValue": "Time to Value"
        };

        // Weights for the total score (can be adjusted)
        const weights = {
            "impactoNegocio": 0.25,
            "viabilidadTecnica": 0.15,
            "alineacionEstrategica": 0.20,
            "madurezDatos": 0.10,
            "riesgoRegulatorio": 0.10,
            "complejidadImplementacion": 0.10,
            "adopcionEsperada": 0.05,
            "timeToValue": 0.05
        };

        // Pre-loaded banking opportunities
        const preLoadedOpportunities = [
            {
                id: "scoring-crediticio",
                name: "Scoring Crediticio Avanzado",
                description: "Mejora la precisión de evaluación de riesgo crediticio usando ML.",
                scores: {
                    impactoNegocio: 90,
                    viabilidadTecnica: 80,
                    alineacionEstrategica: 95,
                    madurezDatos: 75,
                    riesgoRegulatorio: 85,
                    complejidadImplementacion: 70,
                    adopcionEsperada: 90,
                    timeToValue: 40
                }
            },
            {
                id: "deteccion-fraude",
                name: "Detección de Fraude en Tiempo Real",
                description: "Identificación proactiva de transacciones fraudulentas.",
                scores: {
                    impactoNegocio: 95,
                    viabilidadTecnica: 70,
                    alineacionEstrategica: 90,
                    madurezDatos: 80,
                    riesgoRegulatorio: 90,
                    complejidadImplementacion: 85,
                    adopcionEsperada: 95,
                    timeToValue: 60
                }
            },
            {
                id: "chatbots-conversacionales",
                name: "Chatbots Conversacionales",
                description: "Automatización de consultas y soporte al cliente 24/7.",
                scores: {
                    impactoNegocio: 70,
                    viabilidadTecnica: 90,
                    alineacionEstrategica: 80,
                    madurezDatos: 60,
                    riesgoRegulatorio: 50,
                    complejidadImplementacion: 50,
                    adopcionEsperada: 85,
                    timeToValue: 30
                }
            },
            {
                id: "rpa-backoffice",
                name: "RPA para Back-office",
                description: "Automatización de tareas repetitivas en operaciones internas.",
                scores: {
                    impactoNegocio: 65,
                    viabilidadTecnica: 95,
                    alineacionEstrategica: 70,
                    madurezDatos: 85,
                    riesgoRegulatorio: 30,
                    complejidadImplementacion: 40,
                    adopcionEsperada: 70,
                    timeToValue: 20
                }
            },
            {
                id: "analisis-sentimiento",
                name: "Análisis de Sentimiento en RRSS",
                description: "Monitoreo de la percepción de marca y productos en redes sociales.",
                scores: {
                    impactoNegocio: 50,
                    viabilidadTecnica: 70,
                    alineacionEstrategica: 60,
                    madurezDatos: 65,
                    riesgoRegulatorio: 40,
                    complejidadImplementacion: 60,
                    adopcionEsperada: 50,
                    timeToValue: 50
                }
            },
            {
                id: "prediccion-churn",
                name: "Predicción de Churn de Clientes",
                description: "Identificación temprana de clientes en riesgo de abandono.",
                scores: {
                    impactoNegocio: 80,
                    viabilidadTecnica: 75,
                    alineacionEstrategica: 85,
                    madurezDatos: 70,
                    riesgoRegulatorio: 60,
                    complejidadImplementacion: 65,
                    adopcionEsperada: 80,
                    timeToValue: 55
                }
            },
            {
                id: "optimizacion-precios",
                name: "Optimización de Precios y Ofertas",
                description: "Uso de IA para personalizar precios y ofertas de productos bancarios.",
                scores: {
                    impactoNegocio: 85,
                    viabilidadTecnica: 60,
                    alineacionEstrategica: 80,
                    madurezDatos: 65,
                    riesgoRegulatorio: 70,
                    complejidadImplementacion: 75,
                    adopcionEsperada: 75,
                    timeToValue: 70
                }
            },
            {
                id: "kyc-automatizado",
                name: "KYC Automatizado",
                description: "Automatización y agilización del proceso Know Your Customer.",
                scores: {
                    impactoNegocio: 75,
                    viabilidadTecnica: 85,
                    alineacionEstrategica: 85,
                    madurezDatos: 70,
                    riesgoRegulatorio: 95,
                    complejidadImplementacion: 80,
                    adopcionEsperada: 90,
                    timeToValue: 60
                }
            }
        ];

        // Initialize pre-loaded opportunities
        opportunities = [...preLoadedOpportunities];

        // Function to update the score display
        function updateScore(dimensionId) {
            const slider = document.getElementById(dimensionId);
            const numberInput = document.getElementById(`${dimensionId}-num`);
            const scoreDisplay = document.getElementById(`${dimensionId}-score`);
            scoreDisplay.textContent = slider.value;
            numberInput.value = slider.value;
            calculateTotalScoreAndClassification();
        }

        // Function to update the slider based on number input
        function updateRange(dimensionId) {
            const slider = document.getElementById(dimensionId);
            const numberInput = document.getElementById(`${dimensionId}-num`);
            const scoreDisplay = document.getElementById(`${dimensionId}-score`);
            let value = parseInt(numberInput.value);
            if (isNaN(value) || value < 0) value = 0;
            if (value > 100) value = 100;
            slider.value = value;
            numberInput.value = value;
            scoreDisplay.textContent = value;
            calculateTotalScoreAndClassification();
        }

        // Calculate weighted total score and classification
        function calculateTotalScoreAndClassification() {
            let totalWeightedScore = 0;
            let currentScores = {};

            dimensions.forEach(dim => {
                const value = parseInt(document.getElementById(dim).value);
                currentScores[dim] = value;
                // For Time to Value, lower is better, so we invert it
                const weightedValue = (dim === "timeToValue") ? (100 - value) : value;
                totalWeightedScore += weightedValue * weights[dim];
            });

            document.getElementById("total-score").textContent = Math.round(totalWeightedScore);

            // Determine classification
            let classification = "N/A";
            let badgeClass = "";

            const impactScore = (currentScores.impactoNegocio * 0.4 + currentScores.alineacionEstrategica * 0.3 + currentScores.adopcionEsperada * 0.3);
            const effortScore = (currentScores.complejidadImplementacion * 0.3 + currentScores.riesgoRegulatorio * 0.3 + (100 - currentScores.timeToValue) * 0.2 + (100 - currentScores.viabilidadTecnica) * 0.2);

            const HIGH_IMPACT_THRESHOLD = 75;
            const LOW_IMPACT_THRESHOLD = 40;
            const LOW_EFFORT_THRESHOLD = 50;

            if (impactScore >= HIGH_IMPACT_THRESHOLD && effortScore <= LOW_EFFORT_THRESHOLD) {
                classification = "Quick Win";
                badgeClass = "badge-quick-win";
            } else if (impactScore >= HIGH_IMPACT_THRESHOLD && effortScore > LOW_EFFORT_THRESHOLD) {
                classification = "Strategic";
                badgeClass = "badge-strategic";
            } else if (impactScore > LOW_IMPACT_THRESHOLD && effortScore > LOW_EFFORT_THRESHOLD) {
                classification = "Transformación";
                badgeClass = "badge-transform";
            } else {
                classification = "Experimental";
                badgeClass = "badge-experimental";
            }

            document.getElementById("classification").textContent = classification;
            const badgeElement = document.getElementById("classification-badge");
            badgeElement.className = `badge ${badgeClass}`;
            badgeElement.textContent = classification;
        }

        // Add or update opportunity
        function addOrUpdateOpportunity() {
            const opportunityName = document.getElementById("opportunity-name").value.trim();
            const opportunityDescription = document.getElementById("opportunity-description").value.trim();

            if (!opportunityName) {
                alert("El nombre de la oportunidad es obligatorio.");
                return;
            }

            const currentScores = {};
            dimensions.forEach(dim => {
                currentScores[dim] = parseInt(document.getElementById(dim).value);
            });

            const totalScore = parseInt(document.getElementById("total-score").textContent);
            const classification = document.getElementById("classification").textContent;

            const selectedId = document.getElementById("opportunity-select").value;
            let existingOpportunityIndex = -1;
            if (selectedId) {
                existingOpportunityIndex = opportunities.findIndex(opp => opp.id === selectedId);
            }

            if (existingOpportunityIndex !== -1) {
                opportunities[existingOpportunityIndex] = {
                    ...opportunities[existingOpportunityIndex],
                    name: opportunityName,
                    description: opportunityDescription,
                    scores: currentScores,
                    totalScore: totalScore,
                    classification: classification
                };
                alert(`Oportunidad "${opportunityName}" actualizada.`);
            } else {
                const newId = opportunityName.toLowerCase().replace(/\s+/g, "-").replace(/[^a-z0-9-]/g, "");
                const newOpportunity = {
                    id: newId,
                    name: opportunityName,
                    description: opportunityDescription,
                    scores: currentScores,
                    totalScore: totalScore,
                    classification: classification
                };
                opportunities.push(newOpportunity);
                alert(`Oportunidad "${opportunityName}" guardada.`);
            }

            populateOpportunitySelects();
            resetForm();
            updateComparisonChart();
            updatePrioritizationMatrix();
        }

        // Reset form
        function resetForm() {
            document.getElementById("evaluation-form").reset();
            document.getElementById("opportunity-name").value = "";
            document.getElementById("opportunity-description").value = "";
            dimensions.forEach(dim => {
                document.getElementById(dim).value = 50;
                document.getElementById(`${dim}-num`).value = 50;
                document.getElementById(`${dim}-score`).textContent = 50;
            });
            document.getElementById("total-score").textContent = "0";
            document.getElementById("classification").textContent = "N/A";
            document.getElementById("classification-badge").className = "badge";
            document.getElementById("classification-badge").textContent = "";
            document.getElementById("opportunity-select").value = "";
            calculateTotalScoreAndClassification();
        }

        // Populate opportunity selection dropdowns
        function populateOpportunitySelects() {
            const selectElement = document.getElementById("opportunity-select");
            const compareSelectElement = document.getElementById("compare-opportunities-select");

            selectElement.innerHTML = '<option value="">-- Crear Nueva Oportunidad --</option>';
            compareSelectElement.innerHTML = "";

            opportunities.forEach(opp => {
                const option = document.createElement("option");
                option.value = opp.id;
                option.textContent = opp.name;
                selectElement.appendChild(option);

                const compareOption = document.createElement("option");
                compareOption.value = opp.id;
                compareOption.textContent = opp.name;
                compareSelectElement.appendChild(compareOption);
            });
        }

        // Load opportunity from select
        function loadOpportunityFromSelect() {
            const selectedId = document.getElementById("opportunity-select").value;
            if (!selectedId) {
                resetForm();
                return;
            }

            const selectedOpportunity = opportunities.find(opp => opp.id === selectedId);
            if (selectedOpportunity) {
                document.getElementById("opportunity-name").value = selectedOpportunity.name;
                document.getElementById("opportunity-description").value = selectedOpportunity.description || "";
                dimensions.forEach(dim => {
                    const score = selectedOpportunity.scores[dim];
                    document.getElementById(dim).value = score;
                    document.getElementById(`${dim}-num`).value = score;
                    document.getElementById(`${dim}-score`).textContent = score;
                });
                calculateTotalScoreAndClassification();
            }
        }

        // Initialize or update radar chart
        function initOrUpdateRadarChart() {
            const ctx = document.getElementById("radarChart").getContext("2d");

            if (radarChart) {
                radarChart.destroy();
            }

            radarChart = new Chart(ctx, {
                type: "radar",
                data: {
                    labels: dimensions.map(dim => dimensionLabels[dim]),
                    datasets: []
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: "Comparación de Oportunidades de IA",
                            font: {
                                size: 18
                            },
                            color: "#0056b3"
                        },
                        legend: {
                            position: "top",
                        }
                    },
                    scales: {
                        r: {
                            angleLines: {
                                color: "#e0e7eb"
                            },
                            grid: {
                                color: "#e0e7eb"
                            },
                            pointLabels: {
                                font: {
                                    size: 12,
                                    weight: "bold"
                                },
                                color: "#555"
                            },
                            suggestedMin: 0,
                            suggestedMax: 100,
                            ticks: {
                                stepSize: 25,
                                backdropColor: "rgba(255, 255, 255, 0.8)",
                                color: "#777"
                            }
                        }
                    }
                }
            });
        }

        // Update comparison chart
        function updateComparisonChart() {
            const selectedOptions = Array.from(document.getElementById("compare-opportunities-select").selectedOptions);
            const selectedOpportunityIds = selectedOptions.map(option => option.value);

            const datasets = [];
            const colors = ["#007bff", "#28a745", "#ffc107", "#dc3545", "#6c757d", "#17a2b8", "#fd7e14", "#e83e8c"];

            selectedOpportunityIds.forEach((id, index) => {
                const opp = opportunities.find(o => o.id === id);
                if (opp) {
                    datasets.push({
                        label: opp.name,
                        data: dimensions.map(dim => opp.scores[dim]),
                        backgroundColor: `rgba(${parseInt(colors[index].slice(1,3), 16)}, ${parseInt(colors[index].slice(3,5), 16)}, ${parseInt(colors[index].slice(5,7), 16)}, 0.2)`,
                        borderColor: colors[index],
                        pointBackgroundColor: colors[index],
                        pointBorderColor: "#fff",
                        pointHoverBackgroundColor: "#fff",
                        pointHoverBorderColor: colors[index],
                        borderWidth: 2
                    });
                }
            });

            if (radarChart) {
                radarChart.data.datasets = datasets;
                radarChart.update();
            }

            updatePrioritizationMatrix();
            generateRoadmapAndGapAnalysis(selectedOpportunityIds);
        }

        // Update prioritization matrix
        function updatePrioritizationMatrix() {
            const matrixCells = {
                "high-impact-low-effort": document.getElementById("matrix-high-impact-low-effort"),
                "high-impact-high-effort": document.getElementById("matrix-high-impact-high-effort"),
                "low-impact-low-effort": document.getElementById("matrix-low-impact-low-effort"),
                "low-impact-high-effort": document.getElementById("matrix-low-impact-high-effort")
            };

            for (const key in matrixCells) {
                matrixCells[key].innerHTML = "";
            }

            opportunities.forEach(opp => {
                const currentScores = opp.scores;

                const impactScore = (currentScores.impactoNegocio * 0.4 + currentScores.alineacionEstrategica * 0.3 + currentScores.adopcionEsperada * 0.3);
                const effortScore = (currentScores.complejidadImplementacion * 0.3 + currentScores.riesgoRegulatorio * 0.3 + (currentScores.timeToValue) * 0.2 + (100 - currentScores.viabilidadTecnica) * 0.2);

                const IMPACT_MID_THRESHOLD = 70;
                const EFFORT_MID_THRESHOLD = 60;

                let quadrant = "";
                if (impactScore >= IMPACT_MID_THRESHOLD && effortScore <= EFFORT_MID_THRESHOLD) {
                    quadrant = "high-impact-low-effort";
                } else if (impactScore >= IMPACT_MID_THRESHOLD && effortScore > EFFORT_MID_THRESHOLD) {
                    quadrant = "high-impact-high-effort";
                } else if (impactScore < IMPACT_MID_THRESHOLD && effortScore <= EFFORT_MID_THRESHOLD) {
                    quadrant = "low-impact-low-effort";
                } else {
                    quadrant = "low-impact-high-effort";
                }

                const oppElement = document.createElement("div");
                oppElement.className = "matrix-item";
                oppElement.innerHTML = `<span class="opportunity-name">${opp.name}</span><span class="opportunity-score">(${Math.round(impactScore)}I / ${Math.round(effortScore)}E)</span>`;
                matrixCells[quadrant].appendChild(oppElement);
            });
        }

        // Generate roadmap and gap analysis
        function generateRoadmapAndGapAnalysis(selectedOpportunityIds) {
            const roadmapDiv = document.getElementById("roadmap-suggestions");
            roadmapDiv.innerHTML = "";

            if (selectedOpportunityIds.length === 0) {
                roadmapDiv.innerHTML = "<p>Selecciona oportunidades para ver el roadmap sugerido y el análisis de gaps.</p>";
                return;
            }

            const selectedOpportunities = opportunities.filter(opp => selectedOpportunityIds.includes(opp.id));

            let roadmapHTML = "<h4>Roadmap Sugerido</h4><ul class='recommendation-list'>";
            let gapAnalysisHTML = "<h4>Análisis de Gaps y Requisitos</h4><ul class='recommendation-list'>";

            selectedOpportunities.sort((a, b) => {
                const order = { "Quick Win": 1, "Strategic": 2, "Transformación": 3, "Experimental": 4 };
                return order[a.classification] - order[b.classification];
            });

            selectedOpportunities.forEach(opp => {
                roadmapHTML += `<li><strong>${opp.name}</strong> (${opp.classification}): `;
                if (opp.classification === "Quick Win") {
                    roadmapHTML += `<em>Implementar rápidamente para generar valor.</em>`;
                } else if (opp.classification === "Strategic") {
                    roadmapHTML += `<em>Planificar implementación robusta, alineada con estrategia.</em>`;
                } else if (opp.classification === "Transformación") {
                    roadmapHTML += `<em>Requiere inversión significativa y gestión del cambio.</em>`;
                } else if (opp.classification === "Experimental") {
                    roadmapHTML += `<em>Iniciar con PoC para validar hipótesis.</em>`;
                }
                roadmapHTML += "</li>";

                gapAnalysisHTML += `<li><strong>${opp.name}:</strong>`;
                let oppGaps = [];

                if (opp.scores.madurezDatos < 50) {
                    oppGaps.push(`<strong>Madurez de Datos baja (${opp.scores.madurezDatos}):</strong> Requiere inversión en calidad de datos.`);
                }
                if (opp.scores.viabilidadTecnica < 50) {
                    oppGaps.push(`<strong>Baja Viabilidad Técnica (${opp.scores.viabilidadTecnica}):</strong> Explorar tecnologías alternativas.`);
                }
                if (opp.scores.riesgoRegulatorio > 70) {
                    oppGaps.push(`<strong>Alto Riesgo Regulatorio (${opp.scores.riesgoRegulatorio}):</strong> Requiere evaluación AISIA exhaustiva.`);
                }
                if (opp.scores.complejidadImplementacion > 70) {
                    oppGaps.push(`<strong>Alta Complejidad (${opp.scores.complejidadImplementacion}):</strong> Necesita plan de proyecto detallado.`);
                }
                if (opp.scores.adopcionEsperada < 60) {
                    oppGaps.push(`<strong>Baja Adopción Esperada (${opp.scores.adopcionEsperada}):</strong> Requiere gestión del cambio.`);
                }
                if (opp.scores.timeToValue > 60) {
                    oppGaps.push(`<strong>Alto Time to Value (${opp.scores.timeToValue}):</strong> Evaluar MVPs para valor incremental.`);
                }

                if (oppGaps.length > 0) {
                    gapAnalysisHTML += `<ul>${oppGaps.map(gap => `<li>${gap}</li>`).join("")}</ul>`;
                } else {
                    gapAnalysisHTML += ` <em>No se identificaron gaps críticos.</em>`;
                }
                gapAnalysisHTML += "</li>";
            });

            roadmapHTML += "</ul>";
            gapAnalysisHTML += "</ul>";

            roadmapDiv.innerHTML = roadmapHTML + gapAnalysisHTML;
        }

        // Export opportunities as JSON
        function exportOpportunities() {
            const dataStr = JSON.stringify(opportunities, null, 2);
            const dataUri = "data:application/json;charset=utf-8," + encodeURIComponent(dataStr);
            const exportFileDefaultName = "ai_opportunities_radar.json";
            const linkElement = document.createElement("a");
            linkElement.setAttribute("href", dataUri);
            linkElement.setAttribute("download", exportFileDefaultName);
            linkElement.click();
        }

        // Print report
        function printReport() {
            window.print();
        }

        // Initial setup
        document.addEventListener("DOMContentLoaded", () => {
            populateOpportunitySelects();
            dimensions.forEach(dim => {
                const slider = document.getElementById(dim);
                const numberInput = document.getElementById(`${dim}-num`);
                slider.addEventListener("input", () => updateScore(dim));
                numberInput.addEventListener("input", () => updateRange(dim));
            });
            calculateTotalScoreAndClassification();
            initOrUpdateRadarChart();
            updatePrioritizationMatrix();
        });
    </script>
</body>
</html>' width="100%" height="2200" style="border: none; border-radius: 8px;">
  </iframe>
</div>

## 🎯 Características Principales

### Dimensiones de Evaluación (8 Ejes)

| Dimensión | Descripción | Peso |
|-----------|-------------|------|
| **Impacto en Negocio** | Revenue/Cost impact | 25% |
| **Viabilidad Técnica** | Factibilidad tecnológica | 15% |
| **Alineación Estratégica** | Coherencia con visión bancaria | 20% |
| **Madurez de Datos** | Disponibilidad y calidad de datos | 10% |
| **Riesgo Regulatorio** | Cumplimiento normativo | 10% |
| **Complejidad de Implementación** | Esfuerzo y recursos requeridos | 10% |
| **Adopción Esperada** | Aceptación por usuarios/clientes | 5% |
| **Time to Value** | Tiempo hasta generar valor | 5% |

### Clasificación Automática de Oportunidades

!!! success "Quick Win"
    Alto Impacto + Bajo Esfuerzo = Implementación inmediata

!!! info "Strategic"
    Alto Impacto + Alto Esfuerzo = Planificación robusta

!!! warning "Transformación"
    Impacto Medio + Alto Esfuerzo = Inversión a largo plazo

!!! tip "Experimental"
    Bajo Impacto + Bajo Esfuerzo = Pruebas de concepto

## 📈 Dashboard de Comparación

### Visualización Radar

El gráfico radar permite comparar hasta 8 oportunidades simultáneamente:
- Visualización multidimensional clara
- Identificación rápida de fortalezas y debilidades
- Comparación directa entre diferentes iniciativas

### Matriz de Priorización (Impacto vs Esfuerzo)

```mermaid
graph LR
    A[Alto Impacto<br>Bajo Esfuerzo] -->|Quick Win| B[Prioridad 1]
    C[Alto Impacto<br>Alto Esfuerzo] -->|Strategic| D[Prioridad 2]
    E[Bajo Impacto<br>Bajo Esfuerzo] -->|Experimental| F[Prioridad 3]
    G[Bajo Impacto<br>Alto Esfuerzo] -->|Re-evaluar| H[Prioridad 4]
```

## 🏦 Catálogo de Oportunidades Bancarias Pre-cargadas

### 1. Scoring Crediticio Avanzado
- **Impacto**: 90/100
- **Viabilidad**: 80/100
- **Clasificación**: Strategic

### 2. Detección de Fraude en Tiempo Real
- **Impacto**: 95/100
- **Viabilidad**: 70/100
- **Clasificación**: Strategic

### 3. Chatbots Conversacionales
- **Impacto**: 70/100
- **Viabilidad**: 90/100
- **Clasificación**: Quick Win

### 4. RPA para Back-office
- **Impacto**: 65/100
- **Viabilidad**: 95/100
- **Clasificación**: Quick Win

### 5. Análisis de Sentimiento en RRSS
- **Impacto**: 50/100
- **Viabilidad**: 70/100
- **Clasificación**: Experimental

### 6. Predicción de Churn
- **Impacto**: 80/100
- **Viabilidad**: 75/100
- **Clasificación**: Strategic

### 7. Optimización de Precios
- **Impacto**: 85/100
- **Viabilidad**: 60/100
- **Clasificación**: Transformación

### 8. KYC Automatizado
- **Impacto**: 75/100
- **Viabilidad**: 85/100
- **Clasificación**: Strategic

## 🔗 Integración con Framework IMPACT

La herramienta se alinea directamente con las métricas del Framework IMPACT:

| Dimensión Radar | Métrica IMPACT | Contribución |
|-----------------|----------------|--------------|
| Impacto en Negocio | Performance & Cost-Effective | ROI y eficiencia operativa |
| Time to Value | Implementation | Velocidad de entrega de valor |
| Adopción Esperada | Acceptance | Tasa de adopción usuario |
| Alineación Estratégica | Momentum | Coherencia con visión CoE |

## 🛡️ Conexión con Proceso AISIA

### Triggers para Evaluación AISIA

- **Riesgo Regulatorio > 70**: Revisión obligatoria AISIA
- **Viabilidad Técnica < 30**: Evaluación de factibilidad
- **Impacto en Clientes Alto**: Análisis de impacto ético

### Stakeholders Clave

- **AI Risk Officer**: Oportunidades de alto riesgo
- **AI Governance Lead**: Cumplimiento regulatorio
- **Data Ethicist**: Implicaciones éticas de datos

## 📋 Análisis de Gaps y Roadmap

### Gaps Comunes y Acciones

| Gap Identificado | Umbral | Acción Recomendada |
|------------------|--------|-------------------|
| Baja Madurez de Datos | < 50 | Consultar Knowledge Hub, invertir en calidad de datos |
| Baja Viabilidad Técnica | < 50 | Involucrar AI Platform Team (Nova-Cell) |
| Alto Riesgo Regulatorio | > 70 | Proceso AISIA exhaustivo |
| Alta Complejidad | > 70 | Plan de proyecto detallado con MLOps |
| Baja Adopción Esperada | < 60 | Programa AI Champions, gestión del cambio |

## 💡 Guía de Uso

### Proceso de Evaluación

1. **Seleccionar o crear** nueva oportunidad
2. **Evaluar** cada dimensión (0-100)
3. **Revisar** clasificación automática
4. **Comparar** con otras oportunidades
5. **Analizar** gaps y requisitos
6. **Exportar** resultados para presentación

### Mejores Prácticas

- Involucrar stakeholders clave en la evaluación
- Actualizar scores periódicamente
- Usar datos históricos para calibrar estimaciones
- Documentar supuestos y limitaciones
- Priorizar Quick Wins para momentum inicial

## 📊 Exportación y Reportes

### Formatos Disponibles

- **JSON**: Exportación completa de datos
- **Print**: Reporte visual para presentaciones
- **Dashboard**: Vista ejecutiva en tiempo real

## 🆘 Soporte

Para dudas sobre el uso del AI Opportunity Radar:

- **Email**: opportunity-radar@banco.mx
- **Teams**: Canal #ai-opportunities
- **Wiki**: wiki.banco.mx/opportunity-radar
- **Helpdesk CoE**: Ext. 4242

---

*AI Opportunity Radar Tool v2.0 | Centro de Excelencia de IA | Última actualización: 09 de enero de 2025*