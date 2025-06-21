# utils/sql_loader.py

from jinja2 import Environment, FileSystemLoader
import os

# Initialise le moteur Jinja2 dans le dossier "sql"
env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'sql', 'template')),
    trim_blocks=True,
    lstrip_blocks=True
)

def render_query(template_name, **params):
    template = env.get_template(f"{template_name}.sql")
    return template.render(**params)
