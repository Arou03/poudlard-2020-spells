import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Spell } from '../../models/spell.model';
import {
  getSpellTypeImagePath,
  getSpellLabel,
} from '../../utils/spell-type.utils';

@Component({
  selector: 'app-spell-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './spell-card.component.html',
  styleUrl: './spell-card.component.css',
})
export class SpellCardComponent {
  @Input() spell!: Spell;

  getSpellLabel = getSpellLabel;
  getSpellImage = getSpellTypeImagePath;

  getGradientClasses(type1: string, type2?: string): string[] {
    const colorMap: Record<string, string> = {
      'magie elementaire': '#5b1d1d',
      entraves: '#444c5c',
      'metamorphose et transmutation': '#3d3a5a',
      'magie defensive': '#223344',
      sortileges: '#4b3b5c',
      potions: '#3a5230',
      'condition physique': '#5c4020',
      guerison: '#3e664d',
      'creatures magiques': '#4c3f2f',
      'plantes magiques': '#3d5c3f',
      'arts occultes': '#1d3928',
      'histoire du monde de la magie': '#3b3b3b',
      enchantements: '#3b2e4a',
    };

    const color1 = colorMap[type1] ?? '#333333';
    const color2 = type2 ? colorMap[type2] ?? '#222222' : 'transparent';

    const fromClass = `from-[${color1}]`;
    const toClass = `to-[${color2}]`;

    return [fromClass, toClass];
  }
}
