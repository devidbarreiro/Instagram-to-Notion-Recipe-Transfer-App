
No file chosen

App de Transferencia de Recetas Instagram a Notion
Descripción
Esta aplicación automatiza el proceso de extraer recetas de Instagram Reels y transferirlas a Notion en un formato organizado y atractivo. Utiliza procesamiento de lenguaje natural para identificar ingredientes y pasos de preparación, y clasifica automáticamente las recetas según varios criterios.

Características
Extracción de datos de Instagram Reels (audio y descripción)
Transcripción de audio a texto
Análisis de texto para identificar componentes de la receta
Clasificación automática de recetas
Generación de páginas en Notion con una plantilla atractiva
Interfaz web simple para ingresar URLs de Reels (opcional)
Requisitos del Sistema
Python 3.8+
Cuenta de desarrollador de Instagram (para acceso a la API)
Cuenta de Notion con permisos de integración
Instalación
Clonar el repositorio:

git clone https://github.com/tu-usuario/app-recetas-instagram-notion.git
cd app-recetas-instagram-notion
​
Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
​
Instalar las dependencias:

pip install -r requirements.txt
​
Configurar las variables de entorno:
Crea un archivo .env en el directorio raíz y añade las siguientes variables:

INSTAGRAM_API_KEY=tu_clave_api_de_instagram
NOTION_API_KEY=tu_clave_api_de_notion
NOTION_DATABASE_ID=id_de_tu_base_de_datos_notion
​
Uso
Ejecutar la aplicación:

python src/main.py
​
Si has implementado la interfaz web, accede a ella en http://localhost:5000 (o el puerto que hayas configurado).

Ingresa la URL del Instagram Reel que contiene la receta.

La aplicación procesará el Reel y creará una nueva página en tu base de datos de Notion con la receta extraída y clasificada.

Estructura del Proyecto
src/
│
├── main.py                 # Punto de entrada principal de la aplicación
├── config.py               # Configuraciones globales y variables de entorno
│
├── instagram/
│   ├── __init__.py
│   ├── extractor.py        # Lógica para extraer datos de Instagram Reels
│   └── instagram_api.py    # Wrapper para interacciones con la API de Instagram
│
├── audio/
│   ├── __init__.py
│   ├── transcriber.py      # Lógica para transcribir audio a texto
│   └── audio_processor.py  # Procesamiento de audio (si es necesario)
│
├── nlp/
│   ├── __init__.py
│   ├── recipe_extractor.py # Extracción de ingredientes y pasos de la receta
│   └── classifier.py       # Clasificación automática de recetas
│
├── notion/
│   ├── __init__.py
│   ├── notion_api.py       # Wrapper para interacciones con la API de Notion
│   └── page_generator.py   # Generación de páginas de Notion
│
├── utils/
│   ├── __init__.py
│   ├── error_handlers.py   # Manejo de errores personalizado
│   └── logging_config.py   # Configuración de logging
│
├── models/
│   ├── __init__.py
│   ├── recipe.py           # Modelo de datos para la receta
│   └── notion_page.py      # Modelo de datos para la página de Notion
│
├── services/
│   ├── __init__.py
│   └── workflow.py         # Orquestación del flujo de trabajo principal
│
├── tests/
│   ├── __init__.py
│   ├── test_instagram.py
│   ├── test_audio.py
│   ├── test_nlp.py
│   ├── test_notion.py
│   └── test_workflow.py
│
├── web/                    # (Opcional) Para la interfaz de usuario web
│   ├── __init__.py
│   ├── app.py              # Aplicación web (por ejemplo, usando Flask)
│   ├── templates/
│   └── static/
│
└── requirements.txt        # Dependencias del proyectoxº
​
Pruebas
Para ejecutar las pruebas unitarias:

python -m unittest discover tests
​
Contribuir
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de enviar un pull request.

Licencia
MIT License

Contacto
[Tu Nombre] - [tu@email.com]

Enlace del proyecto: https://github.com/tu-usuario/app-recetas-instagram-notion

