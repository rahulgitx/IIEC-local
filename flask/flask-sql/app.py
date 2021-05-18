from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask('iiecapp')
app.config['SQLALCHENY_DATABASE-URI']='sqlit:///DB/data.sqlite'


#ORM
db=SQLAlchemy(app)
print(db)

class iiec9(db.model)