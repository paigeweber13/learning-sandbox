import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
//import FormsModule from @angular/forms library
import { FormsModule }   from '@angular/forms';
import { RouterModule }   from '@angular/router';

import { AppComponent }  from './app.component';
import { DashboardComponent } from './dashboard.component';
import { HeroesComponent } from './heroes.component';
import { HeroDetailComponent } from './hero-detail.component';
import { HeroService } from './hero.service';

let Routes: Object[] = [
  {
    path: '',
    redirectTo: '/dashboard',
    pathMatch: 'full'
  },
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: 'heroes',
    component: HeroesComponent
  },
  {
    path: 'detail/:id',
    component: HeroDetailComponent
  }
];

@NgModule({
  //imports is an array of the external modules the app uses.
  imports:      [
    BrowserModule,
    FormsModule, //FormsModule lets us bind with [(ngModel)]
    RouterModule.forRoot(Routes)
  ],
  //here we declare the app's required directives
  declarations: [ 
    AppComponent,
    DashboardComponent,
    HeroesComponent,
    HeroDetailComponent
    ],
  //put stuff in providers array when you need it in every other view.
  providers: [
    HeroService
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { } 