import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Spell } from '../../models/spell.model';
import { getSpellTypeImagePath, getSpellLabel } from '../../utils/spell-type.utils';

@Component({
  selector: 'app-spell-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './spell-card.component.html',
  styleUrl: './spell-card.component.css'
})
export class SpellCardComponent {
  @Input() spell!: Spell;

	getSpellLabel = getSpellLabel;
	getSpellImage = getSpellTypeImagePath;
}
