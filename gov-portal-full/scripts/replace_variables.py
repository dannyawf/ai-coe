#!/usr/bin/env python3
"""
Script de reemplazo de variables para el Centro de Excelencia AI
Reemplaza todos los tags {{VARIABLE}} con valores del archivo variables.yaml
"""

import os
import re
import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
import shutil
from datetime import datetime

class VariableReplacer:
    """Gestiona el reemplazo de variables en archivos del proyecto"""

    def __init__(self, config_path: str = "config/variables.yaml"):
        """
        Inicializa el replacer con el archivo de configuración

        Args:
            config_path: Ruta al archivo YAML de variables
        """
        self.config_path = config_path
        self.variables = self._load_variables()
        self.replacements = self._flatten_variables()
        self.stats = {
            'files_processed': 0,
            'replacements_made': 0,
            'errors': []
        }

    def _load_variables(self) -> Dict:
        """Carga las variables desde el archivo YAML"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error cargando configuración: {e}")
            return {}

    def _flatten_variables(self) -> Dict[str, str]:
        """
        Convierte la estructura anidada en un diccionario plano de tags

        Returns:
            Dict con formato {"{{TAG_NAME}}": "value"}
        """
        flat = {}

        # Información de la institución
        if 'organization' in self.variables:
            org = self.variables['organization']
            flat['{{BANK_NAME}}'] = org.get('name', '')
            flat['{{BANK_FULL_NAME}}'] = org.get('full_name', '')
            flat['{{BANK_SHORT}}'] = org.get('short_name', '')
            flat['{{BANK_DOMAIN}}'] = org.get('domain', '')
            flat['{{BANK_WEBSITE}}'] = org.get('website', '')

        # Centro de Excelencia
        if 'coe' in self.variables:
            coe = self.variables['coe']
            flat['{{COE_NAME}}'] = coe.get('name', '')
            flat['{{COE_SHORT}}'] = coe.get('short_name', '')
            flat['{{COE_DEPARTMENT}}'] = coe.get('department', '')

            # Emails del CoE
            if 'emails' in coe:
                flat['{{COE_EMAIL}}'] = coe['emails'].get('general', '')
                flat['{{COE_SUPPORT_EMAIL}}'] = coe['emails'].get('support', '')
                flat['{{COE_ADMIN_EMAIL}}'] = coe['emails'].get('admin', '')
                flat['{{COE_MANAGEMENT_EMAIL}}'] = coe['emails'].get('gerencia', '')
                flat['{{COE_ESCALATION_EMAIL}}'] = coe['emails'].get('escalation', '')

            # Teléfonos
            if 'phones' in coe:
                flat['{{COE_PHONE}}'] = coe['phones'].get('main', '')
                flat['{{COE_EXTENSION}}'] = coe['phones'].get('extension', '')
                flat['{{COE_HOTLINE}}'] = coe['phones'].get('hotline', '')
                flat['{{COE_SUPPORT_EXT}}'] = coe['phones'].get('support', '')

        # Nova-Cell
        if 'nova_cell' in self.variables:
            nova = self.variables['nova_cell']
            flat['{{NOVA_NAME}}'] = nova.get('name', '')
            flat['{{NOVA_VERSION}}'] = nova.get('version', '')

            # Emails Nova
            if 'emails' in nova:
                flat['{{NOVA_SUPPORT_EMAIL}}'] = nova['emails'].get('support', '')
                flat['{{NOVA_CLI_EMAIL}}'] = nova['emails'].get('cli', '')
                flat['{{NOVA_HELP_EMAIL}}'] = nova['emails'].get('help', '')
                flat['{{NOVA_API_EMAIL}}'] = nova['emails'].get('api', '')

            # URLs Nova
            if 'urls' in nova:
                flat['{{NOVA_PORTAL_URL}}'] = nova['urls'].get('portal', '')
                flat['{{NOVA_API_URL}}'] = nova['urls'].get('api', '')
                flat['{{NOVA_DOCS_URL}}'] = nova['urls'].get('docs', '')
                flat['{{NOVA_HUB_URL}}'] = nova['urls'].get('hub', '')

        # IMPACT
        if 'impact' in self.variables:
            flat['{{IMPACT_EMAIL}}'] = self.variables['impact'].get('email', '')
            flat['{{IMPACT_DASHBOARD_URL}}'] = self.variables['impact'].get('dashboard', '')

        # Herramientas
        if 'tools' in self.variables:
            if 'aisia' in self.variables['tools']:
                flat['{{AISIA_EMAIL}}'] = self.variables['tools']['aisia'].get('email', '')
                flat['{{AISIA_URL}}'] = self.variables['tools']['aisia'].get('url', '')
            if 'playbooks' in self.variables['tools']:
                flat['{{PLAYBOOKS_EMAIL}}'] = self.variables['tools']['playbooks'].get('email', '')

        # Comunicación
        if 'communication' in self.variables:
            if 'slack' in self.variables['communication']:
                slack = self.variables['communication']['slack']
                flat['{{SLACK_WORKSPACE}}'] = slack.get('workspace', '')
                flat['{{SLACK_URL}}'] = slack.get('url', '')
                if 'channels' in slack:
                    flat['{{SLACK_GENERAL}}'] = slack['channels'].get('general', '')
                    flat['{{SLACK_SUPPORT}}'] = slack['channels'].get('support', '')
                    flat['{{SLACK_DEV}}'] = slack['channels'].get('dev', '')

            if 'google_chat' in self.variables['communication']:
                flat['{{GCHAT_URL}}'] = self.variables['communication']['google_chat'].get('url', '')
                flat['{{GCHAT_CHANNEL}}'] = self.variables['communication']['google_chat'].get('channel', '')

        # Servicios externos
        if 'external' in self.variables:
            if 'github' in self.variables['external']:
                flat['{{GITHUB_ORG}}'] = self.variables['external']['github'].get('org', '')
                flat['{{GITHUB_URL}}'] = self.variables['external']['github'].get('url', '')
            if 'servicenow' in self.variables['external']:
                flat['{{SERVICENOW_URL}}'] = self.variables['external']['servicenow'].get('instance', '')
            if 'confluence' in self.variables['external']:
                flat['{{CONFLUENCE_URL}}'] = self.variables['external']['confluence'].get('url', '')

        # Compliance
        if 'compliance' in self.variables:
            flat['{{COMPLIANCE_EMAIL}}'] = self.variables['compliance'].get('contact', '')
            if 'regulatory' in self.variables['compliance']:
                flat['{{CNBV_EMAIL}}'] = self.variables['compliance']['regulatory'].get('cnbv', '')
                flat['{{BANXICO_EMAIL}}'] = self.variables['compliance']['regulatory'].get('banxico', '')

        # Ambientes
        if 'environments' in self.variables:
            for env_name, env_data in self.variables['environments'].items():
                prefix = env_name.upper()
                flat[f'{{{{{prefix}_API_URL}}}}'] = env_data.get('api', '')
                flat[f'{{{{{prefix}_DASHBOARD_URL}}}}'] = env_data.get('dashboard', '')
                if 'docs' in env_data:
                    flat[f'{{{{{prefix}_DOCS_URL}}}}'] = env_data.get('docs', '')

        # Legal
        if 'legal' in self.variables:
            legal = self.variables['legal']
            flat['{{LEGAL_NAME}}'] = legal.get('company', '')
            flat['{{CURRENT_YEAR}}'] = legal.get('year', '')
            flat['{{COPYRIGHT}}'] = legal.get('copyright', '')
            flat['{{PRIVACY_URL}}'] = legal.get('privacy_url', '')
            flat['{{TERMS_URL}}'] = legal.get('terms_url', '')

        # Branding
        if 'branding' in self.variables:
            brand = self.variables['branding']
            flat['{{PRIMARY_COLOR}}'] = brand.get('primary_color', '')
            flat['{{SECONDARY_COLOR}}'] = brand.get('secondary_color', '')
            flat['{{LOGO_URL}}'] = brand.get('logo_url', '')
            flat['{{FAVICON_URL}}'] = brand.get('favicon', '')

        return flat

    def find_variables_in_file(self, file_path: str) -> List[str]:
        """
        Encuentra todas las variables {{}} en un archivo

        Args:
            file_path: Ruta del archivo a analizar

        Returns:
            Lista de variables encontradas
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                pattern = r'\{\{[A-Z_]+\}\}'
                return list(set(re.findall(pattern, content)))
        except Exception as e:
            self.stats['errors'].append(f"Error leyendo {file_path}: {e}")
            return []

    def replace_in_file(self, file_path: str, dry_run: bool = False) -> int:
        """
        Reemplaza variables en un archivo

        Args:
            file_path: Ruta del archivo
            dry_run: Si True, solo simula sin modificar

        Returns:
            Número de reemplazos realizados
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = original = f.read()

            replacements = 0
            for tag, value in self.replacements.items():
                if tag in content:
                    occurrences = content.count(tag)
                    content = content.replace(tag, value)
                    replacements += occurrences

            if replacements > 0 and not dry_run:
                # Crear backup
                backup_path = f"{file_path}.backup"
                shutil.copy2(file_path, backup_path)

                # Escribir cambios
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                print(f"✅ {file_path}: {replacements} reemplazos")
            elif replacements > 0:
                print(f"🔍 {file_path}: {replacements} reemplazos (dry-run)")

            return replacements

        except Exception as e:
            self.stats['errors'].append(f"Error procesando {file_path}: {e}")
            return 0

    def process_directory(self, directory: str, patterns: List[str],
                         exclude_dirs: List[str] = None, dry_run: bool = False):
        """
        Procesa todos los archivos en un directorio

        Args:
            directory: Directorio a procesar
            patterns: Patrones de archivos (ej: ['*.md', '*.yaml'])
            exclude_dirs: Directorios a excluir
            dry_run: Si True, solo simula
        """
        exclude_dirs = exclude_dirs or ['node_modules', '.git', '__pycache__', 'dist', 'build']
        path = Path(directory)

        for pattern in patterns:
            for file_path in path.rglob(pattern):
                # Verificar exclusiones
                if any(exc in str(file_path) for exc in exclude_dirs):
                    continue

                replacements = self.replace_in_file(str(file_path), dry_run)
                self.stats['files_processed'] += 1
                self.stats['replacements_made'] += replacements

    def generate_report(self) -> str:
        """Genera un reporte del procesamiento"""
        report = f"""
