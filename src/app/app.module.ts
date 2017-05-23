import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
// import FormsModule from @angular/forms library
import { FormsModule }   from '@angular/forms';

import { AppComponent }  from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { DashboardComponent } from './dashboard.component';
import { HeroesComponent } from './heroes.component';
import { HeroService } from './hero.service';
import { HeroDetailComponent } from './hero-detail.component';

@NgModule({
  // imports is an array of the external modules the app uses.
  imports:      [
    BrowserModule,
    FormsModule, //FormsModule lets us bind with [(ngModel)]
    AppRoutingModule
  ],
  // here we declare the app's required directives
  declarations: [
    AppComponent,
    DashboardComponent,
    HeroesComponent,
    HeroDetailComponent
    ],
  // put stuff in providers array when you need it in every other view.
  providers: [
    HeroService
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
