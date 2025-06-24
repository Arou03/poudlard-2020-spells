import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Spell } from '../models/spell.model';
import { environment } from '../../environments/environment';


@Injectable({
	providedIn: 'root',
})
export class SpellService {
	private apiUrl = `${environment.apiBaseUrl}/spells`;

	constructor(private http: HttpClient) {}

	getSpells(params?: {
		name?: string;
		niveau?: (number | string)[];
		type?: string[];
		rapide?: boolean;
		sort_by?: string;
		sort_order?: string;
	}): Observable<Spell[]> {
		let httpParams = new HttpParams();

		if (params?.name) {
			httpParams = httpParams.set('name', params.name);
		}
		if (params?.niveau?.length) {
			for (const n of params.niveau) {
				httpParams = httpParams.append('niveau', n.toString());
			}
		}
		if (params?.type?.length) {
			for (const t of params.type) {
				httpParams = httpParams.append('type', t);
			}
		}
		if (params?.rapide !== undefined) {
			httpParams = httpParams.set('rapide', String(params.rapide));
		}
		if (params?.sort_by) {
			httpParams = httpParams.set('sort_by', params.sort_by);
		}
		if (params?.sort_order) {
			httpParams = httpParams.set('sort_order', params.sort_order);
		}

		return this.http.get<Spell[]>(this.apiUrl, { params: httpParams });
	}
}
