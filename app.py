from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
import json
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text, CheckConstraint, Sequence, Table, UniqueConstraint
from sqlalchemy.orm import relationship
import datetime

# from forms.project_form import CreateProject, EditProject
from forms.customer_form import CreateCustomer

import plotly
import plotly.graph_objs as go

app = Flask(__name__)
app.secret_key = 'key'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1111@localhost/Joseph'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mqgoxakulrqvbp:92ab46fc54c68204130010806e0ed5fd95128ab407e81529e07c63360da4f449@ec2-174-129-253-175.compute-1.amazonaws.com:5432/dad3l418d0q6kq'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class ormCustomer(db.Model):
    __tablename__ = 'customer'
    id = Column(Integer, Sequence('customer_id_seq', start=1, increment=1), primary_key=True)
    name = Column(String(30), nullable=False)
    email = Column(String(50), UniqueConstraint(name = 'users_email_key') ,nullable=False)
    phone = Column(Integer)
    birthday = Column(Date)
    userRelationShip = relationship("ormProject", back_populates="projectsRelationShip")

class ormProject(db.Model):
    __tablename__ = 'project'
    id = Column(Integer, Sequence('project_id_seq', start=1, increment=1), primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now())
    customer_id = Column(Integer, ForeignKey('customer.id'))
    projectsRelationShip = relationship("ormCustomer", back_populates="userRelationShip")

@app.route('/')
def hello_world():
    text = ""
    return render_template('index.html', action="/")

@app.route('/get', methods=['GET', 'POST'])
def add():
    cust1 = ormCustomer(name="Nick",email="Nick2341@gmail.com",phone=380989236842, birthday = datetime.date(2000, 3, 2))
    cust2 = ormCustomer(name="Bob",email="Bob2341@gmail.com",phone=380989236833, birthday = datetime.date(2001, 6, 2))
    cust3 = ormCustomer(name="Tom",email="Tom2341@gmail.com",phone=380989236845, birthday = datetime.date(2002, 3, 9))
    db.session.add_all([cust1,cust2,cust3])

    db.session.commit()
    return render_template("index.html")

@app.route('/show')
def all_customer():
    name = "customer"
    customer_db = db.session.query(ormCustomer).all()
    customer = []
    for row in customer_db:
        customer.append({"id": row.id, "name": row.name, "email": row.email, "birthday": row.birthday})
    return render_template('allCustomer.html', name=name, customers=customer, action="/show")

@app.route('/insert', methods=['GET', 'POST'])
def create_customer():
    form = CreateCustomer()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('create_customer.html', form=form, form_name="New customer", action="/insert")
        else:

            ids = db.session.query(ormCustomer).all()
            check = True
            for row in ids:
                if row.id == form.id.data:
                    check = False
            new_var = CreateCustomer(

                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                birthday=form.birthday.data,

            )
            if check:
                db.session.add(new_var)
                db.session.commit()
                return redirect(url_for('all_customer'))

    return render_template('create_customer.html', form=form, form_name="New customer", action="/insert")

@app.route('/dashboard')
def dashboard():
    query = (
        db.session.query(
            func.count(ormProject.id),
            ormProject.customer_id
        ).group_by(ormProject.customer_id)
    ).all()


    dates, counts = zip(*query)
    bar = go.Bar(
        x=counts,
        y=dates
    )


    print(dates, counts)

    data = {
        "bar": [bar],
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)

if __name__ == '__main__':
    app.run()
