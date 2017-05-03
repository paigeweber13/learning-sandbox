import { Component } from '@angular/core';

//creating a class for a hero
export class Hero {
  //seems like this is how we declare the types of variables in typescript
  id: number;
  name: string;
}

// * array of heroes. Commented names are names of heroes from tutorial.
// * array is names HEROES (is all caps something they do with const?)
//   and this array is of type Hero.
// * this is separate from a class implementation (I guess that's what export
//   class means) because we'll eventually take these from a data source.
const HEROES: Hero[] = [
  { id: 1, name: 'Aphrodite' }, //Windstorm
  { id: 2, name: 'Hephaestos' }, //Mr. Nice
  { id: 3, name: 'Eros' },      //Narco
  { id: 4, name: 'Dionysos' },  //Bombasto
  { id: 5, name: 'Achilles' },  //Celeritas
  { id: 6, name: 'Athena' },    //Magneta
  { id: 7, name: 'Poseidon' },  //RubberMan
  { id: 8, name: 'Artemis' },   //Dynama
  { id: 9, name: 'Apollo' },    //Dr IQ
  { id: 10, name: 'Heracles' }, //Magma
  { id: 11, name: 'Hermes' },   //Tornado
  { id: 12, name: 'Hera' },
  { id: 13, name: 'Zeus' }
]

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
  // * that fun little [()] indicates two-way binding.
  // * ngModel won't work unless you opt-in to using the module "FormsModule".
  //   this is done in app.module.ts
  template: `
    <h1>{{title}}</h1>
    <h2>My Heroes</h2>
    <ul class="heroes">
      <li *ngFor="let hero of heroes" (click)="onSelect(hero)">
        <span class="badge">{{hero.id}}</span> {{hero.name}}
      </li>
    </ul>
    <div *ngIf="selectedHero">
      <h2>{{selectedHero.name}} details:</h2>
      <div><label>id: </label>{{selectedHero.id}}</div>
      <div>
        <label>name: </label>
        <input [(ngModel)]=selectedHero.name placeholder="Hero Name">
      </div>
    </div>
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
  `]
})

//adding properties here is adding properties to the AppComponent
export class AppComponent {
  title = 'Tour of Heroes';
  // * type of heroes isn't declared because TS infers it from
  //   the array.
  // * below I'm saying that the component's property 'hero' is declared as
  //   being of type Hero, then initializing it with some values for id and
  //   name
  heroes = HEROES;
  //we're just declaring the type of selectedHero here, right?
  selectedHero: Hero;

  onSelect(hero: Hero): void {
    //hero comes from the parameter passed to onSelect
    this.selectedHero = hero;
  }

  // hero: Hero = {
  //   id: 1,
  //   name: 'Aphrodite'
  // }
}
