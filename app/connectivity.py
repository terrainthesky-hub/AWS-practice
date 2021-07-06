import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv('.env')


pw = os.getenv('PASSWORD')
un = os.getenv('USER_NAME')
url = os.getenv("URL")

USER_NAME="terra"
PASSWORD="AkuMa2tRon!"
URL="database-2.c0oecrjjdo0a.us-east-1.rds.amazonaws.com"

# Replace username, password, & blah.blah.blah
# database_url = f'postgresql://{un}:{pw}@{url}/postgres'
# database_url = 'postgresql://terra:AkuMa2tRon!@database-2.c0oecrjjdo0a.us-east-1.rds.amazonaws.com/postgres'
database_url = 'postgresql://terra:AkuMa2tRon!@terradb.c0oecrjjdo0a.us-east-1.rds.amazonaws.com/postgres'
engine = sqlalchemy.create_engine(database_url)
connection = engine.connect()