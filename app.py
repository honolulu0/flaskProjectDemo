# coding=utf-8
from flask import Flask

from configDebug import debugConfig
from dataBase import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config.from_object(debugConfig)
#app 的配置
db.init_app(app)
# 测试推送 666666333
# 初始化数据库对象
if __name__ == '__main__':
    app.run('127.0.0.1',8888)

