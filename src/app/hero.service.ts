import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Hero } from './hero';

// * @Injectable() is a decorator that tells TS to emit metadata about this
//   service. This specifies that Angular may need to inject other dependencies
//   into this service. For now there are no dependencies, but that might
//   change. Thus, this is for future-proofing.
@Injectable()
export class HeroService {
    private heroesUrl = 'api/heroes'; // URL to web api
    private headers = new Headers({ 'Content-Type': 'application/json' });

    constructor(private http: Http) {}

    // This is a promise. A promise promises to call back when the results are
    // ready. You describe the work the asynchronus service will do and give it
    // a callback function. The service does the work and then calls the
    // function with the results or an error.
    getHeroes(): Promise<Hero[]> {
        return this.http.get(this.heroesUrl)
                        .toPromise()
                        .then(response => response.json().data as Hero[])
                        .catch(this.handleError);
    };
    getHeroesSlowly(): Promise<Hero[]> {
        return new Promise(resolve => {
            // Simulate server lateny with 2 second delay
            setTimeout(() => resolve(this.getHeroes()), 2000);
        });
    }
    getHero(id: number): Promise < Hero > {
        const url = `${this.heroesUrl}/${id}`;
        return this.http.get(url)
            .toPromise()
            .then(response => response.json().data as Hero)
            .catch(this.handleError);
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occured', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }

    update(hero: Hero): Promise<Hero> {
        const url = `${this.heroesUrl}/${hero.id}`;
        return this.http
            .put(url, JSON.stringify(hero), { headers: this.headers })
            .toPromise()
            .then(() => hero)
            .catch(this.handleError);
    }

    create(name: String): Promise<Hero> {
        return this.http
            .post(this.heroesUrl, JSON.stringify({name: name}), {headers: this.headers})
            .toPromise()
            .then(res => res.json().data as Hero)
            .catch(this.handleError);
    }

    // Typescript vs. Javascript
    /*
    return this.getHeroes()
        .then(heroes => heroes.find(
            hero => hero.id === id));

    // Javascript equivalent:
    
    return this.getHeroes()
        .then(function (heroes) { return heroes.find(
            function (hero) { return hero.id === id; }); });
    */
}
