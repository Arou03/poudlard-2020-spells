import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-filtre-select',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: './filtre-select.component.html',
  styles: [`
    .filtre-select {
      display: block;
      padding: 4px;
      margin-bottom: 1rem;
    }
  `]
})
export class FiltreSelectComponent {
  @Input() label = '';
  @Input() options: { label: string; value: any }[] = [];
  @Input() multiple = false;
  @Input() selected: any = this.multiple ? [] : null;

  @Output() selectedChange = new EventEmitter<any>();

  onChange() {
    this.selectedChange.emit(this.selected);
  }
}
