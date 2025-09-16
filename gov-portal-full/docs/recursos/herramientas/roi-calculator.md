---
title: Calculadora ROI para Iniciativas de IA
tags:
  - herramientas
  - finanzas
  - roi
  - evaluación
search:
  boost: 3
---

# Calculadora ROI para Iniciativas de IA en Banca

<div class="nova-card">
  <div class="nova-accent-border">
    <h2>💰 Análisis Financiero Integral para Proyectos de IA</h2>
    <p>Herramienta completa para calcular ROI, VAN, TIR y otros indicadores financieros clave, diseñada específicamente para evaluar iniciativas de IA en el contexto bancario mexicano.</p>
  </div>
</div>

## 📊 Calculadora Interactiva

<div style="background-color: #f4f7f9; padding: 30px; border-radius: 12px; margin: 20px 0;">
  <iframe srcdoc='<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora ROI para Iniciativas de IA en Banca Mexicana</title>
    
    <!-- Normalización y estilos básicos -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">
    <!-- Librería de Chart.js para gráficos -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    
    <style>
      /* ===============================
         Estilos básicos y de layout
         =============================== */
      body {
        font-family: Arial, sans-serif;
        background: #f8f9fa;
        margin: 0;
        padding: 20px;
        color: #333;
      }
      h1, h2, h3 {
        color: #0056b3;
      }
      form {
        background: #fff;
        padding: 20px;
        border: 1px solid #ddd;
        margin-bottom: 30px;
        border-radius: 5px;
      }
      label {
        font-weight: bold;
      }
      input, select, textarea {
        padding: 8px;
        margin: 5px 0 15px;
        width: 100%;
        border: 1px solid #ccc;
        border-radius: 4px;
      }
      fieldset {
        margin-bottom: 20px;
        padding: 10px;
        border: 1px solid #ccc;
      }
      .button-container {
        display: flex;
        gap: 10px;
      }
      button {
        background: #0056b3;
        color: #fff;
        border: none;
        padding: 10px 15px;
        border-radius: 4px;
        cursor: pointer;
      }
      button:hover {
        background: #004494;
      }
      #results {
        background: #fff;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 5px;
        margin-bottom: 30px;
      }
      .result-line {
        margin-bottom: 10px;
      }
      .note {
        font-size: 0.9em;
        color: #666;
      }
      canvas {
        background: #fff;
        border: 1px solid #ddd;
        margin-top: 20px;
      }
    </style>
  </head>
  
  <body>
    <!-- Título principal -->
    <h1>Calculadora ROI para Iniciativas de IA en Banco Mexicano</h1>
    <p class="note">
      Esta herramienta calcula ROI, VAN, TIR, Payback period y más, integrando casos de uso bancarios como scoring, AML, chatbots y RPA.
    </p>
    
    <!-- Formulario principal -->
    <form id="roiForm">
      
      <!-- Sección 1: Información del Proyecto -->
      <fieldset>
        <legend>1. Información del Proyecto</legend>
        <label for="projectName">Nombre del proyecto de IA:</label>
        <input type="text" id="projectName" placeholder="Ej. Optimización de scoring crediticio" required>
        
        <label for="initiativeType">Tipo de iniciativa:</label>
        <select id="initiativeType" required>
          <option value="">Seleccione</option>
          <option value="ML">Machine Learning (ML)</option>
          <option value="RPA">Robotic Process Automation (RPA)</option>
          <option value="NLP">Natural Language Processing (NLP)</option>
          <option value="CV">Computer Vision</option>
        </select>
        
        <label for="businessArea">Área de negocio impactada:</label>
        <input type="text" id="businessArea" placeholder="Ej. Crédito, Riesgo, Atención al Cliente" required>
        
        <label for="projectDuration">Duración del proyecto (meses):</label>
        <input type="number" id="projectDuration" placeholder="Ej. 12" required min="1">
      </fieldset>
      
      <!-- Sección 2: Costos de Implementación -->
      <fieldset>
        <legend>2. Costos de Implementación</legend>
        
        <label for="softwareLicenses">Licencias de software/cloud (MXN):</label>
        <input type="number" id="softwareLicenses" step="0.01" placeholder="Ej. 500000" required min="0">
        
        <label for="developmentCost">Desarrollo e integración (MXN):</label>
        <input type="number" id="developmentCost" step="0.01" placeholder="Ej. 750000" required min="0">
        
        <label for="trainingCost">Capacitación y change management (MXN):</label>
        <input type="number" id="trainingCost" step="0.01" placeholder="Ej. 200000" required min="0">
        
        <label for="infrastructureCost">Infraestructura y hardware (MXN):</label>
        <input type="number" id="infrastructureCost" step="0.01" placeholder="Ej. 300000" required min="0">
        
        <label for="consultingCost">Consultoría externa (MXN):</label>
        <input type="number" id="consultingCost" step="0.01" placeholder="Ej. 150000" required min="0">
        
        <label for="complianceCost">Costos de validación y compliance (MXN):</label>
        <input type="number" id="complianceCost" step="0.01" placeholder="Ej. 100000" required min="0">
      </fieldset>
      
      <!-- Sección 3: Beneficios Esperados -->
      <fieldset>
        <legend>3. Beneficios Esperados</legend>
        
        <label for="operationalSavings">Reducción de costos operativos (MXN):</label>
        <input type="number" id="operationalSavings" step="0.01" placeholder="Ej. 800000" required min="0">
        
        <label for="revenueIncrease">Incremento en ingresos (MXN):</label>
        <input type="number" id="revenueIncrease" step="0.01" placeholder="Ej. 1200000" required min="0">
        
        <label for="productivityImprovement">Mejora en productividad (%):</label>
        <input type="number" id="productivityImprovement" step="0.01" placeholder="Ej. 15" required min="0">
        
        <label for="riskReduction">Reducción de riesgos/pérdidas (MXN):</label>
        <input type="number" id="riskReduction" step="0.01" placeholder="Ej. 300000" required min="0">
        
        <label for="customerExp">Mejora en experiencia del cliente (valor intangibles cuantificados):</label>
        <input type="number" id="customerExp" step="0.01" placeholder="Ej. 500000" required min="0">
        
        <label for="intangibles">Beneficios intangibles cuantificados (MXN):</label>
        <input type="number" id="intangibles" step="0.01" placeholder="Ej. 250000" required min="0">
      </fieldset>
      
      <!-- Sección 4: Parámetros Financieros -->
      <fieldset>
        <legend>4. Parámetros Financieros</legend>
        <p>Defina los siguientes parámetros considerando la realidad bancaria mexicana:</p>
        
        <label for="discountRate">Tasa de descuento (ej. TIIE/CETES en %):</label>
        <input type="number" id="discountRate" step="0.01" placeholder="Ej. 8.5" required min="0">
        
        <label for="forecastYears">Años de proyección:</label>
        <input type="number" id="forecastYears" placeholder="Ej. 5" required min="1">
      </fieldset>
      
      <div class="button-container">
        <button type="button" id="calculateBtn">Calcular</button>
        <button type="reset">Reiniciar formulario</button>
      </div>
      
    </form>
    
    <!-- Resultados y visualizaciones -->
    <div id="results">
      <h2>Resultados del Análisis Financiero</h2>
      <div id="financialResults"></div>
    </div>
    
    <canvas id="roiChart" width="600" height="300"></canvas>
    
    <!-- Botones para exportar resultados (simulados) -->
    <div class="button-container">
      <button id="exportPDF">Exportar a PDF</button>
      <button id="exportExcel">Exportar a Excel</button>
    </div>
    
    <!-- ====================================
         Lógica JavaScript para cálculos y gráficos 
         ==================================== -->
    <script>
      // =============================
      // Utilidades Financieras
      // =============================
      
      /**
       * Suma todos los costos dados en el formulario
       */
      function totalCost() {
        var software = parseFloat(document.getElementById("softwareLicenses").value) || 0;
        var dev = parseFloat(document.getElementById("developmentCost").value) || 0;
        var training = parseFloat(document.getElementById("trainingCost").value) || 0;
        var infra = parseFloat(document.getElementById("infrastructureCost").value) || 0;
        var consulting = parseFloat(document.getElementById("consultingCost").value) || 0;
        var compliance = parseFloat(document.getElementById("complianceCost").value) || 0;
        return software + dev + training + infra + consulting + compliance;
      }
      
      /**
       * Suma todos los beneficios esperados
       */
      function totalBenefits() {
        var savings = parseFloat(document.getElementById("operationalSavings").value) || 0;
        var revenue = parseFloat(document.getElementById("revenueIncrease").value) || 0;
        var risk = parseFloat(document.getElementById("riskReduction").value) || 0;
        var customer = parseFloat(document.getElementById("customerExp").value) || 0;
        var intangibles = parseFloat(document.getElementById("intangibles").value) || 0;
        // Se incluye la mejora en productividad como porcentaje sobre ingresos estimados
        var productivity = parseFloat(document.getElementById("productivityImprovement").value) || 0;
        var additional = (revenue * (productivity / 100));
        
        return savings + revenue + risk + customer + intangibles + additional;
      }
      
      /** 
       * Calcula el ROI simple: (Beneficios – Costos) / Costos 
       */
      function calculateSimpleROI(totalBenefits, totalCost) {
        if(totalCost === 0) return 0;
        return ((totalBenefits - totalCost) / totalCost) * 100;
      }
      
      /**
       * Calcula el ROI compuesto considerando la tasa de descuento y la duración del proyecto
       * Se asume un flujo anual constante basado en la diferencia anual entre beneficios y costos (distribuidos uniformemente)
       */
      function calculateCompoundROI(totalBenefits, totalCost, discountRate, forecastYears) {
        var annualNet = (totalBenefits - totalCost) / forecastYears;
        var compound = 0;
        for (var year = 1; year <= forecastYears; year++) {
          compound += annualNet / Math.pow((1 + discountRate / 100), year);
        }
        return compound;
      }
      
      /**
       * Calcula el Valor Actual Neto (VAN)
       * Se utiliza el flujo neto anual (suponemos que se distribuyen linealmente)
       */
      function calculateNPV(totalBenefits, totalCost, discountRate, forecastYears) {
        var annualNet = (totalBenefits - totalCost) / forecastYears;
        var npv = -totalCost;
        for (var i = 1; i <= forecastYears; i++) {
          npv += annualNet / Math.pow(1 + discountRate / 100, i);
        }
        return npv;
      }
      
      /**
       * Método iterativo para calcular la TIR (Tasa Interna de Retorno)
       * Se utiliza el método de aproximación incremental
       */
      function calculateIRR(totalBenefits, totalCost, forecastYears) {
        var guess = 0;
        var npv = 0;
        var increment = 0.0001;
        do {
          npv = -totalCost;
          var annualNet = (totalBenefits - totalCost) / forecastYears;
          for (var i = 1; i <= forecastYears; i++) {
            npv += annualNet / Math.pow(1 + guess, i);
          }
          guess += increment;
          // Si se alcanza un límite, se sale
          if (guess > 1) break;
        } while (Math.abs(npv) > 0.001);
        return (guess - increment) * 100;
      }
      
      /**
       * Calcula el periodo de payback (tiempo para recuperar la inversión)
       * Se calcula acumulando el flujo anual hasta cubrir el costo total
       */
      function calculatePaybackPeriod(totalBenefits, totalCost, forecastYears) {
        var annualNet = (totalBenefits - totalCost) / forecastYears;
        var cumulative = 0;
        var period = 0;
        while (cumulative < totalCost && period < forecastYears) {
          cumulative += annualNet;
          period++;
        }
        return period; // en años
      }
      
      // =============================
      // Gestión de Resultados y Visualización
      // =============================
      
      var roiChartInstance = null;
      
      function updateChart(dataLabels, dataValues) {
        var ctx = document.getElementById("roiChart").getContext("2d");
        if (roiChartInstance !== null) {
          roiChartInstance.destroy();
        }
        roiChartInstance = new Chart(ctx, {
          type: "line",
          data: {
            labels: dataLabels,
            datasets: [{
              label: "ROI Proyectado (MXN)",
              data: dataValues,
              backgroundColor: "rgba(0,86,179,0.2)",
              borderColor: "rgba(0,86,179,1)",
              borderWidth: 2,
              fill: true
            }]
          },
          options: {
            responsive: true,
            scales: {
              y: {
                beginAtZero: true,
                ticks: {
                  callback: function(value) {
                    return value.toLocaleString("es-MX", { style: "currency", currency: "MXN" });
                  }
                }
              }
            }
          }
        });
      }
      
      /**
       * Prepara datos para visualización del ROI en escenarios:
       * optimista, esperado y pesimista.
       * Se simulan escenarios modificando ligeramente los beneficios.
       */
      function prepareChartData(totalBenefits, totalCost, discountRate, forecastYears) {
        var baseNPV = calculateNPV(totalBenefits, totalCost, discountRate, forecastYears);
        var optimisticNPV = calculateNPV(totalBenefits * 1.1, totalCost, discountRate, forecastYears);
        var pessimisticNPV = calculateNPV(totalBenefits * 0.9, totalCost, discountRate, forecastYears);
        
        var labels = [];
        var values = [];
        for (var i = 1; i <= forecastYears; i++) {
          labels.push("Año " + i);
          // Se interpola el valor de NPV en cada año (para efectos de gráfico)
          var npvYear = -totalCost;
          var annualNet = (totalBenefits - totalCost) / forecastYears;
          for (var j = 1; j <= i; j++) {
            npvYear += annualNet / Math.pow(1 + discountRate / 100, j);
          }
          values.push(npvYear);
        }
        return {labels: labels, values: values, baseNPV: baseNPV, optimisticNPV: optimisticNPV, pessimisticNPV: pessimisticNPV};
      }
      
      // =============================
      // Manejo de Eventos y Cálculos en Tiempo Real
      // =============================
      
      document.getElementById("calculateBtn").addEventListener("click", function() {
        // Validación de entradas: aseguramos que todos los campos estén completos
        if (!document.getElementById("roiForm").checkValidity()) {
          alert("Por favor, complete todos los campos requeridos.");
          return;
        }
        
        // Recolección de datos
        var discountRate = parseFloat(document.getElementById("discountRate").value);
        var forecastYears = parseInt(document.getElementById("forecastYears").value);
        var total_cost = totalCost();
        var total_benefits = totalBenefits();
        
        // Cálculos básicos
        var simpleROI = calculateSimpleROI(total_benefits, total_cost);
        var compoundROI = calculateCompoundROI(total_benefits, total_cost, discountRate, forecastYears);
        var npv = calculateNPV(total_benefits, total_cost, discountRate, forecastYears);
        var irr = calculateIRR(total_benefits, total_cost, forecastYears);
        var payback = calculatePaybackPeriod(total_benefits, total_cost, forecastYears);
        
        // Preparar información adicional
        var chartData = prepareChartData(total_benefits, total_cost, discountRate, forecastYears);
        
        // Construir la salida en la sección de resultados
        var resultsHTML = "";
        resultsHTML += "<div class=\\"result-line\\"><strong>Costos Totales:</strong> " + total_cost.toLocaleString("es-MX", { style: "currency", currency: "MXN" }) + "</div>";
        resultsHTML += "<div class=\\"result-line\\"><strong>Beneficios Totales:</strong> " + total_benefits.toLocaleString("es-MX", { style: "currency", currency: "MXN" }) + "</div>";
        resultsHTML += "<div class=\\"result-line\\"><strong>ROI Simple:</strong> " + simpleROI.toFixed(2) + "%</div>";
        resultsHTML += "<div class=\\"result-line\\"><strong>ROI Compuesto (Valor Descontado):</strong> " + compoundROI.toLocaleString("es-MX", { style: "currency", currency: "MXN" }) + "</div>";
        resultsHTML += "<div class=\\"result-line\\"><strong>VAN (Valor Actual Neto):</strong> " + npv.toLocaleString("es-MX", { style: "currency", currency: "MXN" }) + "</div>";
        resultsHTML += "<div class=\\"result-line\\"><strong>TIR (Tasa Interna de Retorno):</strong> " + irr.toFixed(2) + "%</div>";
        resultsHTML += "<div class=\\"result-line\\"><strong>Periodo de Payback:</strong> " + payback + " año(s)</div>";
        resultsHTML += "<div class=\\"result-line\\"><strong>Escenarios - VAN Base / Optimista / Pesimista:</strong> " + chartData.baseNPV.toLocaleString("es-MX", { style: "currency", currency: "MXN" }) + " / " + chartData.optimisticNPV.toLocaleString("es-MX", { style: "currency", currency: "MXN" }) + " / " + chartData.pessimisticNPV.toLocaleString("es-MX", { style: "currency", currency: "MXN" }) + "</div>";
        
        document.getElementById("financialResults").innerHTML = resultsHTML;
        
        // Actualizar gráfico
        updateChart(chartData.labels, chartData.values);
      });
      
      // =============================
      // Funcionalidades de Exportación (simuladas)
      // =============================
      
      document.getElementById("exportPDF").addEventListener("click", function() {
        // Aquí se integraría una librería para exportar a PDF (ej. jsPDF),
        // por simulación se muestra un alert
        alert("Exportación a PDF simulada. (Se integraría jsPDF en producción)");
      });
      
      document.getElementById("exportExcel").addEventListener("click", function() {
        // Simulación de exportación a Excel
        alert("Exportación a Excel simulada. (Se integraría SheetJS en producción)");
      });
      
      // ====================================
      // Ejemplos pre-cargados para Casos de Uso Bancarios
      // ====================================
      function loadExample(exampleType) {
        // Si se selecciona un ejemplo se precargan los valores
        switch(exampleType) {
          case "scoring":
            document.getElementById("projectName").value = "Optimización de Scoring Crediticio";
            document.getElementById("initiativeType").value = "ML";
            document.getElementById("businessArea").value = "Crédito";
            document.getElementById("projectDuration").value = 12;
            document.getElementById("softwareLicenses").value = 400000;
            document.getElementById("developmentCost").value = 600000;
            document.getElementById("trainingCost").value = 150000;
            document.getElementById("infrastructureCost").value = 250000;
            document.getElementById("consultingCost").value = 100000;
            document.getElementById("complianceCost").value = 80000;
            document.getElementById("operationalSavings").value = 700000;
            document.getElementById("revenueIncrease").value = 1000000;
            document.getElementById("productivityImprovement").value = 10;
            document.getElementById("riskReduction").value = 200000;
            document.getElementById("customerExp").value = 300000;
            document.getElementById("intangibles").value = 150000;
            document.getElementById("discountRate").value = 8;
            document.getElementById("forecastYears").value = 5;
            break;
          case "aml":
            document.getElementById("projectName").value = "Detección de Transacciones Sospechosas (AML)";
            document.getElementById("initiativeType").value = "ML";
            document.getElementById("businessArea").value = "Cumplimiento";
            document.getElementById("projectDuration").value = 10;
            document.getElementById("softwareLicenses").value = 350000;
            document.getElementById("developmentCost").value = 500000;
            document.getElementById("trainingCost").value = 120000;
            document.getElementById("infrastructureCost").value = 200000;
            document.getElementById("consultingCost").value = 90000;
            document.getElementById("complianceCost").value = 60000;
            document.getElementById("operationalSavings").value = 600000;
            document.getElementById("revenueIncrease").value = 800000;
            document.getElementById("productivityImprovement").value = 12;
            document.getElementById("riskReduction").value = 250000;
            document.getElementById("customerExp").value = 200000;
            document.getElementById("intangibles").value = 100000;
            document.getElementById("discountRate").value = 7.5;
            document.getElementById("forecastYears").value = 5;
            break;
          case "chatbot":
            document.getElementById("projectName").value = "Chatbot Asistente Virtual para Clientes";
            document.getElementById("initiativeType").value = "NLP";
            document.getElementById("businessArea").value = "Atención al Cliente";
            document.getElementById("projectDuration").value = 9;
            document.getElementById("softwareLicenses").value = 300000;
            document.getElementById("developmentCost").value = 550000;
            document.getElementById("trainingCost").value = 100000;
            document.getElementById("infrastructureCost").value = 180000;
            document.getElementById("consultingCost").value = 80000;
            document.getElementById("complianceCost").value = 50000;
            document.getElementById("operationalSavings").value = 500000;
            document.getElementById("revenueIncrease").value = 900000;
            document.getElementById("productivityImprovement").value = 14;
            document.getElementById("riskReduction").value = 150000;
            document.getElementById("customerExp").value = 400000;
            document.getElementById("intangibles").value = 120000;
            document.getElementById("discountRate").value = 8.5;
            document.getElementById("forecastYears").value = 5;
            break;
          case "rpa":
            document.getElementById("projectName").value = "Automatización de Procesos Operativos (RPA)";
            document.getElementById("initiativeType").value = "RPA";
            document.getElementById("businessArea").value = "Operaciones";
            document.getElementById("projectDuration").value = 8;
            document.getElementById("softwareLicenses").value = 250000;
            document.getElementById("developmentCost").value = 450000;
            document.getElementById("trainingCost").value = 80000;
            document.getElementById("infrastructureCost").value = 150000;
            document.getElementById("consultingCost").value = 70000;
            document.getElementById("complianceCost").value = 40000;
            document.getElementById("operationalSavings").value = 650000;
            document.getElementById("revenueIncrease").value = 850000;
            document.getElementById("productivityImprovement").value = 18;
            document.getElementById("riskReduction").value = 220000;
            document.getElementById("customerExp").value = 250000;
            document.getElementById("intangibles").value = 90000;
            document.getElementById("discountRate").value = 7;
            document.getElementById("forecastYears").value = 5;
            break;
          default:
            break;
        }
      }
      
      // ====================================
      // Carga de Ejemplos Pre-cargados al seleccionar opción
      // ====================================
      // Se agregan botones para cargar ejemplos predefinidos
      
      function createExampleButtons() {
        var exampleContainer = document.createElement("div");
        exampleContainer.style.marginTop = "20px";
        exampleContainer.innerHTML = "<h3>Ejemplos Pre-Cargados:</h3>";
        
        var btnScoring = document.createElement("button");
        btnScoring.type = "button";
        btnScoring.textContent = "Caso Scoring";
        btnScoring.style.marginRight = "10px";
        btnScoring.addEventListener("click", function() { loadExample("scoring"); });
        
        var btnAML = document.createElement("button");
        btnAML.type = "button";
        btnAML.textContent = "Caso AML";
        btnAML.style.marginRight = "10px";
        btnAML.addEventListener("click", function() { loadExample("aml"); });
        
        var btnChatbot = document.createElement("button");
        btnChatbot.type = "button";
        btnChatbot.textContent = "Caso Chatbot";
        btnChatbot.style.marginRight = "10px";
        btnChatbot.addEventListener("click", function() { loadExample("chatbot"); });
        
        var btnRPA = document.createElement("button");
        btnRPA.type = "button";
        btnRPA.textContent = "Caso RPA";
        btnRPA.addEventListener("click", function() { loadExample("rpa"); });
        
        exampleContainer.appendChild(btnScoring);
        exampleContainer.appendChild(btnAML);
        exampleContainer.appendChild(btnChatbot);
        exampleContainer.appendChild(btnRPA);
        
        document.getElementById("roiForm").appendChild(exampleContainer);
      }
      
      // Inicialización de botones de ejemplo
      createExampleButtons();
      
      
      // ====================================
      // Validaciones y mensajes en tiempo real
      // ====================================
      function attachRealtimeValidation() {
        var inputs = document.querySelectorAll("#roiForm input");
        inputs.forEach(function(input) {
          input.addEventListener("input", function() {
            // Validación mínima: mostrar borde rojo si valor negativo
            if (parseFloat(input.value) < 0) {
              input.style.borderColor = "red";
            } else {
              input.style.borderColor = "#ccc";
            }
          });
        });
      }
      
      attachRealtimeValidation();
    </script>
  </body>
