SELECT 
    spell.id,
    spell.name,
    spell.description,
    spell.amp,
    spell.zone,
    spell_type.name AS type_name
FROM spell
JOIN spell_type ON spell.id_type = spell_type.id
{% if name %}
WHERE spell.name LIKE :name COLLATE NOCASE
{% endif %}
ORDER BY spell.name;
