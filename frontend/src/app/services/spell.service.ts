import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Spell } from '../models/spell.model';

@Injectable({
    providedIn: 'root'
})
export class SpellService {
    private apiUrl = 'http://127.0.0.1:5000/spells'; // à adapter

    constructor(private http: HttpClient) {}

    getSpells(): Observable<Spell[]> {
        return this.http.get<Spell[]>(this.apiUrl);
    }
}
