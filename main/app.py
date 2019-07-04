from flask import Flask
from flask_sqlalchemy import SQLAlchemy

appConf = Flask(__name__)
appConf.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ghostbuster/DevTools/workspace/cubejsGenerator/test.db'
#appConf.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/DevTools/eclipse/workspace/test.db'
appConf.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(appConf)
