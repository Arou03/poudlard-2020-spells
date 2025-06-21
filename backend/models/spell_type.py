# models/spell_type.py

from database.db import db

class SpellType(db.Model):
    __tablename__ = 'spell_type'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    spells = db.relationship('Spell', backref='type', lazy=True)
