import { Hero } from './hero';

// * array of heroes. Commented names are names of heroes from tutorial.
// * array is names HEROES (is all caps something they do with const?)
//   and this array is of type Hero.
// * this is separate from a class implementation (I guess that's what export
//   class means) because we'll eventually take these from a data source.
export const HEROES: Hero[] = [
    { id: 1, name: 'Aphrodite' },  //Windstorm
    { id: 2, name: 'Hephaestos' }, //Mr. Nice
    { id: 3, name: 'Eros' },       //Narco
    { id: 4, name: 'Dionysos' },   //Bombasto
    { id: 5, name: 'Achilles' },   //Celeritas
    { id: 6, name: 'Athena' },     //Magneta
    { id: 7, name: 'Poseidon' },   //RubberMan
    { id: 8, name: 'Artemis' },    //Dynama
    { id: 9, name: 'Apollo' },     //Dr IQ
    { id: 10, name: 'Heracles' },   //Magma
    { id: 11, name: 'Hermes' },     //Tornado
    { id: 12, name: 'Hera' },
    { id: 13, name: 'Zeus' }
]