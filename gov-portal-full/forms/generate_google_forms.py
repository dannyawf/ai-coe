#!/usr/bin/env python3
"""
Script para generar Google Forms para el Portal CoE IA
Requiere configuración previa de Google Forms API
"""

import json
import os
from typing import Dict, List, Any

# Configuración de formularios
FORMS_CONFIG = {
    "nova-coe-support": {
        "title": "Nova CoE - Solicitud de Apoyo",
        "description": "Solicite apoyo del Centro de Excelencia de IA para su proyecto",
        "fields": [
            {
                "title": "Correo Corporativo",
                "type": "email",
                "required": True,
                "prefilled": "respondentEmail"
            },
            {
                "title": "Tipo de Solicitud",
                "type": "multiple_choice",
                "required": True,
                "options": [
                    "Consultoría Técnica",
                    "Arquitectura de Solución",
                    "Capacitación",
                    "Evaluación de Modelo",
                    "Soporte Nova-Cell",
                    "Otro"
                ]
            },
            {
                "title": "Nombre del Proyecto",
                "type": "short_text",
                "required": True
            },
            {
                "title": "Descripción del Proyecto",
                "type": "long_text",
                "required": True,
                "help_text": "Describa brevemente su proyecto y el tipo de apoyo que necesita"
            },
            {
                "title": "Área/Departamento",
                "type": "dropdown",
                "required": True,
                "options": [
                    "Banca Digital",
                    "Risk Management",
                    "Customer Service",
                    "Operations",
                    "IT/Tecnología",
                    "Innovación",
                    "Compliance",
                    "Otro"
                ]
            },
            {
                "title": "Urgencia",
                "type": "scale",
                "required": True,
                "low_label": "Baja",
                "high_label": "Crítica",
                "scale_max": 5
            },
            {
                "title": "Timeline Esperado",
                "type": "multiple_choice",
                "required": True,
                "options": [
                    "Esta semana",
                    "Próximas 2 semanas",
                    "Este mes",
                    "Próximos 3 meses",
                    "Sin urgencia específica"
                ]
            }
        ]
    },

    "nova-llm-eval": {
        "title": "Nova CoE - Evaluación de Modelos LLM",
        "description": "Solicite una evaluación técnica de modelos de lenguaje para su caso de uso",
        "fields": [
            {
                "title": "Correo Corporativo",
                "type": "email",
                "required": True,
                "prefilled": "respondentEmail"
            },
            {
                "title": "Modelo a Evaluar",
                "type": "checkbox",
                "required": True,
                "options": [
                    "GPT-4",
                    "GPT-3.5 Turbo",
                    "Claude 3",
                    "Llama 2",
                    "Gemini Pro",
                    "Modelo Propio",
                    "Otro"
                ]
            },
            {
                "title": "Caso de Uso Principal",
                "type": "dropdown",
                "required": True,
                "options": [
                    "Chatbot/Asistente Virtual",
                    "Análisis de Documentos",
                    "Generación de Contenido",
                    "Clasificación de Texto",
                    "Extracción de Información",
                    "Traducción",
                    "Resumen Automático",
                    "Q&A sobre Documentos",
                    "Otro"
                ]
            },
            {
                "title": "Volumen de Datos Estimado",
                "type": "multiple_choice",
                "required": True,
                "options": [
                    "< 1,000 documentos",
                    "1,000 - 10,000 documentos",
                    "10,000 - 100,000 documentos",
                    "> 100,000 documentos"
                ]
            },
            {
                "title": "Métricas de Evaluación Requeridas",
                "type": "checkbox",
                "required": True,
                "options": [
                    "Precisión",
                    "Latencia",
                    "Costo por Token",
                    "Seguridad/Privacy",
                    "Sesgo/Fairness",
                    "Explicabilidad",
                    "Robustez"
                ]
            },
            {
                "title": "Presupuesto Mensual Estimado (USD)",
                "type": "multiple_choice",
                "required": False,
                "options": [
                    "< $1,000",
                    "$1,000 - $5,000",
                    "$5,000 - $20,000",
                    "> $20,000",
                    "Por definir"
                ]
            }
        ]
    },

    "nova-aisia": {
        "title": "Nova CoE - Evaluación AISIA",
        "description": "Evalúe la madurez de IA de su organización con el framework AISIA",
        "fields": [
            {
                "title": "Correo Corporativo",
                "type": "email",
                "required": True,
                "prefilled": "respondentEmail"
            },
            {
                "title": "Área a Evaluar",
                "type": "short_text",
                "required": True
            },
            {
                "title": "Adopción - Nivel Actual",
                "type": "scale",
                "required": True,
                "low_label": "Sin adopción",
                "high_label": "Adopción completa",
                "scale_max": 5
            },
            {
                "title": "Impacto - Beneficios Medidos",
                "type": "scale",
                "required": True,
                "low_label": "Sin impacto",
                "high_label": "Alto impacto",
                "scale_max": 5
            },
            {
                "title": "Seguridad - Controles Implementados",
                "type": "scale",
                "required": True,
                "low_label": "Sin controles",
                "high_label": "Controles completos",
                "scale_max": 5
            },
            {
                "title": "Innovación - Capacidad de Experimentación",
                "type": "scale",
                "required": True,
                "low_label": "Sin innovación",
                "high_label": "Altamente innovador",
                "scale_max": 5
            },
            {
                "title": "Alineación - Con Estrategia de Negocio",
                "type": "scale",
                "required": True,
                "low_label": "Sin alineación",
                "high_label": "Totalmente alineado",
                "scale_max": 5
            },
            {
                "title": "Principales Desafíos",
                "type": "checkbox",
                "required": False,
                "options": [
                    "Falta de talento",
                    "Presupuesto limitado",
                    "Resistencia al cambio",
                    "Restricciones regulatorias",
                    "Deuda técnica",
                    "Calidad de datos",
                    "Seguridad/Privacy"
                ]
            }
        ]
    },

    "nova-roi": {
        "title": "Nova CoE - Calculadora ROI",
        "description": "Calcule el retorno de inversión de su iniciativa de IA",
        "fields": [
            {
                "title": "Correo Corporativo",
                "type": "email",
                "required": True,
                "prefilled": "respondentEmail"
            },
            {
                "title": "Nombre del Proyecto",
                "type": "short_text",
                "required": True
            },
            {
                "title": "Costo de Implementación Inicial (USD)",
                "type": "number",
                "required": True
            },
            {
                "title": "Costo Operativo Mensual (USD)",
                "type": "number",
                "required": True
            },
            {
                "title": "Ahorro Mensual Esperado (USD)",
                "type": "number",
                "required": True
            },
            {
                "title": "Incremento de Ingresos Mensual (USD)",
                "type": "number",
                "required": False
            },
            {
                "title": "Número de Usuarios/Clientes Impactados",
                "type": "number",
                "required": True
            },
            {
                "title": "Tiempo de Implementación (meses)",
                "type": "number",
                "required": True
            },
            {
                "title": "Beneficios No Monetarios",
                "type": "checkbox",
                "required": False,
                "options": [
                    "Mejora en satisfacción del cliente",
                    "Reducción de errores",
                    "Mayor velocidad de procesamiento",
                    "Mejor cumplimiento regulatorio",
                    "Innovación en productos",
                    "Ventaja competitiva"
                ]
            }
        ]
    },

    "nova-intake": {
        "title": "Nova CoE - Registro de Proyecto IA",
        "description": "Registre su proyecto de IA para obtener apoyo del CoE",
        "fields": [
            {
                "title": "Correo Corporativo",
                "type": "email",
                "required": True,
                "prefilled": "respondentEmail"
            },
            {
                "title": "Nombre del Proyecto",
                "type": "short_text",
                "required": True
            },
            {
                "title": "Etapa Actual del Proyecto",
                "type": "multiple_choice",
                "required": True,
                "options": [
                    "1. Explorar - Identificando oportunidades",
                    "2. Experimentar - Proof of Concept",
                    "3. Construir - Desarrollo activo",
                    "4. Validar - Testing y QA",
                    "5. Desplegar - Implementación",
                    "6. Escalar - Expansión"
                ]
            },
            {
                "title": "Objetivo Principal",
                "type": "long_text",
                "required": True
            },
            {
                "title": "Tecnologías de IA a Utilizar",
                "type": "checkbox",
                "required": True,
                "options": [
                    "LLMs/GenAI",
                    "Computer Vision",
                    "NLP Clásico",
                    "Machine Learning",
                    "Deep Learning",
                    "Robotic Process Automation",
                    "Speech Recognition",
                    "Otro"
                ]
            },
            {
                "title": "¿Requiere acceso a Nova-Cell?",
                "type": "yes_no",
                "required": True
            },
            {
                "title": "Equipo del Proyecto (nombres y roles)",
                "type": "long_text",
                "required": True
            }
        ]
    }
}

