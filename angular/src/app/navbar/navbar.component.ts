import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {

  form: any = {
    data: {}
  }

  constructor(private router: Router) { }

  isLogin() {
    let check = localStorage.getItem('firstName');
    if (check != "null" && check != null) {
      this.form.data.firstName = localStorage.getItem("firstName");
      return true;
    } else {
      return false;
    }
  }

  logout() {
    localStorage.clear();
    this.router.navigateByUrl('/login')
  }

}