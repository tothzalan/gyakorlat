import sqlite3
import json
from indexer import get_data

con = sqlite3.connect('gyakorlat.db')
cur = con.cursor()

def create_tables():
    cur.execute('CREATE TABLE IF NOT EXISTS company(name, url, technologies)')
    cur.execute('CREATE TABLE IF NOT EXISTS updated(last_date)')
    cur.execute('INSERT INTO updated VALUES (DATE())')
    con.commit()

def should_update() -> bool:
    res = cur.execute('SELECT DATE(), last_date FROM updated')
    current, last_updated = res.fetchone()
    cur.execute('UPDATE updated SET last_date = DATE()')
    return current != last_updated

def update():
    cur.execute('DELETE FROM company')
    companies = json.loads(get_data(3))
    for c in companies:
        c['technologies'] = array_to_csv(c['technologies'])
    cur.executemany('INSERT INTO company VALUES (?, ?, ?)', [list(c.values()) for c in companies])
    con.commit()

def array_to_csv(input: list) -> str:
    ret = ''
    for v in input:
        ret += f'{v},'
    return ret[:-1]

def csv_to_array(str) -> list:
    return str.split(',')

def get_all():
    res = cur.execute('SELECT * FROM company')
    raw_arrays = res.fetchall()

    return [{ 'name': c[0], 'url': c[1], 'technologies': csv_to_array(c[2]) } for c in raw_arrays]

create_tables()
#update()
