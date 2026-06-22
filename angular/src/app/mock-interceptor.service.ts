import { Injectable } from '@angular/core';
import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpResponse
} from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { delay } from 'rxjs/operators';

@Injectable()
export class MockInterceptorService implements HttpInterceptor {

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {

    if (req.method === 'POST' && req.url.includes('/ORSAPI/signUp/')) {
      return of(new HttpResponse({
        status: 200,
        body: {
          result: {
            message: 'User Registered Successfully'
          }
        }
      })
      ).pipe(delay(1000)); // optional delay
    }

    if (req.method === 'POST' && req.url.includes('/ORSAPI/login/')) {
      const data = req.body;
      if (data.loginId === 'admin' && data.password === 'admin') {
        return of(
          new HttpResponse({
            status: 200,
            body: {
              result: {
                data: {
                  id: 1,
                  firstName: 'Sawan',
                  lastName: 'Panwar',
                  loginId: 'admin'
                }
              }
            }
          })
        ).pipe(delay(1000));
      }

      return of(
        new HttpResponse({
          status: 200,
          body: {
            result: {
              message: 'Invalid Login ID & Password'
            }
          }
        })
      ).pipe(delay(1000));
    }

    let allData = [
      {
        id: 1,
        firstName: 'klm',
        lastName: 'klm',
        loginId: 'abc@gmail.com',
        password: '123',
        dob: '2020-01-01',
        address: 'indore'
      },
      {
        id: 3,
        firstName: 'Bharat',
        lastName: 'Chikhaliya',
        loginId: 'bharat@gmail.com',
        password: '123',
        dob: '2024-06-01',
        address: 'indore'
      },
      {
        id: 4,
        firstName: 'Rahul',
        lastName: 'Singh',
        loginId: 'rahul@gmail.com',
        password: '123',
        dob: '2024-06-01',
        address: 'indore'
      },
      {
        id: 8,
        firstName: 'Shubham',
        lastName: 'Singh',
        loginId: 'shubham@gmail.com',
        password: '123',
        dob: '2022-01-01',
        address: 'indore'
      },
      {
        id: 10,
        firstName: 'Vishal',
        lastName: 'Vishwakarma',
        loginId: 'vishal@gmail.com',
        password: '123',
        dob: '2025-04-02',
        address: 'Indore'
      },
      {
        id: 11,
        firstName: 'Amit',
        lastName: 'Sharma',
        loginId: 'amit@gmail.com',
        password: '123',
        dob: '2021-01-01',
        address: 'Bhopal'
      },
      {
        id: 12,
        firstName: 'Rohit',
        lastName: 'Verma',
        loginId: 'rohit@gmail.com',
        password: '123',
        dob: '2023-05-10',
        address: 'Ujjain'
      }
    ];


    if (req.method === 'POST' && req.url.includes('/ORSAPI/search/')) {

      const pageNo = parseInt(req.url.split('/search/')[1]);

      const search = req.body;

      // Search by firstName
      if (search.firstName) {
        allData = allData.filter(user =>
          user.firstName.toLowerCase().startsWith(
            search.firstName.toLowerCase()
          )
        );
      }

      const pageSize = 5;

      const start = pageNo * pageSize;
      const end = start + pageSize;
      const pageData = allData.slice(start, end);

      return of(
        new HttpResponse({
          status: 200,
          body: {
            result: {
              data: pageData,
            }
          }
        })
      ).pipe(delay(500));
    }

    if (req.method === 'GET' && req.url.includes('/ORSAPI/get/')) {

      const id = parseInt(req.url.split('/get/')[1]);

      const user = allData.find(x => x.id === id);

      return of(
        new HttpResponse({
          status: 200,
          body: {
            result: {
              data: user
            }
          }
        })
      );
    }

    return next.handle(req);
  }
}
