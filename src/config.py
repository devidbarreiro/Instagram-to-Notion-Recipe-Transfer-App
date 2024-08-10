# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Instagram API configuration
INSTAGRAM_API_KEY = os.getenv('INSTAGRAM_API_KEY')

# Notion API configuration
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

# OpenAI API configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Other configuration
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Validate required environment variables
required_vars = ['INSTAGRAM_API_KEY', 'NOTION_API_KEY', 'NOTION_DATABASE_ID', 'OPENAI_API_KEY']
missing_vars = [var for var in required_vars if not globals().get(var)]

if missing_vars:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")