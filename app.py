from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///employeedata.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True)
    first_name=db.Column(db.String(100),nullable=False)
    last_name=db.Column(db.String(100),nullable=False)
    contact=db.Column(db.String(10),nullable=False)
    address=db.Column(db.String(150),nullable=False)
    city=db.Column(db.String(100),nullable=False)
    designation=db.Column(db.String(100),nullable=False)
    company=db.Column(db.String(100),nullable=False)
    
@app.route('/', methods=['GET','POST'])
def home():
    if request.method=="POST":
        first_name=request.form['firstname']
        last_name=request.form['lastname']
        email=request.form['email']
        city=request.form['city']
        company=request.form['company']
        address=request.form['address']
        designation=request.form['design']
        contact=request.form['contact']
        data=Employee(first_name=first_name,last_name=last_name,email=email,city=city,company=company,designation=designation,address=address,contact=contact)
        db.session.add(data)
        db.session.commit()
    emp=Employee.query.all()
    return render_template('index.html',emp=emp)

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    if request.method=="POST":
        first_name=request.form['firstname']
        last_name=request.form['lastname']
        email=request.form['email']
        city=request.form['city']
        company=request.form['company']
        address=request.form['address']
        designation=request.form['design']
        contact=request.form['contact']
        data=Employee.query.filter_by(id=id).first()
        data.first_name=first_name
        data.last_name=last_name
        data.email=email
        data.city=city
        data.company=company
        data.address=address
        data.designation=designation
        data.contact=contact
        db.session.add(data)
        db.session.commit()
        return redirect('/')
    emp=Employee.query.filter_by(id=id).first()
    return render_template('update.html',emp=emp)

@app.route('/delete/<int:id>',)
def delete(id):
        data=Employee.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()
        return redirect('/')


with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True,port=7000)
