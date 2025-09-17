#!/usr/bin/env python3
"""
Verifica que todos los archivos referenciados en mkdocs.yml existen
"""

import os
import yaml
import re

def extract_md_files(nav_item):
    """Extrae recursivamente todos los archivos .md de la navegación"""
    md_files = []

    if isinstance(nav_item, dict):
        for key, value in nav_item.items():
            if isinstance(value, str) and value.endswith('.md'):
                md_files.append(value)
            else:
                md_files.extend(extract_md_files(value))
    elif isinstance(nav_item, list):
        for item in nav_item:
            md_files.extend(extract_md_files(item))

    return md_files

def main():
    # Leer mkdocs.yml
    with open('mkdocs.yml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # Extraer todos los archivos .md de la navegación
    nav = config.get('nav', [])
    md_files = extract_md_files(nav)

    # Verificar cada archivo
    missing_files = []
    existing_files = []

    for file_path in md_files:
        if file_path.endswith('.html'):
            continue  # Skip HTML files

        full_path = os.path.join('docs', file_path)
        if os.path.exists(full_path):
            existing_files.append(file_path)
        else:
            missing_files.append(file_path)

    # Reportar resultados
    print(f"Total de archivos en navegación: {len(md_files)}")
    print(f"Archivos existentes: {len(existing_files)}")
    print(f"Archivos faltantes: {len(missing_files)}")

    if missing_files:
        print("\n❌ Archivos FALTANTES (causan 404):")
        print("-" * 50)
        for file in missing_files:
            print(f"  - {file}")
            # Buscar alternativas
            base_name = os.path.basename(file)
            alt_search = os.popen(f"find docs -name '{base_name}' 2>/dev/null").read().strip()
            if alt_search:
                alternatives = alt_search.replace('docs/', '').split('\n')
                print(f"    → Alternativas encontradas: {', '.join(alternatives)}")

    print("\n📋 Resumen de correcciones sugeridas:")
    print("-" * 50)
    corrections = {}

    for missing in missing_files:
        base_name = os.path.basename(missing)
        alt_search = os.popen(f"find docs -name '{base_name}' 2>/dev/null").read().strip()
        if alt_search:
            alt_path = alt_search.replace('docs/', '').split('\n')[0]
            corrections[missing] = alt_path

    for old, new in corrections.items():
        print(f"  {old}")
        print(f"  → {new}\n")

    return missing_files, corrections

if __name__ == "__main__":
    missing, corrections = main()