def generate_form_html_embed(form_id: str, height: str = "800") -> str:
    """
    Genera el código HTML para embeber un Google Form
    """
    # URL base de Google Forms (se debe reemplazar con las URLs reales después de crearlos)
    base_url = "https://docs.google.com/forms/d/e/"

    # Placeholder para los IDs reales de Google Forms
    form_urls = {
        "nova-coe-support": f"{base_url}YOUR_FORM_ID_HERE/viewform?embedded=true",
        "nova-llm-eval": f"{base_url}YOUR_FORM_ID_HERE/viewform?embedded=true",
        "nova-aisia": f"{base_url}YOUR_FORM_ID_HERE/viewform?embedded=true",
        "nova-roi": f"{base_url}YOUR_FORM_ID_HERE/viewform?embedded=true",
        "nova-intake": f"{base_url}YOUR_FORM_ID_HERE/viewform?embedded=true",
    }

    if form_id not in form_urls:
        return f"<!-- Form {form_id} not found -->"

    embed_code = f'''
<iframe
    src="{form_urls[form_id]}"
    width="100%"
    height="{height}"
    frameborder="0"
    marginheight="0"
    marginwidth="0"
    style="border: 1px solid #e0e0e0; border-radius: 8px;">
    Cargando formulario...
</iframe>
'''
    return embed_code

