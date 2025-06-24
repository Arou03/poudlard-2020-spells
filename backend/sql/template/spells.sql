WITH types_by_spell AS (
    SELECT 
        sst.spell_id,
        JSON_ARRAYAGG(st.name) AS type
    FROM spell_spell_type sst
    JOIN spell_type st ON st.id = sst.spell_type_id
    GROUP BY sst.spell_id
),
specialites_by_spell AS (
    SELECT 
        sss.spell_id,
        JSON_ARRAYAGG(JSON_OBJECT('name', ss.name, 'description', ss.description)) AS specialites
    FROM spell_spell_spe sss
    JOIN spell_spe ss ON ss.id = sss.spell_spe_id
    GROUP BY sss.spell_id
),
filtered_spells AS (
    SELECT s.*
    FROM spell s
    WHERE 1=1
    {% if name %}
        AND s.name LIKE CONCAT('%', :name, '%') COLLATE utf8mb4_general_ci
    {% endif %}
    {% if niveau %}
        AND s.niveau IN ({{ niveau | join(',') }})
    {% endif %}
    {% if rapide is not none %}
        AND s.rapide = :rapide
    {% endif %}
    {% if type %}
        AND EXISTS (
            SELECT 1
            FROM spell_spell_type sst
            JOIN spell_type st ON st.id = sst.spell_type_id
            WHERE sst.spell_id = s.id AND st.name IN ({{ type | map('tojson') | join(',') }})
        )
    {% endif %}
)

SELECT 
    fs.*,
    COALESCE(t.type, JSON_ARRAY()) AS type,
    COALESCE(sp.specialites, JSON_ARRAY()) AS specialites
FROM filtered_spells fs
LEFT JOIN types_by_spell t ON fs.id = t.spell_id
LEFT JOIN specialites_by_spell sp ON fs.id = sp.spell_id
ORDER BY
    {% if sort_by == 'niveau' %}
        fs.niveau {{ (sort_order or 'asc') | upper }}
    {% else %}
        fs.name {{ (sort_order or 'asc') | upper }}
    {% endif %}
