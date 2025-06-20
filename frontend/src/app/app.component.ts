import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SpellCardComponent } from "./components/spell-card/spell-card.component";

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  imports: [SpellCardComponent]
})
export class AppComponent {
  title = 'frontend';
}
