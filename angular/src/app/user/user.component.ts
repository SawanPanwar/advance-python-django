import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  form: any = {
    data: {},
    inputerror: {},
    message: '',
    preload: []
  }

  fileToUpload: any = null;

  constructor(private httpClient: HttpClient, private route: ActivatedRoute) {
    this.route.params.subscribe((params: any) => {
      this.form.data.id = params["id"] ?? 0;
      console.log("id ====>>> ", this.form.data.id)
    })
  }


  ngOnInit(): void {
    if (this.form.data.id && this.form.data.id > 0) {
      this.display();
    }
  }

  display() {
    this.httpClient.get('http://localhost:8000/ORSAPI/get/' + this.form.data.id + '/').subscribe((res: any) => {
      console.log(res)
      this.form.data = res.result.data;
    });
  }

  save() {
    this.httpClient.post('http://localhost:8000/ORSAPI/save/', this.form.data).subscribe((res: any) => {
      console.log('res => ', res)

      this.form.message = '';

      if (res.result.message) {
        this.form.message = res.result.message;
      }
    });
  }
}