</html>' width="100%" height="1800" style="border: none; border-radius: 8px;">
  </iframe>
</div>

## 📈 Características de la Calculadora

### Indicadores Financieros Calculados

| Indicador | Descripción | Fórmula |
|-----------|-------------|---------|
| **ROI Simple** | Retorno sobre la inversión básico | (Beneficios - Costos) / Costos × 100 |
| **ROI Compuesto** | ROI considerando valor del dinero en el tiempo | Suma de flujos descontados |
| **VAN** | Valor Actual Neto del proyecto | -I₀ + Σ(Fₙ/(1+r)ⁿ) |
| **TIR** | Tasa Interna de Retorno | Tasa donde VAN = 0 |
| **Payback Period** | Tiempo de recuperación de inversión | Años hasta flujo acumulado ≥ inversión |
| **Análisis de Sensibilidad** | Escenarios optimista/pesimista | VAN con ±10% en beneficios |

### Casos de Uso Pre-configurados

!!! tip "Ejemplos Bancarios Disponibles"
    La calculadora incluye configuraciones pre-cargadas para:
    
    - **Scoring Crediticio**: Optimización de modelos de riesgo
    - **AML/PLD**: Detección de transacciones sospechosas
    - **Chatbot**: Asistente virtual para atención al cliente
    - **RPA**: Automatización de procesos operativos

