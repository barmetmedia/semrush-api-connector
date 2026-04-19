---
name: semrush-api-connector
description: Skill para conectarse a la API de SEMrush y extraer datos SEO y de palabras clave. Úsala cuando necesites obtener métricas de dominios, volumen de búsquedas, dificultad de keywords o analizar competidores en SEMrush de forma programática.
license: Complete terms in LICENSE.txt
---

# SEMrush API Connector

Esta skill proporciona las herramientas y la configuración necesarias para interactuar con la API de SEMrush, permitiendo la extracción automatizada de datos SEO como métricas de dominio, análisis de palabras clave y datos de competidores.

## Cuándo usar esta skill

Utiliza esta skill cuando necesites:
1. Extraer palabras clave posicionadas para un dominio específico (competidores o dominios propios).
2. Obtener volúmenes de búsqueda, CPC y nivel de competencia de palabras clave específicas.
3. Automatizar la extracción de datos SEO para reportes o análisis en el proyecto BarmetMedia.

## Requisitos Previos

Para utilizar esta skill, necesitas la API key de SEMrush. Si estás trabajando en el contexto del proyecto BarmetMedia, la API key de SEMrush es `224f9256bfdf174c497f0de10493d110`.

## Funcionalidades Principales

La API de SEMrush devuelve datos en formato CSV para los endpoints de SEO. Esta skill incluye un script en Python (`semrush_client.py`) que facilita la realización de peticiones a la API y convierte automáticamente las respuestas CSV a JSON para su análisis.

### 1. Análisis de Dominio (Domain Overview)

Permite obtener métricas clave de un dominio específico en una base de datos regional (ej. `es` para España, `us` para Estados Unidos).

- **Endpoint**: `https://api.semrush.com/?type=domain_organic`
- **Uso común**: Extraer las palabras clave por las que un dominio posiciona orgánicamente, incluyendo volumen de búsqueda, posición y tráfico estimado.

### 2. Análisis de Palabras Clave (Keyword Overview)

Proporciona un resumen detallado de una o varias palabras clave, incluyendo volumen de búsqueda, Coste por Clic (CPC) y nivel de competencia.

- **Endpoint**: `https://api.semrush.com/?type=phrase_this` (una base de datos) o `phrase_all` (todas las bases de datos)
- **Uso común**: Evaluar la viabilidad de nuevas palabras clave para estrategias de contenido.

## Cómo Usar esta Skill

Para realizar consultas a la API de SEMrush, utiliza el script proporcionado en la carpeta `scripts/`.

### Uso del Script `semrush_client.py`

El script principal se encuentra en `/home/ubuntu/skills/semrush-api-connector/scripts/semrush_client.py`. Puedes ejecutarlo desde la terminal usando la herramienta `shell` de la siguiente manera:

```bash
# Para análisis de dominio (Domain Organic Search Keywords)
python3 /home/ubuntu/skills/semrush-api-connector/scripts/semrush_client.py --api-key "TU_API_KEY" --type domain_organic --domain barmetmedia.com --database es --limit 10

# Para análisis de palabra clave (Keyword Overview)
python3 /home/ubuntu/skills/semrush-api-connector/scripts/semrush_client.py --api-key "TU_API_KEY" --type phrase_this --phrase "agencia seo" --database es
```

### Parámetros del Script

- `--api-key`: Tu clave de API de SEMrush (Obligatorio).
- `--type`: Tipo de reporte (`domain_organic`, `phrase_this`, `phrase_all`).
- `--domain`: Dominio a analizar (Requerido para reportes de dominio).
- `--phrase`: Palabra clave a analizar (Requerido para reportes de palabras clave).
- `--database`: Base de datos regional (ej. `es`, `us`, `mx`). Por defecto es `es`.
- `--limit`: Número máximo de resultados a devolver. Por defecto es 10.
- `--columns`: (Opcional) Especificar las columnas a devolver separadas por comas.
- `--format`: (Opcional) Formato de salida (`json` o `csv`). Por defecto es `json`.
- `--output`: (Opcional) Ruta del archivo de salida. Si no se especifica, imprime en consola.

## Buenas Prácticas

1. **Gestión de Unidades de API**: Cada petición consume unidades de la API de SEMrush (generalmente 10 unidades por línea de resultado). Utiliza el parámetro `--limit` para restringir la cantidad de datos y no agotar el saldo innecesariamente.
2. **Manejo de Errores**: Si la API devuelve un error (ej. `ERROR 50 :: NOTHING FOUND`), el script lo capturará y mostrará un mensaje descriptivo.
3. **Bases de Datos Regionales**: Asegúrate de especificar la base de datos correcta (`--database`) para obtener resultados relevantes para el mercado objetivo de BarmetMedia. Por defecto, usa `es` para España.
