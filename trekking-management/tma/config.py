class Config:
    SECRET_KEY = "123456"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/tma"

    SQLALCHEMY_TRACK_MODIFICATIONS = False