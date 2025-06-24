import { Component, EventEmitter, Output, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { debounceTime, distinctUntilChanged, Subject } from 'rxjs';
import { SpellType } from '../../models/spell-type.model';

@Component({
	selector: 'app-search-bar',
	standalone: true,
	imports: [CommonModule, FormsModule],
	templateUrl: './search-bar.component.html',
})
export class SearchBarComponent {
	name: string = '';
	niveaux: (number | string)[] = [];
	types: string[] = [];
	rapide: boolean | undefined;
	sortSelection = 'name_asc';

	showNiveauDropdown = false;
	showTypeDropdown = false;
	showRapideDropdown = false;
	showSortDropdown = false;

	niveauOptions = [1, 2, 3, 4, 5, 6, 7];
	typeOptions = Object.entries(SpellType).map(([key, label]) => ({
		value: key,
		label,
	}));

	sortOptions = [
		{ value: 'name_asc', label: 'Nom croissant' },
		{ value: 'name_desc', label: 'Nom décroissant' },
		{ value: 'niveau_asc', label: 'Niveau croissant' },
		{ value: 'niveau_desc', label: 'Niveau décroissant' },
	];

	private nameSubject = new Subject<string>();

	@Output() search = new EventEmitter<{
		name?: string;
		niveau?: (string | number)[];
		type?: string[];
		rapide?: boolean;
		sort_by?: string;
		sort_order?: string;
	}>();

	constructor() {
		this.nameSubject
			.pipe(debounceTime(300), distinctUntilChanged())
			.subscribe((value) => {
				this.name = value;
				this.emitSearch();
			});
	}

	onNameChange(event: Event): void {
		const target = event.target as HTMLInputElement;
		this.nameSubject.next(target.value);
	}

	onNiveauToggle(niveau: number): void {
		const index = this.niveaux.indexOf(niveau);
		if (index > -1) this.niveaux.splice(index, 1);
		else this.niveaux.push(niveau);
		this.emitSearch();
	}

	onToggleTousNiveaux(): void {
		this.niveaux = [];
		this.emitSearch();
	}

	isTousNiveauxChecked(): boolean {
		return this.niveaux.length === 0;
	}

	onTypeToggle(type: string): void {
		const index = this.types.indexOf(type);
		if (index > -1) this.types.splice(index, 1);
		else this.types.push(type);
		this.emitSearch();
	}

	onToggleTousTypes(): void {
		this.types = [];
		this.emitSearch();
	}

	isTousTypesChecked(): boolean {
		return this.types.length === 0;
	}

	onRapideChange(val: boolean | undefined): void {
		this.rapide = val;
		this.emitSearch();
	}

	onToggleTousRapide(): void {
		this.rapide = undefined;
		this.emitSearch();
	}

	isTousRapideChecked(): boolean {
		return this.rapide === undefined;
	}

	getNiveauDisplay(): string {
		return this.niveaux.length ? this.niveaux.join(', ') : 'Tous';
	}

	getTypeDisplay(): string {
		return this.types.length
			? this.types.map((t) => this.getTypeLabel(t)).join(', ')
			: 'Tous';
	}

	getTypeLabel(value: string): string {
		const found = this.typeOptions.find((t) => t.value === value);
		return found ? found.label : value;
	}

	getSortDisplay(): string {
		const found = this.sortOptions.find((s) => s.value === this.sortSelection);
		return found ? found.label : '';
	}

	onSortChanged(): void {
		const [field, order] = this.sortSelection.split('_');
		this.search.emit({
			name: this.name,
			niveau: this.niveaux,
			type: this.types,
			rapide: this.rapide,
			sort_by: field,
			sort_order: order,
		});
	}

	onFiltersChanged(): void {
		this.emitSearch();
	}

	private emitSearch(): void {
		const [field, order] = this.sortSelection.split('_');
		this.search.emit({
			name: this.name,
			niveau: this.niveaux,
			type: this.types,
			rapide: this.rapide,
			sort_by: field,
			sort_order: order,
		});
	}

	@HostListener('document:click', ['$event'])
	onClickOutside(event: MouseEvent): void {
		const target = event.target as HTMLElement;
		if (!target.closest('.niveau-dropdown')) this.showNiveauDropdown = false;
		if (!target.closest('.type-dropdown')) this.showTypeDropdown = false;
		if (!target.closest('.rapide-dropdown')) this.showRapideDropdown = false;
		if (!target.closest('.sort-dropdown')) this.showSortDropdown = false;
	}
}
