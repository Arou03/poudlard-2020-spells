# models/spell_spe_assoc.py

from database.db import db

spell_spell_spe = db.Table(
    'spell_spell_spe',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('spell_id', db.Integer, db.ForeignKey('spell.id'), primary_key=True),
    db.Column('spell_spe_id', db.Integer, db.ForeignKey('spell_spe.id'), primary_key=True)
)
