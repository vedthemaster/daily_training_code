import { Component, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'section',
  templateUrl: './section.component.html'
})

export class SectionComponent {

  public sections: Section[];

  constructor(http: HttpClient, @Inject('BASE_URL') baseUrl: string) {
    http.get<Section[]>(baseUrl + 'api/SectionsApi').subscribe(result => {

      console.log(result);

      this.sections = result;
      console.log(this.sections);

    }, error => console.error(error));
  }
}

interface Section {
  sectionId: number,
  sectionName: string;
}
