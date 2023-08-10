from fastapi import FastAPI
from pydantic import BaseModel
import json

from indexer import get_data

app = FastAPI()

class Company(BaseModel):
    name: str
    url: str
    technologies: list[str]

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'name': 'Menoceg xd',
                    'url': 'https://www.inf.elte.hu/szakmaigyalorlat/menocegxdkft',
                    'technologies': [
                        'haskell', 'python'
                    ]
                }
            ]
        }
    }

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/companies', response_model=list[Company])
async def get_all_companies():
    return json.loads(get_data(5))