import os

from dotenv import load_dotenv

load_dotenv()

PROD = os.getenv("PROD")
DEBUG = PROD is None
