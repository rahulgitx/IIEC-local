from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask('iiecapp')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb\data.sqlite'


#ORM
db=SQLAlchemy(app)
print(db)

class iiec(db.Model):
    iid=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    remarks=db.Column(db.Text)
    
    def __init__(self, name, age, remarks):
        self.name=name
        self.age=age
        self.remarks=remarks

db.create_all()

#CREATE
'''
vimal=iiec("vimal", 20, "ok")
db.session.add(vimal)
db.session.commit()

rahul=iiec("rahul", 23, "ok")
db.session.add(rahul)
db.session.commit()
'''

#READ
r2=iiec.query.get(3)
print(r2.name, r2.age)

rall=iiec.query.all()
print(rall[0].name)