# models/spell_type.py

from database.db import db

class SpellSpe(db.Model):
    __tablename__ = 'spell_spe'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
