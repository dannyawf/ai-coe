#!/bin/bash

echo "Verificando archivos faltantes en mkdocs.yml..."
echo "============================================"

# Lista de archivos a verificar manualmente
files=(
  "academy/guia-desarrolladores-ia.md"
  "academy/guia-risk-officers-ia.md"
  "playbooks/playbook-risk-management-ia.md"
  "playbooks/playbook-customer-service-ia.md"
)

for file in "${files[@]}"; do
  if [ ! -f "docs/$file" ]; then
    echo "❌ FALTA: $file"
    base=$(basename "$file")
    alt=$(find docs -name "$base" 2>/dev/null | head -1)
    if [ ! -z "$alt" ]; then
      echo "   ✓ Existe en: ${alt#docs/}"
    fi
  fi
done