import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv('.env')


pw = os.getenv('PASSWORD')
un = os.getenv('USER_NAME')
url = os.getenv("URL")

# Replace username, password, & blah.blah.blah
# database_url = f'postgresql://{un}:{pw}@{url}/postgres'
# 

engine = sqlalchemy.create_engine(database_url)
connection = engine.connect()