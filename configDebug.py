# coding=utf-8
class debugConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy
    # 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_ECHO = True
    # 打印sql

    DEBUG = True
