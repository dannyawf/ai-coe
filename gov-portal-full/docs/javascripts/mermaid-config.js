// Mermaid configuration for MkDocs Material
document$.subscribe(function() {
  // Check if mermaid is available
  if (typeof mermaid === 'undefined') {
    console.warn('Mermaid library not loaded');
    return;
  }

  // Configure mermaid
  mermaid.initialize({
    startOnLoad: false,
    theme: 'default',
    themeVariables: {
      primaryColor: '#667eea',
      primaryTextColor: '#ffffff',
      primaryBorderColor: '#5a67d8',
      lineColor: '#5a67d8',
      secondaryColor: '#764ba2',
      tertiaryColor: '#f7fafc',
      background: '#ffffff',
      mainBkg: '#667eea',
      secondBkg: '#764ba2',
      tertiaryBkg: '#f7fafc'
    },
    flowchart: {
      htmlLabels: true,
      curve: 'basis'
    },
    securityLevel: 'loose'
  });

  // Find and render all mermaid blocks
  const mermaidBlocks = document.querySelectorAll('pre > code.language-mermaid');
  
  mermaidBlocks.forEach((element, index) => {
    try {
      // Get the mermaid code
      const graphDefinition = element.textContent;
      
      // Create container for the diagram
      const container = document.createElement('div');
      container.className = 'mermaid';
      container.setAttribute('data-processed', 'false');
      
      // Generate unique ID
      const id = `mermaid-${Date.now()}-${index}`;
      container.id = id;
      
      // Replace the code block with the container
      const pre = element.parentElement;
      pre.parentElement.insertBefore(container, pre);
      pre.style.display = 'none';
      
      // Render the diagram
      mermaid.render(id, graphDefinition).then(function(result) {
        container.innerHTML = result.svg;
        container.setAttribute('data-processed', 'true');
      }).catch(function(error) {
        console.error('Mermaid rendering error:', error);
        // Show error message
        container.innerHTML = `
          <div style="color: red; padding: 10px; border: 1px solid red; border-radius: 5px;">
            <strong>Error rendering diagram:</strong><br>
            ${error.message || 'Unknown error'}
          </div>
        `;
        // Show original code
        pre.style.display = 'block';
      });
      
    } catch (error) {
      console.error('Error processing mermaid block:', error);
    }
  });
});