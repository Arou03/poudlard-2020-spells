SELECT 
    spell.*,
    JSON_ARRAYAGG(spell_type.name) AS type,
    JSON_ARRAYAGG(JSON_OBJECT('name', spell_spe.name, 'description', spell_spe.description)) AS specialites
FROM spell
JOIN spell_spell_type ON spell.id = spell_spell_type.spell_id
JOIN spell_type ON spell_type.id = spell_spell_type.spell_type_id
JOIN spell_spell_spe ON spell.id = spell_spell_spe.spell_id
JOIN spell_spe ON spell_spe.id = spell_spell_spe.spell_spe_id
{% if name %}
WHERE spell.name LIKE :name COLLATE NOCASE
{% endif %}
GROUP BY spell.id, spell.name, spell.description, spell.amp, spell.zone
ORDER BY spell.name;
