import { Injectable } from '@angular/core';
import { Hero } from './hero';
import { HEROES } from './mock-heroes';

// * @Injectable() is a decorator that tells TS to emit metadata about this
//   service. This specifies that Angular may need to inject other dependencies
//   into this service. For now there are no dependencies, but that might
//   change. Thus, this is for future-proofing.
@Injectable()
export class HeroService {
    //This is a promise. A promise promises to call back when the results are
    //ready. You describe the work the asynchronus service will do and give it
    //a callback function. The service does the work and then calls the
    //function with the results or an error.
    getHeroes(): Promise<Hero[]> {
        return Promise.resolve(HEROES);
    };
    getHeroesSlowly(): Promise<Hero[]>{
        return new Promise(resolve => {
            //Simulate server lateny with 2 second delay
            setTimeout(() => resolve(this.getHeroes()), 2000);
        });
    }
}