def generate_form_config_json():
    """
    Genera configuración JSON para crear los formularios manualmente
    o con Google Apps Script
    """
    output = {
        "forms": [],
        "settings": {
            "requireSignIn": True,
            "collectEmail": True,
            "limitToOrganization": True,
            "sendReceiptEmail": True,
            "progressBar": True,
            "confirmationMessage": "Gracias por su solicitud. El equipo del CoE se pondrá en contacto pronto.",
            "theme": {
                "primaryColor": "#003366",
                "backgroundColor": "#FFFFFF",
                "fontFamily": "Inter"
            }
        }
    }

    for form_id, config in FORMS_CONFIG.items():
        form_data = {
            "id": form_id,
            "title": config["title"],
            "description": config["description"],
            "fields": config["fields"]
        }
        output["forms"].append(form_data)

    return json.dumps(output, indent=2, ensure_ascii=False)

def generate_replacement_map():
    """
    Genera un mapa de reemplazos para actualizar los archivos MD
    """
    replacements = []

    # Mapeo de archivos a formularios
    file_mappings = {
        "/docs/servicios/solicitar-apoyo.md": {
            "old_form_id": "support-request-form",
            "new_form_id": "nova-coe-support"
        },
        "/docs/servicios/evaluacion-modelos-llm.md": {
            "old_form_id": "llm-evaluation-form",
            "new_form_id": "nova-llm-eval"
        },
        "/docs/tools/aisia-assessment.md": {
            "old_form_id": "aisiaForm",
            "new_form_id": "nova-aisia"
        },
        "/docs/tools/roi-calculator.md": {
            "old_form_id": "roiForm",
            "new_form_id": "nova-roi"
        },
        "/docs/start-here.md": {
            "old_form_id": "intake-form",
            "new_form_id": "nova-intake"
        }
    }

    for file_path, mapping in file_mappings.items():
        embed_code = generate_form_html_embed(mapping["new_form_id"])
        replacements.append({
            "file": file_path,
            "old_form_id": mapping["old_form_id"],
            "embed_code": embed_code
        })

    return replacements

def main():
    """
    Función principal
    """
    print("=" * 60)
    print("GENERADOR DE GOOGLE FORMS - NOVA COE")
    print("=" * 60)
    print()

    # Generar configuración JSON
    print("1. Generando configuración JSON para Google Forms...")
    config_json = generate_form_config_json()

    # Guardar configuración
    with open("forms_config.json", "w", encoding="utf-8") as f:
        f.write(config_json)
    print("   ✓ Configuración guardada en forms_config.json")
    print()

    # Generar códigos de embed
    print("2. Generando códigos de embed HTML...")
    replacements = generate_replacement_map()

    # Guardar reemplazos
    with open("form_replacements.json", "w", encoding="utf-8") as f:
        json.dump(replacements, f, indent=2, ensure_ascii=False)
    print("   ✓ Reemplazos guardados en form_replacements.json")
    print()

    # Instrucciones
    print("PRÓXIMOS PASOS:")
    print("-" * 40)
    print("1. Crear los formularios en Google Forms usando la configuración en forms_config.json")
    print("2. Configurar cada formulario con:")
    print("   - Requerir inicio de sesión con cuenta corporativa")
    print("   - Recopilar direcciones de correo automáticamente")
    print("   - Limitar a usuarios de la organización")
    print("   - Activar notificaciones al equipo CoE")
    print("3. Obtener los IDs reales de cada formulario")
    print("4. Actualizar form_urls en este script con los IDs reales")
    print("5. Ejecutar el script de reemplazo para actualizar los archivos MD")
    print()
    print("FORMULARIOS A CREAR:")
    print("-" * 40)
    for form_id, config in FORMS_CONFIG.items():
        print(f"• {config['title']}")
        print(f"  ID: {form_id}")
        print(f"  Campos: {len(config['fields'])}")
        print()

if __name__ == "__main__":
    main()