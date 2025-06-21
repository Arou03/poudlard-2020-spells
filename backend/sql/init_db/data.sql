-- Nettoyage (avec protection)

-- Supprimer les sorts si la table existe
DELETE FROM spell
WHERE EXISTS (SELECT name FROM sqlite_master WHERE type='table' AND name='spell');

-- Supprimer les types si la table existe
DELETE FROM spell_type
WHERE EXISTS (SELECT name FROM sqlite_master WHERE type='table' AND name='spell_type');

-- Remplissage table spell_type
INSERT INTO spell_type (name) VALUES
    ('Magie Élémentaire'),
    ('Entraves'),
    ('Métamorphose et Transmutation'),
    ('Magie Défensive'),
    ('Sortilèges'),
    ('Potions'),
    ('Condition Physique'),
    ('Guérison'),
    ('Créatures Magiques'),
    ('Plantes Magiques'),
    ('Arts Occultes'),
    ('Histoire du Monde de la Magie'),
    ('Enchantements');


-- Remplissage table spell
INSERT INTO spell (id, name, description, amp, zone, id_type) VALUES 
    (1, 'Incendio', 'Crée une flamme', 3, 1, 1),
    (2, 'Aguamenti', 'Fait jaillir de l''eau', 2, 1, 2),
    (3, 'Ventus', 'Provoque une rafale de vent', 1, 2, 3),
    (4, 'Terralux', 'Illumine la terre', 4, 1, 4);
