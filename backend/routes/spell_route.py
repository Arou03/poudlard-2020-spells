from flask import Blueprint, request, jsonify
from services.spell_service import get_spells

spell_bp = Blueprint('spell_bp', __name__)

@spell_bp.route('/spells', methods=['GET'])
def get_spells_route():
    try:
        name = request.args.get('name')
        niveaux = request.args.getlist('niveau')  # ?niveau=2&niveau=5
        types = request.args.getlist('type')      # ?type=Feu&type=Glace
        rapide = request.args.get('rapide')
        sort_by = request.args.get('sort_by')     # ?sort_by=name|niveau
        sort_order = request.args.get('sort_order')  # ?sort_order=asc|desc

        print("🔍 Requête reçue avec paramètres :")
        print("  - name:", name)
        print("  - niveaux:", niveaux)
        print("  - types:", types)
        print("  - rapide:", rapide)
        print("  - sort_by:", sort_by)
        print("  - sort_order:", sort_order)

        # Conversion rapide string → bool
        if rapide is not None:
            rapide = rapide.lower() == "true"

        spells = get_spells(
            name_filter=name,
            niveaux=niveaux,
            types=types,
            rapide=rapide,
            sort_by=sort_by,
            sort_order=sort_order
        )

        return jsonify(spells)

    except Exception as e:
        print("❌ Erreur dans /spells :", e)
        return jsonify({'error': str(e)}), 500
