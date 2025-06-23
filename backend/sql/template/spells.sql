SELECT 
    s.*,
    (
        SELECT JSON_ARRAYAGG(unique_types.name)
        FROM (
            SELECT DISTINCT st.name
            FROM spell_spell_type sst
            JOIN spell_type st ON st.id = sst.spell_type_id
            WHERE sst.spell_id = s.id
        ) AS unique_types
    ) AS type,
    (
        SELECT JSON_ARRAYAGG(JSON_OBJECT('name', unique_specialites.name, 'description', unique_specialites.description))
        FROM (
            SELECT DISTINCT ss.name, ss.description
            FROM spell_spell_spe sss
            JOIN spell_spe ss ON ss.id = sss.spell_spe_id
            WHERE sss.spell_id = s.id
        ) AS unique_specialites
    ) AS specialites
FROM spell s
{% if name %}
WHERE s.name LIKE :name COLLATE NOCASE
{% endif %}
ORDER BY s.name;
