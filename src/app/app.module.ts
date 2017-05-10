import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
//import FormsModule from @angular/forms library
import { FormsModule }   from '@angular/forms';

import { AppComponent }  from './app.component';
import { HeroDetailComponent } from './hero-detail.component';

@NgModule({
  //imports is an array of the external modules the app uses.
  imports:      [
    BrowserModule,
    FormsModule, //FormsModule lets us bind with [(ngModel)]
  ],
  //here we declare the app's required directives
  declarations: [ 
    AppComponent,
    HeroDetailComponent
    ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
