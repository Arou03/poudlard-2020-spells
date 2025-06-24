import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SpellService } from '../../services/spell.service';
import { Spell } from '../../models/spell.model';
import { SpellCardComponent } from '../spell-card/spell-card.component';
import { SearchBarComponent } from '../search-bar/search-bar.component';

@Component({
	selector: 'app-spell-list',
	standalone: true,
	imports: [CommonModule, SpellCardComponent, SearchBarComponent],
	templateUrl: './spell-list.component.html',
	styleUrls: ['./spell-list.component.css']
})
export class SpellListComponent implements OnInit {
	spells: Spell[] = [];

	constructor(private spellService: SpellService) {}

	ngOnInit(): void {
		this.loadSpells(); // chargement initial sans filtres
	}

	loadSpells(filters?: {
		name?: string;
		niveau?: (number | string)[];
		type?: string[];
		rapide?: boolean;
		sort_by?: string;
		sort_order?: string;
	}): void {
		this.spellService.getSpells(filters).subscribe(data => {
			this.spells = data;
		});
	}

	onSearch(filters: {
		name?: string;
		niveau?: (number | string)[];
		type?: string[];
		rapide?: boolean;
		sort_by?: string;
		sort_order?: string;
	}): void {
		this.loadSpells(filters);
	}
}
