import { SpellType } from "../models/spell-type.model";

const spellTypeImagePaths: Record<string, string> = {
    "magie elementaire": "assets/img/types/elementaire.png",
    "entraves": "assets/img/types/entraves.png",
    "metamorphose et transmutation": "assets/img/types/metamorphose.png",
    "magie defensive": "assets/img/types/defensive.png",
    "sortileges": "assets/img/types/sortileges.png",
    "potions": "assets/img/types/potions.png",
    "condition physique": "assets/img/types/physique.png",
    "guerison": "assets/img/types/guerison.png",
    "creatures magiques": "assets/img/types/creatures.png",
    "plantes magiques": "assets/img/types/plantes.png",
    "arts occultes": "assets/img/types/occultes.png",
    "histoire du monde de la magie": "assets/img/types/histoire.png",
    "enchantements": "assets/img/types/enchantements.png",
};

export function getSpellTypeImagePath(spellType: string): string {
    const normalized = spellType.trim().toLowerCase();
    return spellTypeImagePaths[normalized] || "assets/img/types/default.png";
}

export function getSpellLabel(t: string): string {
	return SpellType[t] || t;
}

