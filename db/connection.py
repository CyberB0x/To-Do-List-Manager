import mysql.connector
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

def get_db_connection():
    """Функция для получения подключения к базе данных."""
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
