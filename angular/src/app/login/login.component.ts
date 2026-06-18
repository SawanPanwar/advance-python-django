import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  form: any = {
    data: {},
    message: '',
  }

  constructor(private httpClient: HttpClient, public router: Router) {

  }

  signIn() {
    this.httpClient.post('http://localhost:8000/ORSAPI/login/', this.form.data).subscribe((res: any) => {
      console.log('res => ', res)
      this.form.message = '';

      if (res.result.message) {
        this.form.message = res.result.message;
      }

      if (res.result.data != null) {
        localStorage.setItem('firstName', res.result.data.firstName)
        this.router.navigateByUrl('welcome');
      }
    })
  }

  signUp() {
    this.router.navigateByUrl('signup');
  }
}