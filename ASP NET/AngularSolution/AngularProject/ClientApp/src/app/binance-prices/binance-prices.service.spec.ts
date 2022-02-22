import { Inject, Injectable,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subscription, interval } from 'rxjs';

@Injectable({
  providedIn: 'root'
})


export class BinancePricesService {


  constructor(private http: HttpClient) { }
  getData() {
    let url = "https://api.binance.com/api/v3/ticker/price";
    return this.http.get(url);
  }


 
}
