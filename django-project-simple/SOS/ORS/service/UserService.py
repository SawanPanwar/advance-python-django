from django.db import connection


class UserService:

    def nextPk(self):
        pk = 0
        with connection.cursor() as cursor:
            sql = "select max(id) from sos_user"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        return pk + 1

    def add(self, data):
        f = data['firstName']
        l = data['lastName']
        e = data['loginId']
        p = data['password']
        d = data['dob']
        a = data['address']

        sql = "insert into sos_user values((%s), (%s), (%s), (%s), (%s), (%s), (%s))"
        data = [UserService.nextPk(self), f, l, e, p, d, a]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def update(self, data):
        f = data['firstName']
        l = data['lastName']
        e = data['loginId']
        p = data['password']
        d = data['dob']
        a = data['address']
        i = data['id']
        sql = "update sos_user set firstName = (%s), lastName = (%s), loginId = (%s), password = (%s), dob = (%s), address = (%s) where id = (%s)"
        data = [f, l, e, p, d, a, i]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def delete(self, id):
        sql = "delete from sos_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def auth(self, e, p):
        sql = "select * from sos_user where loginId = (%s) and password = (%s)"
        data = [e, p]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "loginId", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get(self, id):
        sql = "select * from sos_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "loginId", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def findByLogin(self, loginId):
        sql = "select * from sos_user where loginId = (%s)"
        data = [loginId]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "loginId", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def search(self, params):
        fname = params.get("firstName", "")
        pageNo = params.get("pageNo", 0)
        pageSize = params.get("pageSize", 0)
        sql = "select * from sos_user where 1=1"
        if fname != "":
            sql += " and firstName like '" + fname + "%%' "
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit %s, %s"
        print('sql => ', sql)
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, pageSize])
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "loginId", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res
