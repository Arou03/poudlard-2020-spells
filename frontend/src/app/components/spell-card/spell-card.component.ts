import { Component, Input } from '@angular/core';
import { Spell } from '../../models/spell.model';

@Component({
  selector: 'app-spell-card',
  standalone: true,
  imports: [],
  templateUrl: './spell-card.component.html',
  styleUrl: './spell-card.component.css'
})
export class SpellCardComponent {
  @Input() spell!: Spell;
}
