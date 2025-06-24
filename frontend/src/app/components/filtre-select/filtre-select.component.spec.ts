import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FiltreSelectComponent } from './filtre-select.component';

describe('FiltreSelectComponent', () => {
  let component: FiltreSelectComponent;
  let fixture: ComponentFixture<FiltreSelectComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FiltreSelectComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FiltreSelectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
