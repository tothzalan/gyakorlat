from fastapi import FastAPI
from pydantic import BaseModel
import json

from database import should_update, update, get_all, get_by_comp_name

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
    if should_update():
        update()
        return json.loads(get_all())
    return get_all()

@app.get('/companies/{company_name}', response_model=Company)
async def get_company(company_name: str):
    if should_update():
        update()
        return get_by_comp_name(company_name)
    print(get_by_comp_name(company_name))
    return get_by_comp_name(company_name)