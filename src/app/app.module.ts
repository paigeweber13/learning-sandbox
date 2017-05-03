import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
//import FormsModule from @angular/forms library
import { FormsModule }   from '@angular/forms';

import { AppComponent }  from './app.component';

@NgModule({
  //imports is an array of the external modules the app uses.
  imports:      [
    BrowserModule,
    FormsModule, //FormsModule lets us bind with [(ngModel)]
  ],
  declarations: [ AppComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
