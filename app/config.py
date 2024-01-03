import os

from dotenv import load_dotenv

load_dotenv()

PROD = os.getenv("PROD")
DATABASE = os.getenv("SCHEMA", "database_name")
HOST = os.getenv("DB_HOST", "127.0.0.1")
PORT = os.getenv("DB_PORT", "5432")
USER = os.getenv("USER", "root")
PASSWD = os.getenv("PASSWD", "1")
DEBUG = PROD is None

ALLOW_TOKEN = ["hMRSNSNiw3tAh33cLwCGhXeZDs4zNyeMnGwhoFjH6vavT"]
