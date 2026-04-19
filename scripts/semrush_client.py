import argparse
import requests
import csv
import json
import sys
from io import StringIO

def get_semrush_data(api_key, report_type, **kwargs):
    """
    Hace una petición a la API de SEMrush y devuelve los datos.
    """
    base_url = "https://api.semrush.com/"
    
    params = {
        "key": api_key,
        "type": report_type
    }
    
    # Añadir parámetros adicionales
    for k, v in kwargs.items():
        if v is not None:
            params[k] = v
            
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        # Comprobar si la respuesta es un error de SEMrush (ej. ERROR 50 :: NOTHING FOUND)
        if response.text.startswith("ERROR"):
            print(f"Error de SEMrush: {response.text}", file=sys.stderr)
            return None
            
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición HTTP: {e}", file=sys.stderr)
        return None

def csv_to_json(csv_data):
    """Convierte datos CSV a una lista de diccionarios JSON"""
    if not csv_data:
        return []
        
    f = StringIO(csv_data)
    reader = csv.DictReader(f, delimiter=';')
    return list(reader)

def main():
    parser = argparse.ArgumentParser(description="Cliente para la API de SEMrush")
    parser.add_argument("--api-key", required=True, help="Clave de API de SEMrush")
    parser.add_argument("--type", required=True, choices=["domain_organic", "phrase_this", "phrase_all", "phrase_these"], help="Tipo de reporte")
    
    # Parámetros específicos de reportes
    parser.add_argument("--domain", help="Dominio a analizar (requerido para domain_organic)")
    parser.add_argument("--phrase", help="Palabra clave a analizar (requerido para phrase_*)")
    parser.add_argument("--database", default="es", help="Base de datos regional (ej. es, us, mx). Por defecto: es")
    parser.add_argument("--limit", type=int, default=10, help="Número máximo de resultados (display_limit). Por defecto: 10")
    parser.add_argument("--columns", help="Columnas a exportar separadas por coma (export_columns)")
    
    # Opciones de salida
    parser.add_argument("--output", help="Archivo de salida. Si no se especifica, imprime en consola")
    parser.add_argument("--format", choices=["csv", "json"], default="json", help="Formato de salida (csv o json). Por defecto: json")
    
    args = parser.parse_args()
    
    # Validaciones básicas
    if args.type == "domain_organic" and not args.domain:
        parser.error("--domain es requerido para el tipo domain_organic")
    
    if args.type in ["phrase_this", "phrase_all", "phrase_these"] and not args.phrase:
        parser.error("--phrase es requerido para los tipos phrase_*")
        
    # Construir parámetros para la API
    api_params = {}
    
    if args.domain:
        api_params["domain"] = args.domain
        
    if args.phrase:
        api_params["phrase"] = args.phrase
        
    if args.type != "phrase_all":
        api_params["database"] = args.database
        
    if args.limit:
        api_params["display_limit"] = args.limit
        
    if args.columns:
        api_params["export_columns"] = args.columns
        
    # Obtener datos
    print(f"Obteniendo datos de SEMrush para el reporte '{args.type}'...", file=sys.stderr)
    csv_data = get_semrush_data(args.api_key, args.type, **api_params)
    
    if not csv_data:
        sys.exit(1)
        
    # Procesar salida
    if args.format == "json":
        output_data = json.dumps(csv_to_json(csv_data), indent=2, ensure_ascii=False)
    else:
        output_data = csv_data
        
    # Guardar o imprimir
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_data)
        print(f"Datos guardados en {args.output}", file=sys.stderr)
    else:
        print(output_data)

if __name__ == "__main__":
    main()
