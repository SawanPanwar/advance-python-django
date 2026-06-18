import { TestBed } from '@angular/core/testing';

import { MockInterceptorService } from './mock-interceptor.service';

describe('MockInterceptorService', () => {
  let service: MockInterceptorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MockInterceptorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
