from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def create_db_uri():
    db_uri = getenv('DB_URI')
    return db_uri
