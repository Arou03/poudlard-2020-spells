from database.db import db
from sqlalchemy import text
from utils.sql_loader import render_query
import json

def get_spells(name_filter=None, niveaux=None, types=None, rapide=None, sort_by=None, sort_order=None):
    try:
        # Nettoyage des paramètres de tri
        if sort_by not in ['name', 'niveau']:
            sort_by = None  # Par défaut dans le template, ce sera name
        if sort_order:
            sort_order = sort_order.lower()
            if sort_order not in ['asc', 'desc']:
                sort_order = 'asc'
        else:
            sort_order = 'asc'

        # Préparer le booléen de présence de chaque filtre pour le template
        sql_str = render_query(
            "spells",
            name=bool(name_filter),
            niveau=niveaux if niveaux else None,
            type=types if types else None,
            rapide=rapide if rapide is not None else None,
            sort_by=sort_by,
            sort_order=sort_order
        )
        print("📜 SQL rendu :", sql_str)

        sql = text(sql_str)

        # Construction des paramètres SQL
        params = {}

        if name_filter:
            print(f"🔍 Filtre nom : {name_filter}")
            params["name"] = name_filter  # Le LIKE est déjà géré dans le template

        if niveaux:
            print(f"🎚️ Niveaux filtrés : {niveaux}")
            params["niveau"] = [int(n) for n in niveaux if str(n).isdigit()]

        if types:
            print(f"🔥 Types filtrés : {types}")
            params["type"] = types

        if rapide is not None:
            print(f"⚡ Vitesse : {'rapide' if rapide else 'lent'}")
            params["rapide"] = bool(rapide)

        # Exécution
        results = db.session.execute(sql, params).mappings().all()
        rows = [dict(row) for row in results]

        # Parsing JSON
        for row in rows:
            if "type" in row and isinstance(row["type"], str):
                row["type"] = json.loads(row["type"])
            if "specialites" in row and isinstance(row["specialites"], str):
                row["specialites"] = json.loads(row["specialites"])

        return rows

    except Exception as e:
        print("❌ Erreur SQL :", e)
        return []
