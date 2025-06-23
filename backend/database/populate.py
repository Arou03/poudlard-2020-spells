import os
from sqlalchemy import text
from database.db import db
from models.spell_type import SpellType

def reset_table():
    db.session.execute(text("DELETE FROM spell_spell_type;"))
    db.session.execute(text("DELETE FROM spell_spell_spe;"))
    db.session.execute(text("DELETE FROM spell;"))
    db.session.execute(text("DELETE FROM spell_type;"))
    db.session.execute(text("DELETE FROM spell_spe;"))

    db.session.execute(text("ALTER TABLE spell_type AUTO_INCREMENT = 1"))
    db.session.commit()


def populate(app):
    with app.app_context():
        db.create_all()
        print("✅ Tables créées")

        reset_table()

        sql_path = os.path.join(os.path.dirname(__file__), '..', 'sql', 'init_db', 'data.sql')
        with open(sql_path, "r", encoding='utf-8') as f:
            sql_content = f.read()

        # Sépare les statements en se basant sur les points-virgules
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]

        for stmt in statements:
            db.session.execute(text(stmt))
        
        db.session.commit()
        print("✅ Données insérées (si non déjà présentes)")