## 🎯 Guía de Uso

### 1. Información del Proyecto

Complete los datos básicos del proyecto de IA:
- Nombre descriptivo del proyecto
- Tipo de tecnología (ML, RPA, NLP, Computer Vision)
- Área de negocio impactada
- Duración estimada en meses

### 2. Costos de Implementación

Ingrese todos los costos asociados:
- **Licencias**: Software, cloud, herramientas
- **Desarrollo**: Programación e integración
- **Capacitación**: Training y gestión del cambio
- **Infraestructura**: Servidores, hardware
- **Consultoría**: Expertos externos
- **Compliance**: Validación y cumplimiento regulatorio

### 3. Beneficios Esperados

Cuantifique los beneficios del proyecto:
- **Ahorros operativos**: Reducción de costos directos
- **Incremento de ingresos**: Nuevas oportunidades de negocio
- **Productividad**: Mejora porcentual en eficiencia
- **Reducción de riesgos**: Mitigación de pérdidas
- **Experiencia del cliente**: Valor cuantificado de mejoras
- **Intangibles**: Otros beneficios monetizados

### 4. Parámetros Financieros

Configure los parámetros de evaluación:
- **Tasa de descuento**: Basada en TIIE/CETES actual
- **Años de proyección**: Horizonte de evaluación (típicamente 3-5 años)

