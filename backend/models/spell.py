# models/spell.py

from database.db import db
from models.spell_type_assoc import spell_spell_type 

class Spell(db.Model):
    __tablename__ = 'spell'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    amp = db.Column(db.Integer, nullable=False)
    zone = db.Column(db.Integer, nullable=False)

    types = db.relationship('SpellType', secondary=spell_spell_type, backref='spells', lazy='subquery')


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "amp": self.amp,
            "zone":self.zone,
            "id_type": self.id_type
        }
