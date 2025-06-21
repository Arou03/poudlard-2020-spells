from database.db import db
from sqlalchemy import text
from utils.sql_loader import render_query

def get_spells(name_filter=None):
    sql_str = render_query("spells", name=bool(name_filter))
    sql = text(sql_str)

    params = {}
    if name_filter:
        print(f"J'ai reçu un parametre : {name_filter}")
        params["name"] = f"%{name_filter}%"

    results = db.session.execute(sql, params).mappings().all()
    return [dict(row) for row in results]

