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

    return next.handle(req);
  }
}
