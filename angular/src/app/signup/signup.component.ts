import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {

  form: any = {
    data: {},
    message: '',
  }

  constructor(private httpClient: HttpClient) {

  }

  signUp() {
    this.httpClient.post('http://localhost:8000/ORSAPI/signUp/', this.form.data).subscribe((res: any) => {
      console.log('res => ', res.result.message)
      this.form.message = res.result.message
    })
  }
}
