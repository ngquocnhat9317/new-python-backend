import os

from dotenv import load_dotenv

load_dotenv()

PROD = os.getenv("PROD")
DATABASE = os.getenv("SCHEMA")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
USER = os.getenv("USER")
PASSWD = os.getenv("PASSWD")
RDS_CERT_PATH = "/opt/root-certs.crt"
DEBUG = PROD is None
