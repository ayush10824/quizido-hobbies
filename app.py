from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    hobby= db.Column(db.String(500),nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow)
    
with app.app_context():
    db.create_all()

def __repr__(self)->str:
    return f"{self.id}+{self.name}"
    
@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        name=request.form['name']
        hobby=request.form['hobby']
        object=User(name=name,hobby=hobby)
        db.session.add(object)
        db.session.commit()
    ob=User.query.all()
    return render_template('index.html',ob=ob)

@app.route("/delete/<int:id>")
def delete(id):
    object=User.query.filter_by(id=id).first()
    db.session.delete(object)
    db.session.commit()
    return redirect("/")
    
@app.route("/update/<int:id>",methods=['GET','POST'])
def update(id):
    if request.method=="POST":
        name=request.form.get('name')
        hobby=request.form.get('hobby')
        object= User.query.filter_by(id=id).first()
        object.name=name
        object.hobby=hobby
        db.session.add(object)
        db.session.commit()
        return redirect('/')

    object= User.query.filter_by(id=id).first()
   
    return render_template('update.html',object=object)
if __name__=="__main__":
    app.run(debug=True)
