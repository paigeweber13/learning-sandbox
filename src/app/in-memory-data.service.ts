import { InMemoryDbService } from 'angular-in-memory-web-api';

export class InMemoryDataService implements InMemoryDbService {
    createDb() {
        // * array of heroes. Commented names are names of heroes from tutorial.
        let heroes = [
            { id: 1,  name: 'Aphrodite',  imgFullPath: '/assets/aphrodite.png'  }, // Windstorm
            { id: 2,  name: 'Hephaestos', imgFullPath: '/assets/hephaestos.png' }, // Mr. Nice
            { id: 3,  name: 'Eros',       imgFullPath: '/assets/eros.png'       }, // Narco
            { id: 4,  name: 'Dionysos',   imgFullPath: '/assets/dionysos.png'   }, // Bombasto
            { id: 5,  name: 'Achilles',   imgFullPath: '/assets/achilles.png'   }, // Celeritas
            { id: 6,  name: 'Athena',     imgFullPath: '/assets/athena.png'     }, // Magneta
            { id: 7,  name: 'Poseidon',   imgFullPath: '/assets/poseidon.png'   }, // RubberMan
            { id: 8,  name: 'Artemis',    imgFullPath: '/assets/artemis.png'    }, // Dynama
            { id: 9,  name: 'Apollo',     imgFullPath: '/assets/apollo.png'     }, // Dr IQ
            { id: 10, name: 'Heracles',   imgFullPath: '/assets/heracles.png'   }, // Magma
            { id: 11, name: 'Hermes',     imgFullPath: '/assets/hermes.png'     }, // Tornado
            { id: 12, name: 'Hera',       imgFullPath: '/assets/hera.png'       },
            { id: 13, name: 'Zeus',       imgFullPath: '/assets/zeus.png'       }
        ];
        return { heroes };
    }
}
