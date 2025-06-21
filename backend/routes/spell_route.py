from flask import Blueprint, request, jsonify
from services.spell_service import get_spells

spell_bp = Blueprint('spell_bp', __name__)

@spell_bp.route('/spells', methods=['GET'])
def get_spells_route():
    name = request.args.get('name')  # ex: /spells?name=lumos
    spells = get_spells(name_filter=name)
    return jsonify(spells)