## 📊 Interpretación de Resultados

### Criterios de Decisión

| Indicador | Criterio de Aceptación | Interpretación |
|-----------|------------------------|----------------|
| **VAN** | > 0 | Proyecto genera valor |
| **TIR** | > Tasa de descuento | Rentabilidad superior al costo de capital |
| **ROI** | > 30% | Alto retorno sobre inversión |
| **Payback** | < 2 años | Recuperación rápida de inversión |

### Benchmarks de la Industria Bancaria

Según estudios de McKinsey y Gartner para banca mexicana:

- **Proyectos ML/Scoring**: ROI promedio 45-60%
- **Iniciativas RPA**: ROI promedio 30-40%
- **Chatbots/NLP**: ROI promedio 35-50%
- **Computer Vision**: ROI promedio 25-35%

## 🔗 Integración con Framework IMPACT

La calculadora ROI se alinea con las métricas del Framework IMPACT:

```mermaid
graph LR
    A[Calculadora ROI] --> B[Implementation]
    A --> C[Momentum]
    A --> D[Performance]
    A --> E[Acceptance]
    A --> F[Cost-Effective]
    A --> G[Trust]
    
    B --> H[Tiempo de implementación]
    C --> I[Proyectos evaluados/mes]
    D --> J[ROI real vs proyectado]
    E --> K[Tasa de aprobación]
    F --> L[Eficiencia de costos]
    G --> M[Cumplimiento regulatorio]
```

