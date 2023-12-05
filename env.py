import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_DIRECTORY = os.path.dirname(__file__)

DB_USERNAME = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('DB_PORT', '3306')
REQUIREMENTS_PATH = os.environ.get('REQUIREMENTS_PATH', f'{PROJECT_DIRECTORY}/requirements.csv')
