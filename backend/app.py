from flask import Flask
from config import Config
from database.db import db
from routes.spell_route import spell_bp

from models.spell import Spell
from models.spell_type import SpellType
from models.spell_spe import SpellSpe

from database.populate import populate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(spell_bp)

with app.app_context():
    db.create_all()  # <-- crée spellwiki.db avec les tables définies

populate(app)

if __name__ == '__main__':
    app.run(debug=True)

