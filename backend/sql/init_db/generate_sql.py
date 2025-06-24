import re
from pathlib import Path
import unicodedata

# === Chemins ===
# J'utilise le nom de fichier que vous avez fourni.
raw_path = Path("raw_spells.txt") 
output_path = Path("generated_spells_clean.sql")

# === Mapping emojis → types ===
# (Inchangé)
emoji_to_type = {
    "🔥": "magie elementaire",
    "⛓️": "entraves",
    "🌔": "metamorphose et transmutation",
    "🛡️": "magie defensive",
    "🪄": "sortileges",
    ":wizard_potion3:": "potions",
    "💪": "condition physique",
    "💗": "guerison",
    "🐉": "creatures magiques",
    "🍄": "plantes magiques",
    ":Pentagram:": "arts occultes",
    "📖": "histoire du monde de la magie",
    "⭐": "enchantements"
}

emoji_rapide = "🟡"
emoji_lent = "🟢"

# === Fonction de nettoyage SQL-safe (Améliorée) ===
def sanitize_for_sql(text):
    """
    Nettoie une chaîne pour une insertion SQL sécurisée :
    - échappe les apostrophes
    - remplace les sauts de ligne
    - remplace les points-virgules qui pourraient rompre les requêtes
    """
    text = text.replace("'", "''")       # Échappe les apostrophes
    text = text.replace(";", ",")        # Remplace les ; dangereux
    text = text.replace("\n", " ")       # Supprime les retours ligne
    return text.strip()

# === Lecture du texte brut ===
raw_text = raw_path.read_text(encoding="utf-8")
raw_text = unicodedata.normalize("NFKC", raw_text)

# === NOUVELLE LOGIQUE : Découpage par les séparateurs ===
# Ce motif identifie une ligne de séparation complète (ex: • ===...•)
# et les lignes "MJ" qui peuvent la suivre.
# ^\s*• : commence par une puce, potentiellement précédée d'espaces.
# [=–\-•\s]{10,} : suivi par au moins 10 caractères de séparation.
# .*$ : jusqu'à la fin de la ligne.
splitter_pattern = re.compile(r"^\s*•\s*[=–\-•\s]{10,}.*?•\s*$(?:\nMJ —.*)?", re.MULTILINE)

# On découpe le fichier entier en utilisant le séparateur.
# Les séparateurs sont supprimés, et on obtient une liste de blocs de sorts propres.
spell_blocks = splitter_pattern.split(raw_text)

# === Génération SQL ===
sql_statements = []
spe_name_to_id = {}
current_spe_id = 1
current_spell_id = 1

# Le motif pour trouver l'en-tête d'un sort
header_pattern = re.compile(r"^(?P<name>.+?)\s(?P<speed>[🟢🟡])\s\|\s(?P<types>.+?)\s\|\s(?P<level>\d+)️⃣", re.MULTILINE)

for block in spell_blocks:
    block = block.strip()
    if not block:
        continue # Ignorer les blocs vides résultant du split

    lines = block.splitlines()
    header = lines[0]
    
    name_match = header_pattern.match(header)
    if not name_match:
        print(f"[⚠] En-tête non reconnu pour le bloc :\n---\n{block[:100]}...\n---")
        continue

    # --- Extraction des données de l'en-tête ---
    name = sanitize_for_sql(name_match.group("name"))
    rapide = "true" if name_match.group("speed") == emoji_rapide else "false"
    niveau = int(name_match.group("level"))
    
    types_str = unicodedata.normalize("NFKC", name_match.group("types"))
    types_emojis = [emoji for emoji in emoji_to_type if emoji in types_str]
    types_sql = set(emoji_to_type[e] for e in types_emojis if e in emoji_to_type)
    
    if not types_sql:
        print(f"[⚠] Aucun type détecté pour le sort '{name}' avec types_str = '{types_str}'")

    # --- Extraction des attributs (Amp, Dgts, etc.) ---
    amp = degat = zone = cmb = 0
    # On commence la recherche après l'en-tête (ligne 1)
    body_lines = lines[1:]
    
    for line in body_lines:
        line = line.strip()
        if line.lower().startswith("amp:"):
            amp = int(line.split(":")[1].strip())
        elif line.lower().startswith("dgts:"):
            val = line.split(":")[1].strip()
            degat = "NULL" if "♾️" in val or not val else int(val)
        elif line.lower().startswith("zone:"):
            zone = int(line.split(":")[1].strip())
        elif line.lower().startswith("cmb:"):
            cmb = int(line.split(":")[1].strip())
            
    # --- Extraction des Spécialités ---
    spe_lines_raw = []
    in_spe_section = False
    # On ne garde que les lignes qui suivent la ligne "Spé:"
    for i, line in enumerate(body_lines):
        if line.lower().strip() == "spé:":
            in_spe_section = True
            # Les spécialités commencent à la ligne suivante
            spe_lines_raw = body_lines[i+1:]
            break
    
    spes = []
    # On arrête de lire les spécialités à la première ligne vide
    # ou à une ligne qui ne contient pas le séparateur "- -"
    description_lines_start_index = 0
    for i, line in enumerate(spe_lines_raw):
        if "- -" in line:
            spe_name, spe_desc = map(str.strip, line.split("- -", 1))
            spe_name_clean = sanitize_for_sql(spe_name)
            spe_desc_clean = sanitize_for_sql(spe_desc)
            
            if spe_name_clean not in spe_name_to_id:
                spe_name_to_id[spe_name_clean] = current_spe_id
                sql_statements.append(
                    f"INSERT INTO spell_spe (id, name, description) VALUES ({current_spe_id}, '{spe_name_clean}', '{spe_desc_clean}') "
                    f"ON CONFLICT (id) DO NOTHING;"
                )
                current_spe_id += 1
            spes.append((spe_name_to_id[spe_name_clean], spe_name_clean))
        else:
            # On a fini les spécialités, le reste est la description
            description_lines_start_index = i
            break

    # --- Extraction de la description libre ---
    # La description est tout ce qui reste après les spécialités.
    description_raw = "\n".join(spe_lines_raw[description_lines_start_index:]).strip()
    description = sanitize_for_sql(description_raw)

    # --- Génération des instructions SQL ---
    sql_statements.append(
        "INSERT INTO spell (id, name, niveau, rapide, description, amp, degat, zone, cmb) "
        f"VALUES ({current_spell_id}, '{name}', {niveau}, {rapide}, '{description}', {amp}, {degat}, {zone}, {cmb});"
    )

    for type_name in types_sql:
        sql_statements.append(
            "INSERT INTO spell_spell_type (spell_id, spell_type_id) "
            f"SELECT {current_spell_id}, id FROM spell_type WHERE LOWER(name) = '{sanitize_for_sql(type_name)}';"
        )

    for spe_id, _ in spes:
        sql_statements.append(
            f"INSERT INTO spell_spell_spe (spell_id, spell_spe_id) VALUES ({current_spell_id}, {spe_id});"
        )

    current_spell_id += 1

# === Sauvegarde fichier SQL ===
output_path.write_text("\n".join(sql_statements), encoding="utf-8")
print(f"[✔] SQL généré : {output_path.resolve()}")