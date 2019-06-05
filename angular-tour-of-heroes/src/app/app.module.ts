import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
// import FormsModule from @angular/forms library
import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';

// Imports for loadinmg and configuring the in-memory web api
import { InMemoryWebApiModule } from 'angular-in-memory-web-api';
import { InMemoryDataService } from './in-memory-data.service';

import { AppComponent }  from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { DashboardComponent } from './dashboard.component';
import { HeroesComponent } from './heroes.component';
import { HeroSearchComponent } from './hero-search.component';
import { HeroService } from './hero.service';
import { HeroDetailComponent } from './hero-detail.component';

@NgModule({
  // imports is an array of the external modules the app uses.
  imports:      [
    BrowserModule,
    FormsModule, // FormsModule lets us bind with [(ngModel)]
    HttpModule,
    InMemoryWebApiModule.forRoot(InMemoryDataService),
    AppRoutingModule
  ],
  // here we declare the app's required directives
  declarations: [
    AppComponent,
    DashboardComponent,
    HeroesComponent,
    HeroSearchComponent,
    HeroDetailComponent
    ],
  // put stuff in providers array when you need it in every other view.
  providers: [
    HeroService
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
