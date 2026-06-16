from django.db import connection


class UserService:

    def next_pk(self):
        pk = 0
        cursor = connection.cursor()
        sql = "select max(id) from sos_user"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.close()
        return pk + 1

    def add(self, data):
        id = UserService.next_pk(self)
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        dob = data['dob']
        address = data['address']

        user_exist = self.find_by_login(login_id)

        if len(user_exist) > 0:
            raise Exception('Login ID already exist')

        cursor = connection.cursor()
        sql = "insert into sos_user values(%s, %s, %s, %s, %s, %s, %s)"
        data = (id, first_name, last_name, login_id, password, dob, address)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        dob = data['dob']
        address = data['address']

        user_exist = self.find_by_login(login_id)

        if len(user_exist) > 0 and user_exist[0].get('id') != id:
            raise Exception('Login ID already exist')

        cursor = connection.cursor()
        sql = "update sos_user set first_name = %s, last_name = %s,login_id = %s, password = %s, dob = %s, address = %s where id = %s"
        data = (first_name, last_name, login_id, password, dob, address, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, id):
        cursor = connection.cursor()
        sql = "delete from sos_user where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        cursor = connection.cursor()
        sql = "select * from sos_user where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "firstName", "lastName", "loginId", "password", "dob", "address")
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def find_by_login(self, login_id):
        cursor = connection.cursor()
        sql = "select * from sos_user where login_id = %s"
        data = (login_id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "firstName", "lastName", "loginId", "password", "dob", "address")
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def authenticate(self, login_id, password):
        cursor = connection.cursor()
        sql = "select * from sos_user where login_id = %s and password = %s"
        data = (login_id, password)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "firstName", "lastName", "loginId", "password", "dob", "address")
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def search(self, data):
        first_name = data.get('first_name', '')
        dob = data.get('dob', 0)
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)
        cursor = connection.cursor()
        sql = "select * from sos_user where 1=1"
        if first_name != '':
            sql += " and first_name='" + first_name + "'"
        if dob != 0:
            sql += " and dob= " + str(dob)
        if (page_size > 0):
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "firstName", "lastName", "loginId", "password", "dob", "address")
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res
