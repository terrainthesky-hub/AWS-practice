"""Database functions"""

import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
import pandas as pd
import pandas.util.testing

router = APIRouter()

def engine_connect():
    load_dotenv('.env')


    pw = os.getenv('PASSWORD')
    un = os.getenv('USER_NAME')
    url = os.getenv("URL")


    # Replace username, password, & blah.blah.blah
    database_url = f'postgresql://{un}:{pw}@{url}/postgres'
    engine = sqlalchemy.create_engine(database_url)
    global connection
    connection = engine.connect()



async def get_db() -> sqlalchemy.engine.base.Connection:
    """Get a SQLAlchemy database connection.
    
    Uses this environment variable if it exists:  
    DATABASE_URL=dialect://user:password@host/dbname

    Otherwise uses a SQLite database for initial local development.
    """
    # Replace username, password, & blah.blah.blah
    load_dotenv('.env')

    pw = os.getenv('PASSWORD')
    un = os.getenv('USER_NAME')
    url = os.getenv("URL")
    database_url = f'postgresql://{un}:{pw}@{url}/postgres'
    engine = sqlalchemy.create_engine(database_url)
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()

# def get_url():
#     """Verify we can connect to the database, 
#     and return the database URL in this format:

#     dialect://user:password@host/dbname
    
#     The password will be hidden with ***
#     """
#     engine_connect()
#     url_without_password = repr(connection.engine.url)
#     return {'database_url': url_without_password}


@router.get('/info')
async def get_url():
    """Verify we can connect to the database, 
    and return the database URL in this format:

    dialect://user:password@host/dbname

    The password will be hidden with ***


    """
    engine_connect()
    
    url_without_password = repr(connection.engine.url)
    connection.close()
    return {'database_url': url_without_password}


@router.post('/write')
def write_data():    
    engine_connect()
    tablename = 'mytable'
    df = pd.util.testing.makeDataFrame()
    df.to_sql(tablename, connection, if_exists='append', index=False, method='multi')
    connection.close()
    return {"message" : "Data added to Database"}


@router.get('/read')
def read_data():
    engine_connect()
    query = """SELECT * FROM mytable LIMIT 5;"""
    df = pd.read_sql(query, connection)
    connection.close()
    return df.to_dict(orient='records')