import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SpellCardComponent } from "./components/spell-card/spell-card.component";
import { SpellListComponent } from "./components/spell-list/spell-list.component";

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  imports: [SpellListComponent]
})
export class AppComponent {
  title = 'frontend';
}
