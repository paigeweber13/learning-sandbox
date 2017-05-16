//need this everywhere we define a component
import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';

import { Hero } from './hero';
import { HeroService } from './hero.service';

//provides Angular metadata for the component
@Component({
    //selector will be used to identify this component in parent templates
    selector:'hero-detail',
    template: `
    <div *ngIf="hero"> <!-- only shows if ngIf statement is truthy -->
      <h2>{{hero.name}} details:</h2>
      <div><label>id: </label>{{hero.id}}</div>
      <div>
        <label>name: </label>
        <input [(ngModel)]=hero.name placeholder="Hero Name">
      </div>
    </div>
    `
})
//always export the component class because you'll always import it elsewhere.
export class HeroDetailComponent implements OnInit {
    //this component receives a hero object and then binds that object's
    //properties to its template.
    @Input() hero: Hero;
    constructor(
      private heroService: HeroService,
      private route: ActivatedRoute,
      private location: Location
    ) {}

    //route.params is an observable.
    ngOnInit(): void {
      this.route.params
      .switchMap((params: Params) => this.heroService.getHero(+params['id']))
      .subscribe(hero => this.hero = hero);
    }
}