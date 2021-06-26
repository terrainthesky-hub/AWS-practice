from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, ml, viz

description = """
FastAPI using uvicorn. 
See [https://fastapi.tiangolo.com/tutorial/metadata/](https://fastapi.tiangolo.com/tutorial/metadata/)

To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details

#<img src=>
"""

app = FastAPI(
    title='DS\' API',
    description=description,
    docs_url='/',
)

app.include_router(db.router, tags=["Lesley's database endpoints"])
app.include_router(ml.router, tags=['Machine Learning'])
app.include_router(viz.router, tags=['Visualization'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    uvicorn.run(app)