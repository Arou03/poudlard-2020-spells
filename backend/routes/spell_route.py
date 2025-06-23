from flask import Blueprint, request, jsonify
from services.spell_service import get_spells

spell_bp = Blueprint('spell_bp', __name__)

@spell_bp.route('/spells', methods=['GET'])
def get_spells_route():
    try:
        name = request.args.get('name')
        print("Requête reçue ! Nom =", name)
        spells = get_spells(name_filter=name)
        return jsonify(spells)
    except Exception as e:
        print("Erreur dans /spells :", e)
        return jsonify({'error': str(e)}), 500
