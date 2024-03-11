from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:jose1984br@localhost:3306/seu_embarque'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

