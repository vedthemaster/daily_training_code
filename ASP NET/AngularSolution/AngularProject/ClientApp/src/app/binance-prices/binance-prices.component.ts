
import { Component, Inject} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BinancePricesService } from './binance-prices.service.spec';

@Component({
  selector: 'binance-prices',
  templateUrl: './binance-prices.component.html'
})

export class BinancePricesComponent {

  finaldata: any;

  constructor(private prices: BinancePricesService) {
    this.prices.getData().subscribe(data => {
      console.log(data)
      this.finaldata = data;
    });
  }

}


