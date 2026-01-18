import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.getenv("DATABASE_URL")

def get_test_data():
    """Возвращает 3 числа: 1, 2, 3"""
    return [1, 2, 3]

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)