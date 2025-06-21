# models/spell_type_assoc.py

from database.db import db

spell_spell_type = db.Table(
    'spell_spell_type',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('spell_id', db.Integer, db.ForeignKey('spell.id'), primary_key=True),
    db.Column('spell_type_id', db.Integer, db.ForeignKey('spell_type.id'), primary_key=True)
)
