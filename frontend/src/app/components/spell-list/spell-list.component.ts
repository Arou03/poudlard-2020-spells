import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SpellService } from '../../services/spell.service';
import { Spell } from '../../models/spell.model';
import { SpellCardComponent } from '../spell-card/spell-card.component';

@Component({
    selector: 'app-spell-list',
    standalone: true,
    imports: [SpellCardComponent, CommonModule],
    templateUrl: './spell-list.component.html',
    styleUrls: ['./spell-list.component.css']
})
export class SpellListComponent implements OnInit {
    spells: Spell[] = [];

    constructor(private spellService: SpellService) {}

    ngOnInit(): void {
        this.spellService.getSpells().subscribe(data => {
            this.spells = data;
        });
    }
}