## 💡 Mejores Prácticas

### Para Maximizar el ROI

1. **Identificación clara de beneficios**
   - Cuantifique todos los beneficios tangibles
   - Monetice beneficios intangibles cuando sea posible
   - Considere beneficios indirectos y de largo plazo

2. **Estimación conservadora de costos**
   - Incluya costos ocultos (mantenimiento, actualizaciones)
   - Considere costos de cambio organizacional
   - Agregue buffer del 15-20% para contingencias

3. **Validación con stakeholders**
   - Revise estimaciones con áreas de negocio
   - Obtenga aprobación de Risk y Compliance
   - Documente supuestos y limitaciones

4. **Monitoreo post-implementación**
   - Compare ROI proyectado vs real
   - Ajuste modelos para futuros proyectos
   - Documente lecciones aprendidas

## 📚 Referencias y Recursos

### Metodologías Financieras
- **WACC**: Weighted Average Cost of Capital para banca
- **CAPM**: Capital Asset Pricing Model ajustado
- **Monte Carlo**: Simulación para análisis de riesgo

### Fuentes de Datos
- **Banxico**: Tasas de referencia (TIIE, CETES)
- **CNBV**: Benchmarks del sector bancario
- **ABM**: Estudios de transformación digital

## 🆘 Soporte

Para dudas sobre el uso de la calculadora ROI:

- **Email**: roi-calculator@novasolutionsystems.com
- **Teams**: Canal #roi-iniciativas-ia
- **Wiki**: wiki.novasolutionsystems.com/roi-calculator
- **Helpdesk CoE**: Ext. 4242

---

*Calculadora ROI v2.0 | Centro de Excelencia de IA | Última actualización: 09 de enero de 2025*