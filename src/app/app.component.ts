import { Component } from '@angular/core';

// this is a router component: it is attached to a router and displays
// routed views.
@Component({
    selector: 'my-app',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})

export class AppComponent {
    title = 'Tour of Heroes';
}
