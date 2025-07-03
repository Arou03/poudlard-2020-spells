# models/spell.py

from database.db import db
from models.spell_type_assoc import spell_spell_type 
from models.spell_spe_assoc import spell_spell_spe 

class Spell(db.Model):
    __tablename__ = 'spell'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(120), unique=True, nullable=False)
    niveau = db.Column(db.Integer, nullable=False)
    rapide = db.Column(db.Boolean, nullable=False)

    description = db.Column(db.Text, nullable=True)

    amp = db.Column(db.Integer, nullable=False)
    degat = db.Column(db.Integer, nullable=False)
    zone = db.Column(db.Integer, nullable=False)
    cmb = db.Column(db.Integer, nullable=False)

    types = db.relationship('SpellType', secondary=spell_spell_type, backref='spells', lazy='subquery')
    spes = db.relationship('SpellSpe', secondary=spell_spell_spe, backref='spell', lazy='subquery')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "niveau": self.niveau,
            "rapide": self.rapide,
            "description": self.description,
            "amp": self.amp,
            "degat": self.degat,
            "zone": self.zone,
            "cmb": self.cmb,
        }