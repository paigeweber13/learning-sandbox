import { Component } from '@angular/core';

//creating a class for a hero
export class Hero {
  //seems like this is how we declare the types of variables in typescript
  id: number;
  name: string;
}

//array of heroes. Commented names are names of heroes from tutorial.
const HEROES: Hero[] = [
  { id: 2, name: 'Hephaestos'}, //Mr. Nice
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
  // * double curly braces are the syntax for "interpolation binding"
  // * because I'm using the backticks, I can put parts of the string on their
  //   own lines. You can also embedd expressions into one of these so-called
  //   "template literals" with the following syntax: `string ${expression}`
  //   expressions can be things like a variable name or (2+2)
  //   you can even pass the data to a function afterwards. This is cool!
  //   see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
  //   for more info

  template: `
    <h1>{{title}}</h1>
    <h2>{{hero.name}} details:</h2>
    <div><label>id: </label>{{hero.id}}</div>
    <div>
      <label>name: </label>
      <input [(ngModel)]=hero.name placeholder="Hero Name">
    </div>
    `,
  // * that fun little [()] indicates two-way binding.
  // * ngModel won't work unless you opt-in to using the module "FormsModule".
  //   this is done in app.module.ts
})

//adding properties here is adding properties to the AppComponent
export class AppComponent  {
  title = 'Tour of Heroes';
  //below I'm saying that the component's property 'hero' is declared as
  //being of type Hero, then initializing it with some values for id and
  //name
  hero: Hero = {
    id: 1,
    name: 'Aphrodite' //Windstorm
  }
}
