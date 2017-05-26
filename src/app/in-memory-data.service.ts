import { InMemoryDbService } from 'angular-in-memory-web-api';

export class InMemoryDataService implements InMemoryDbService {
    createDb() {
        // * array of heroes. Commented names are names of heroes from tutorial.
        let heroes = [
            { id: 1, name: 'Aphrodite' },  // Windstorm
            { id: 2, name: 'Hephaestos' }, // Mr. Nice
            { id: 3, name: 'Eros' },       // Narco
            { id: 4, name: 'Dionysos' },   // Bombasto
            { id: 5, name: 'Achilles' },   // Celeritas
            { id: 6, name: 'Athena' },     // Magneta
            { id: 7, name: 'Poseidon' },   // RubberMan
            { id: 8, name: 'Artemis' },    // Dynama
            { id: 9, name: 'Apollo' },     // Dr IQ
            { id: 10, name: 'Heracles' },  // Magma
            { id: 11, name: 'Hermes' },    // Tornado
            { id: 12, name: 'Hera' },
            { id: 13, name: 'Zeus' }
        ];
        return { heroes };
    }
}
