import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { Hero } from './hero';
import { HeroService } from './hero.service';

// so this is called a decorator?
@Component({
  selector: 'my-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css'],
  // this array tells Angular to make a fresh instance of the HeroService when
  // it creates AppComponent. AppComponent and its children can use this service
  // providers: [HeroService]
  // * promoted to app.module
})

// adding properties here is adding properties to the AppComponent
export class HeroesComponent {
  heroes: Hero[];
  // we're just declaring the type of selectedHero here, right?
  selectedHero: Hero;

  // all this does is defines a heroSevice property (which is private) and
  // identifies it as an injection site for HeroService. Now Angular knows
  // to provide an instance of the HeroService when it creates AppComponent
  // *** however, it doesn't know HOW to provide this service until ***
  // *** you add HeroService to the providers array in the          ***
  // *** @Component call                                            ***
  constructor(
    private heroService: HeroService,
    private router: Router
  ) {}
  // this is called a lifecycle hook. For more info, see
  // https://angular.io/docs/ts/latest/guide/lifecycle-hooks.html
  ngOnInit(): void {
    this.getHeroes();
  }

  onSelect(hero: Hero): void {
    // hero comes from the parameter passed to onSelect
    this.selectedHero = hero;
  }

  getHeroes(): void {
    // arrow thing means that we have an anonymous function with a parameter
    // "heroes", and when it is called it returns "this.heroes = heroes"
    this.heroService.getHeroes().then(heroes => this.heroes = heroes);
  }

  gotoDetail(): void {
    this.router.navigate(['/detail', this.selectedHero.id]);
  }

  add(name: string): void {
    name = name.trim();
    if (!name) { return; }
    this.heroService.create(name)
      .then(hero => {
        this.heroes.push(hero);
        this.selectedHero = null;
      });
  }

  delete(hero: Hero): void {
    this.heroService
      .delete(hero.id)
      .then(() => {
        this.heroes = this.heroes.filter(h => h !== hero);
        if (this.selectedHero === hero) { this.selectedHero = null; }
      });
  }

  // -------deprecated stuff kept because learning:-------

  // * type of heroes isn't declared because TS infers it from
  //   the array.
  // heroes = HEROES;

  // * below I'm saying that the component's property 'hero' is declared as
  //   being of type Hero, then initializing it with some values for id and
  //   name
  // hero: Hero = {
  //   id: 1,
  //   name: 'Aphrodite'
  // }
}
