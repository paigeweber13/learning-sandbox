import { Component } from '@angular/core';
import { Hero } from './hero';
import { HeroService } from './hero.service';
import { OnInit } from '@angular/core';

//so this is called a decorator?
@Component({
  selector: 'my-heroes',
  templateUrl: './heroes.component.html',
  styles: [`
    .selected {
      background-color: #CFD8DC !important;
      color: white;
    }
    .heroes {
      margin: 0 0 2em 0;
      list-style-type: none;
      padding: 0;
      width: 15em;
    }
    .heroes li {
      cursor: pointer;
      position: relative;
      left: 0;
      background-color: #EEE;
      margin: .5em;
      padding: .3em 0;
      height: 1.6em;
      border-radius: 4px;
    }
    .heroes li.selected:hover {
      background-color: #BBD8DC !important;
      color: white;
    }
    .heroes li:hover {
      color: #607D8B;
      background-color: #DDD;
      left: .1em;
    }
    .heroes .text {
      position: relative;
      top: -3px;
    }
    .heroes .badge {
      display: inline-block;
      font-size: small;
      color: white;
      padding: 0.8em 0.7em 0 0.7em;
      background-color: #607D8B;
      line-height: 1em;
      position: relative;
      left: -1px;
      top: -4px;
      height: 1.8em;
      margin-right: .8em;
      border-radius: 4px 0 0 4px;
    }
  `],
  //this array tells Angular to make a fresh instance of the HeroService when
  //it creates AppComponent. AppComponent and its children can use this service
  //providers: [HeroService]
  // * promoted to app.module
})

//adding properties here is adding properties to the AppComponent
export class HeroesComponent {
  heroes: Hero[];
  //we're just declaring the type of selectedHero here, right?
  selectedHero: Hero;

  //all this does is defines a heroSevice property (which is private) and
  //identifies it as an injection site for HeroService. Now Angular knows
  //to provide an instance of the HeroService when it creates AppComponent
  // *** however, it doesn't know HOW to provide this service until ***
  // *** you add HeroService to the providers array in the          ***
  // *** @Component call                                            ***
  constructor(private heroService: HeroService) {}
  //this is called a lifecycle hook. For more info, see
  //https://angular.io/docs/ts/latest/guide/lifecycle-hooks.html
  ngOnInit(): void {
    this.getHeroes();
  }

  onSelect(hero: Hero): void {
    //hero comes from the parameter passed to onSelect
    this.selectedHero = hero;
  }

  getHeroes(): void {
    //arrow thing means that we have an anonymous function with a parameter
    //"heroes", and when it is called it returns "this.heroes = heroes"
    this.heroService.getHeroes().then(heroes => this.heroes = heroes);
  }

  //-------deprecated stuff kept because learning:-------

  // * type of heroes isn't declared because TS infers it from
  //   the array.
  //heroes = HEROES;

  // * below I'm saying that the component's property 'hero' is declared as
  //   being of type Hero, then initializing it with some values for id and
  //   name
  // hero: Hero = {
  //   id: 1,
  //   name: 'Aphrodite'
  // }
}
