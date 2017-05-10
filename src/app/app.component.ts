import { Component } from '@angular/core';
import { Hero } from './hero';
import { HeroService } from './hero.service';
import { OnInit } from '@angular/core';

//so this is called a decorator?
@Component({
  selector: 'my-app',

  // * template is a html. I assume you can also do it in another file.
  // * because I'm using the backticks, I can put parts of the string on their
  //   own lines. You can also embedd expressions into one of these so-called
  //   "template literals" with the following syntax: `string ${expression}`
  //   expressions can be things like a variable name or (2+2)
  //   you can even pass the data to a function afterwards. This is cool!
  //   see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
  //   for more info
  // * master/detail: master is the list of heroes, detail is the stuff about
  //   the selected hero below the list.
  // * the * prefix to ngFor is essential, apparently... The tutorial says that
  //   this indicates that the <li> element and it's children (what are its
  //   children?) constitute a master template (what's a master tempalte?)
  // * putting the ngFor inside the <li> tag makes multiple <li> elements.
  //   Moving it to the <ul> tag makes multiple <ul> elements.
  // * "let hero" indiacates that the variable hero will contain the current
  //   iteration's hero.
  // * parentheses around "click" indicate that the li element's "click" event
  //   is the target.
  // * double curly braces are the syntax for "interpolation binding"
  // * () indicates one way binding from user to program (from element in 
  //   markup to a component on the backend.) This is called event binding
  // * [] indicates one way binding from program to user (from component to
  //   an element in markup) - this is called property binding.
  // * that fun little [()] indicates two-way binding.
  // * ngModel won't work unless you opt-in to using the module "FormsModule".
  //   this is done in app.module.ts
  template: `
    <h1>{{title}}</h1>
    <h2>My Heroes</h2>
    <ul class="heroes">
      <li *ngFor="let hero of heroes"
          (click)="onSelect(hero)"
          [class.selected]="hero === selectedHero">
        <span class="badge">{{hero.id}}</span> {{hero.name}}
      </li>
    </ul>
    <hero-detail [hero]="selectedHero"></hero-detail>
    `,

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
  providers: [HeroService]
})

//adding properties here is adding properties to the AppComponent
export class AppComponent {
  title = 'Tour of Heroes';
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
