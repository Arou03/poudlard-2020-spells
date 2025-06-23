from database.db import db
from sqlalchemy import text
from utils.sql_loader import render_query
import json

def get_spells(name_filter=None):
    try:
        sql_str = render_query("spells", name=bool(name_filter))
        print("SQL rendu :", sql_str)

        sql = text(sql_str)

        params = {}
        if name_filter:
            print(f"J'ai reçu un parametre : {name_filter}")
            params["name"] = f"%{name_filter}%"

        results = db.session.execute(sql, params).mappings().all()
        rows = [dict(row) for row in results]

        for row in rows:
            if "type" in row and isinstance(row["type"], str):
                row["type"] = json.loads(row["type"])
            if "specialites" in row and isinstance(row["specialites"], str):
                row["specialites"] = json.loads(row["specialites"])

        return rows

    except Exception as e:
        print("❌ Erreur SQL :", e)
        return []