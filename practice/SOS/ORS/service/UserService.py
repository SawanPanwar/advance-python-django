from django.db import connection
from ..models import User


class UserService:

    def save(self, mobj):
        mobj.save()

    def authenticate(self, params):
        q = User.objects.filter()
        val = params.get("loginId", None)
        q = q.filter(loginId=val)
        val = params.get("password", None)
        q = q.filter(password=val)
        userList = [user.to_json() for user in q]
        print("=================>>>>>>>>>>>>>>>", type(userList[0]), userList[0])
        if (userList[0]):
            return userList[0]
        else:
            return None

    def search(self, params):
        pageNo = (params["pageNo"] - 1) * 5
        print("pageNo ======>>>>>>>", pageNo)
        fname = params.get("firstName", "")
        lname = params.get("lastName", "")
        id = params.get("id", "")
        sql = "select * from sos_user where 1=1"
        if fname != "":
            sql += " and firstName like '" + fname + "%%' "
        if lname != "":
            sql += " and lastName like '" + lname + "%%' "
        if id != "":
            sql += " and id = " + id
        sql += " limit %s, %s"
        print("sql ======>>>>>>", sql)
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, 5])
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "loginId", "password")
        res = {
            "data": []
        }
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def edit(self, val):
        q = User.objects.filter()
        q = q.filter(id=val)
        userList = [user.to_json() for user in q]
        if (userList[0]):
            return userList[0]
        else:
            return None

    def get(self, id):
        r = User.objects.get(id=id)
        return r

    def delete(self, obj):
        obj.delete()

    def preload(self):
        r = User.objects.all()
        return r
