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


INSERT INTO spell_spe (name, description) VALUES
('Accablant', 'Cmb+1.'),
('Alourdissant', 'Le prochain sort de la cible subit un malus d Amp-3.'),
('Épars', 'Zone+1'),
('Excessif', 'Gagne la propriété :Pentagram: et +1 Dgts, la cible se mettant à abondamment saigner du nez.');

-- Locomotor Wibbly
INSERT INTO spell (name, niveau, vitesse, description, amp, degat, zone, cmb)
VALUES (
    'Locomotor Wibbly',
    3,
    FALSE,
    'Rend les jambes de la cible particulièrement molles et inefficaces. La cible ne peut plus utiliser d\'action rapide pour 1d3 tour - représentant la durée d\'activité du sort.',
    9,
    0,
    1,
    0
);

-- Mucus Ad Nauseam
INSERT INTO spell (name, niveau, vitesse, description, amp, degat, zone, cmb)
VALUES (
    'Mucus Ad Nauseam',
    1,
    FALSE,
    'Enrhume au sens premier la cible, dont le nez se met à couler abondamment. Les effets durent le temps d\'un rhume classique, à moins qu\'ils ne soient dissipés par magie.',
    9,
    0,
    1,
    1
);

-- Locomotor Wibbly
INSERT INTO spell_spell_spe (spell_id, spell_spe_id)
VALUES
((SELECT id FROM spell WHERE name = 'Locomotor Wibbly'), (SELECT id FROM spell_spe WHERE name = 'Accablant')),
((SELECT id FROM spell WHERE name = 'Locomotor Wibbly'), (SELECT id FROM spell_spe WHERE name = 'Alourdissant'));

-- Mucus Ad Nauseam
INSERT INTO spell_spell_spe (spell_id, spell_spe_id)
VALUES
((SELECT id FROM spell WHERE name = 'Mucus Ad Nauseam'), (SELECT id FROM spell_spe WHERE name = 'Épars')),
((SELECT id FROM spell WHERE name = 'Mucus Ad Nauseam'), (SELECT id FROM spell_spe WHERE name = 'Excessif'));

-- Locomotor Wibbly: 🛡️ ⛓️
INSERT INTO spell_spell_type (spell_id, spell_type_id)
VALUES
((SELECT id FROM spell WHERE name = 'Locomotor Wibbly'), (SELECT id FROM spell_type WHERE name = 'Magie Défensive')),
((SELECT id FROM spell WHERE name = 'Locomotor Wibbly'), (SELECT id FROM spell_type WHERE name = 'Entraves'));

-- Mucus Ad Nauseam: 🛡️ 🌖 (+ :Pentagram: via Excessif)
INSERT INTO spell_spell_type (spell_id, spell_type_id)
VALUES
((SELECT id FROM spell WHERE name = 'Mucus Ad Nauseam'), (SELECT id FROM spell_type WHERE name = 'Magie Défensive')),
((SELECT id FROM spell WHERE name = 'Mucus Ad Nauseam'), (SELECT id FROM spell_type WHERE name = 'Arts Occultes'));
