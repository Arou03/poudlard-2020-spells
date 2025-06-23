export interface Spell {
    id: number;
    name: string;
    description: string;
    amp: number;
    degat: number;
    zone: string;
    cmb: string;
    niveau: number;
    type: string[];
    specialites: {
        name: string;
        description: string;
    }[];
    rapide: boolean;
}
