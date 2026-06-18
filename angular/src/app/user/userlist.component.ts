import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-userlist',
  templateUrl: './userlist.component.html',
  styleUrls: ['./userlist.component.css']
})
export class UserlistComponent implements OnInit {

  form: any = {
    list: [],
    searchParams: {
      id: null,
      firstName: ''
    },
    deleteParams: {},
    preload: [],
    message: '',
    pageNo: 0
  }

  constructor(private httpClient: HttpClient, private router: Router) {

  }

  ngOnInit(): void {
    this.preload();
    this.search();
  }

  next() {
    this.form.pageNo++;
    console.log('pageNo => ', this.form.pageNo)
    this.search();
  }

  previous() {
    this.form.pageNo--;
    console.log('pageNo => ', this.form.pageNo)
    this.search();
  }

  preload() {
    this.httpClient.get('http://localhost:8000/ORSAPI/preload/').subscribe((res: any) => {
      this.form.preload = res.result.preload;
    });
  }

  search() {
    this.httpClient.post('http://localhost:8000/ORSAPI/search/' + this.form.pageNo + '/', this.form.searchParams).subscribe((res: any) => {
      this.form.list = res.result.data;
    })
  }

  edit(page: any) {
    this.router.navigateByUrl(page);
  }

  onCheckboxChange(userId: number) {
    console.log('Checkbox with ID', userId, 'is checked/unchecked');
    this.form.deleteParams.id = userId;
  }

  delete() {
    this.httpClient.get('http://localhost:8000/ORSAPI/delete/' + this.form.deleteParams.id + '/').subscribe((res: any) => {
      this.form.message = res.result.message;
      console.log('message => ', this.form.message)
      this.form.pageNo = 0;
      this.search();
    });
  }
}