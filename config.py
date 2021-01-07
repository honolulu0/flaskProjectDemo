# coding=utf-8
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'xpit'
CHARSET = '?charset=UTF8'
SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}{}'.format(
    DIALECT,
    USERNAME,
    PASSWORD,
    HOST,
    PORT,
    DATABASE,
    CHARSET
)
JSON_AS_ASCII = False
JSONIFY_MIMETYPE = 'application/json;charset=utf-8'
print SQLALCHEMY_DATABASE_URI