╔════════════════════════════════════════════╗
║     REPORTE DE REEMPLAZO DE VARIABLES     ║
╚════════════════════════════════════════════╝

📊 ESTADÍSTICAS:
  • Archivos procesados: {self.stats['files_processed']}
  • Reemplazos totales: {self.stats['replacements_made']}
  • Errores encontrados: {len(self.stats['errors'])}

📝 VARIABLES DISPONIBLES: {len(self.replacements)}
"""

        if self.stats['errors']:
            report += "\n⚠️ ERRORES:\n"
            for error in self.stats['errors']:
                report += f"  • {error}\n"

        return report

    def list_variables(self):
        """Lista todas las variables disponibles"""
        print("\n📋 VARIABLES DISPONIBLES:\n")
        for tag, value in sorted(self.replacements.items()):
            print(f"  {tag:<30} → {value}")


def main():
    """Función principal del script"""
    parser = argparse.ArgumentParser(
        description='Reemplaza variables en archivos del proyecto'
    )
    parser.add_argument(
        '--config',
        default='config/variables.yaml',
        help='Archivo de configuración de variables'
    )
    parser.add_argument(
        '--directory',
        default='.',
        help='Directorio a procesar'
    )
    parser.add_argument(
        '--patterns',
        nargs='+',
        default=['*.md', '*.yaml', '*.yml', '*.tsx', '*.ts', '*.py'],
        help='Patrones de archivos a procesar'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simular sin modificar archivos'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='Listar variables disponibles'
    )
    parser.add_argument(
        '--find',
        metavar='FILE',
        help='Buscar variables en un archivo específico'
    )

    args = parser.parse_args()

    # Crear instancia del replacer
    replacer = VariableReplacer(args.config)

    if args.list:
        # Listar variables
        replacer.list_variables()
    elif args.find:
        # Buscar variables en archivo
        variables = replacer.find_variables_in_file(args.find)
        if variables:
            print(f"\n📍 Variables encontradas en {args.find}:")
            for var in sorted(variables):
                value = replacer.replacements.get(var, '❌ NO DEFINIDA')
                print(f"  {var} → {value}")
        else:
            print(f"No se encontraron variables en {args.find}")
    else:
        # Procesar directorio
        print(f"\n{'🔍 MODO DRY-RUN' if args.dry_run else '🚀 PROCESANDO ARCHIVOS'}\n")
        replacer.process_directory(
            args.directory,
            args.patterns,
            dry_run=args.dry_run
        )
        print(replacer.generate_report())

        if args.dry_run:
            print("\n💡 Ejecuta sin --dry-run para aplicar los cambios\n")


if __name__ == '__main__':
    main()