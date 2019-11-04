from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms.ProductsForm import ProductsForm
from forms.StoreForm import StoreForm
from forms.ProductsFormEdit import ProductsFormEdit
from forms.RecommendationForm import RecommendationForm
from forms.CharacteristicForm import CharacteristicForm
from forms.StoreFormEdit import StoreFormEdit
from forms.RecommendationFormEdit import RecommendationFormEdit
from forms.CharacteristicFormEdit import CharacteristicFormEdit
from forms.VendorFormEdit import VendorFormEdit
from forms.VendorForm import VendorForm

from sqlalchemy.sql import func
import plotly
import plotly.graph_objs as go

import json


app = Flask(__name__)
app.secret_key = 'key'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:blackjack21@localhost/Vadim_Pits'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jfemlpyycmlqhd:871690116729b2c919f4850284d01db6dfd973fec5f3305d4423255ee79e7ad3@ec2-174-129-253-162.compute-1.amazonaws.com:5432/d3icu3uc1h1tpn'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Products (db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20))
    product_model = db.Column(db.String(20))

    products_store_fk = db.relationship("Store", secondary="products_store")
    products_characteristic_fk = db.relationship("Characteristic", secondary="characteristic_products")
    recommendation_id = db.Column(db.Integer, db.ForeignKey('recommendation.recommendation_id'))
    vendor_name = db.Column(db.String, db.ForeignKey('vendor.vendor_name'))


class Store(db.Model):
    __tablename__ = 'store'
    store_name = db.Column(db.String(20), primary_key=True)

    store_fk = db.relationship("Products", secondary="products_store")


class Products_Store(db.Model):
    __tablename__ = 'products_store'
    left_name = db.Column(db.Integer, db.ForeignKey('products.product_id'), primary_key=True)
    right_name = db.Column(db.String(20), db.ForeignKey('store.store_name'), primary_key=True)


class Recommendation(db.Model):
    __tablename__ = 'recommendation'
    recommendation_id = db.Column(db.Integer, primary_key=True)
    recommendation_price = db.Column(db.Float)
    recommendation_name = db.Column(db.String(20))
    recommendation_model = db.Column(db.String(20))

    recommendation_products = db.relationship("Products")


class Characteristic(db.Model):
    __tablename__ = 'characteristic'
    characteristic_id = db.Column(db.Integer, primary_key=True)
    characteristic_specification = db.Column(db.String(40))
    characteristic_price = db.Column(db.Float)

    characteristic_fk = db.relationship("Products", secondary="characteristic_products")


class Characteristic_Products(db.Model):
    __tablename__ = 'characteristic_products'
    left_name = db.Column(db.Integer, db.ForeignKey('characteristic.characteristic_id'), primary_key=True)
    right_name = db.Column(db.Integer, db.ForeignKey('products.product_id'), primary_key=True)


class Vendor(db.Model):
    __tablename__ = 'vendor'
    vendor_name = db.Column(db.String, primary_key=True)
    vendor_balance = db.Column(db.Float)
    vendor_country = db.Column(db.String(20))
    vendor_city = db.Column(db.String(20))

    vendor_products = db.relationship("Products")

# создание всех таблиц
db.create_all()

# # очистрка всех таблиц

# db.session.query(Characteristic_Products).delete()
# db.session.query(Products_Store).delete()
# db.session.query(Characteristic).delete()
# db.session.query(Products).delete()
# db.session.query(Recommendation).delete()
# db.session.query(Store).delete()
# db.session.query(Vendor).delete()


# # # создане объектов
'''
Lexus = Products(product_id=1,
                 product_name='Lexus',
                 product_model='LX350'
                 )

BMW = Products(product_id=2,
               product_name='BMW',
               product_model='X5'
               )

Audi = Products(product_id=3,
                product_name='Audi',
                product_model='A8'
                )

ZAZ = Products(product_id=4,
               product_name='ZAZ',
               product_model='Vida'
               )

Mazda = Products(product_id=5,
                 product_name='Mazda',
                 product_model='Model 6'
                 )

R_Lexus = Recommendation(recommendation_id=1,
                         recommendation_price=30000,
                         recommendation_name='Lexus',
                         recommendation_model='LX350')

R_BMW = Recommendation(recommendation_id=2,
                       recommendation_price=20000,
                       recommendation_name='BMW',
                       recommendation_model='X5'
                       )

R_Audi = Recommendation(recommendation_id=3,
                        recommendation_price=40000,
                        recommendation_name='Audi',
                        recommendation_model='A8'
                        )

R_ZAZ = Recommendation(recommendation_id=4,
                       recommendation_price=4000,
                       recommendation_name='ZAZ',
                       recommendation_model='Vida'
                       )

R_Mazda = Recommendation(recommendation_id=5,
                         recommendation_price=10000,
                         recommendation_name='Mazda',
                         recommendation_model='Model 6'
                         )

Char_1 = Characteristic(characteristic_id=1,
                        characteristic_specification='White',
                        characteristic_price=30000
                        )

Char_2 = Characteristic(characteristic_id=2,
                        characteristic_specification='Black',
                        characteristic_price=20000
                        )

Char_3 = Characteristic(characteristic_id=3,
                        characteristic_specification='Gold',
                        characteristic_price=40000
                        )

Char_4 = Characteristic(characteristic_id=4,
                        characteristic_specification='Pink',
                        characteristic_price=4000
                        )

Char_5 = Characteristic(characteristic_id=5,
                        characteristic_specification='Grey',
                        characteristic_price=10000
                        )

St_name_1 = Store(store_name='Ukraine')

St_name_2 = Store(store_name='USA')

St_name_3 = Store(store_name='Germany')

St_name_4 = Store(store_name='Russia')

St_name_5 = Store(store_name='Japan')

Ven_1 = Vendor(vendor_name='Ivan',
                         vendor_balance=10000,
                         vendor_country='Ukraine',
                         vendor_city='Odessa'
                         )

Ven_2 = Vendor(vendor_name='Bob',
                         vendor_balance=10000,
                         vendor_country='Ukraine',
                         vendor_city='Kyiv'
                         )

R_Lexus.recommendation_products.append(Lexus)
R_BMW.recommendation_products.append(BMW)
R_Audi.recommendation_products.append(Audi)
R_ZAZ.recommendation_products.append(ZAZ)
R_Mazda.recommendation_products.append(Mazda)

Lexus.products_store_fk.append(St_name_1)
BMW.products_store_fk.append(St_name_2)
Audi.products_store_fk.append(St_name_3)
ZAZ.products_store_fk.append(St_name_4)
Mazda.products_store_fk.append(St_name_5)

Lexus.products_characteristic_fk.append(Char_1)
BMW.products_characteristic_fk.append(Char_2)
Audi.products_characteristic_fk.append(Char_3)
ZAZ.products_characteristic_fk.append(Char_4)
Mazda.products_characteristic_fk.append(Char_5)

Ven_1.vendor_products.append(Lexus)
Ven_2.vendor_products.append(BMW)

db.session.add_all([Lexus, BMW, Audi, ZAZ, Mazda,
                    R_Lexus, R_BMW, R_Audi, R_ZAZ, R_Mazda,
                    Char_1, Char_2, Char_3, Char_4, Char_5,
                    St_name_1, St_name_2, St_name_3, St_name_4, St_name_5,
                    Ven_1, Ven_2
                    ])

db.session.commit()

'''
@app.route('/', methods=['GET', 'POST'])
def root():

    return render_template('index.html')


@app.route('/products', methods=['GET'])
def all_products():
    result = db.session.query(Products).all()

    return render_template('all_products.html', result=result)


@app.route('/store', methods=['GET'])
def all_store():
    result = db.session.query(Store).all()

    return render_template('all_store.html', result=result)


@app.route('/recommendation', methods=['GET'])
def all_recommendation():
    result = db.session.query(Recommendation).all()

    return render_template('all_recommendation.html', result=result)


@app.route('/characteristic', methods=['GET'])
def all_characteristic():
    result = db.session.query(Characteristic).all()

    return render_template('all_characteristic.html', result=result)


@app.route('/vendor', methods=['GET'])
def all_vendor():
    result = db.session.query(Vendor).all()

    return render_template('all_vendor.html', result=result)


@app.route('/create_product', methods=['POST', 'GET'])
def create_product():
    form = ProductsForm()

    if request.method == 'POST':
        new_product = Products(
            product_id=form.product_id.data,
            product_name=form.product_name.data,
            product_model=form.product_model.data,
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect('/products')
    elif request.method == 'GET':
        return render_template('create_product.html', form=form)


@app.route('/delete_product/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    result = db.session.query(Products).filter(Products.product_id == id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/products')


@app.route('/create_store', methods=['POST', 'GET'])
def create_store():
    form = StoreForm()

    if request.method == 'POST':
        new_store = Store(
            store_name=form.store_name.data,
        )
        db.session.add(new_store)
        db.session.commit()
        return redirect('/store')
    elif request.method == 'GET':
        return render_template('create_store.html', form=form)


@app.route('/delete_store/<string:name>', methods=['GET', 'POST'])
def delete_store(name):
    result = db.session.query(Store).filter(Store.store_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/store')


@app.route('/create_recommendation', methods=['POST', 'GET'])
def create_recommendation():
    form = RecommendationForm()

    if request.method == 'POST':
        new_recommendation = Recommendation(
            recommendation_id=form.recommendation_id.data,
            recommendation_name=form.recommendation_name.data,
            recommendation_model=form.recommendation_model.data,
            recommendation_price=form.recommendation_price.data,
        )
        db.session.add(new_recommendation)
        db.session.commit()
        return redirect('/recommendation')
    elif request.method == 'GET':
        return render_template('create_recommendation.html', form=form)


@app.route('/delete_recommendation/<string:r_id>', methods=['GET', 'POST'])
def delete_recommendation(r_id):
    result = db.session.query(Recommendation).filter(Recommendation.recommendation_id == int(r_id)).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/recommendation')


@app.route('/create_characteristic', methods=['POST', 'GET'])
def create_characteristic():
    form = CharacteristicForm()

    if request.method == 'POST':
        new_characteristic = Characteristic(
            characteristic_id=form.characteristic_id.data,
            characteristic_price=form.characteristic_price.data,
            characteristic_specification=form.characteristic_specification.data,
        )
        db.session.add(new_characteristic)
        db.session.commit()
        return redirect('/characteristic')
    elif request.method == 'GET':
        return render_template('create_characteristic.html', form=form)


@app.route('/delete_characteristic/<int:c_id>', methods=['GET', 'POST'])
def delete_characteristic(c_id):
    result = db.session.query(Characteristic).filter(Characteristic.characteristic_id == c_id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/characteristic')


@app.route('/create_vendor', methods=['POST', 'GET'])
def create_vendor():
    form = VendorForm()

    if request.method == 'POST':
        new_vendor = Vendor(
            vendor_name=form.vendor_name.data,
            vendor_balance=form.vendor_balance.data,
            vendor_country=form.vendor_country.data,
            vendor_city=form.vendor_city.data,
        )
        db.session.add(new_vendor)
        db.session.commit()
        return redirect('/vendor')
    elif request.method == 'GET':
        return render_template('create_vendor.html', form=form)


@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    form = ProductsFormEdit()
    result = db.session.query(Products).filter(Products.product_id == id).one()

    if request.method == 'GET':

        form.product_id.data = result.product_id
        form.product_name.data = result.product_name
        form.product_model.data = result.product_model


        return render_template('edit_product.html', form=form, form_name=id)
    elif request.method == 'POST':

        result.product_id = form.product_id.data
        result.product_name = form.product_name.data
        result.product_model = form.product_model.data,

        db.session.commit()
        return redirect('/products')


@app.route('/edit_store/<string:name>', methods=['GET', 'POST'])
def edit_store(name):
    form = StoreFormEdit()
    result = db.session.query(Store).filter(Store.store_name == name).one()

    if request.method == 'GET':

        form.store_name.data = result.store_name


        return render_template('edit_store.html', form=form, form_name=name)
    elif request.method == 'POST':

        result.store_name = form.store_name.data

        db.session.commit()
        return redirect('/store')


@app.route('/edit_recommendation/<int:r_id>', methods=['GET', 'POST'])
def edit_recommendation(r_id):
    form = RecommendationFormEdit()
    result = db.session.query(Recommendation).filter(Recommendation.recommendation_id == r_id).one()

    if request.method == 'GET':

        form.recommendation_id.data = result.recommendation_id
        form.recommendation_price.data = result.recommendation_price
        form.recommendation_name.data = result.recommendation_name
        form.recommendation_model.data = result.recommendation_model

        return render_template('edit_recommendation.html', form=form, form_name='Edit Recommendation')
    elif request.method == 'POST':

        result.recommendation_id = form.recommendation_id.data
        result.recommendation_price = form.recommendation_price.data
        result.recommendation_name = form.recommendation_name.data
        result.recommendation_model = form.recommendation_model.data
        db.session.commit()
        return redirect('/recommendation')


@app.route('/edit_characteristic/<int:c_id>', methods=['GET', 'POST'])
def edit_characteristic(c_id):
    form = CharacteristicFormEdit()
    result = db.session.query(Characteristic).filter(Characteristic.characteristic_id == c_id).one()

    if request.method == 'GET':

        form.characteristic_id.data = result.characteristic_id
        form.characteristic_specification.data = result.characteristic_specification
        form.characteristic_price.data = result.characteristic_price

        return render_template('edit_characteristic.html', form=form, form_name='Edit Characteristic')
    elif request.method == 'POST':

        result.characteristic_id = form.characteristic_id.data
        result.characteristic_specification = form.characteristic_specification.data
        result.characteristic_price = form.characteristic_price.data,

        db.session.commit()
        return redirect('/characteristic')


@app.route('/edit_vendor/<string:v_name>', methods=['GET', 'POST'])
def edit_vendor(v_name):
    form = VendorFormEdit()
    result = db.session.query(Vendor).filter(Vendor.vendor_name == v_name).one()

    if request.method == 'GET':

        form.vendor_name.data = result.vendor_name
        form.vendor_balance.data = result.vendor_balance
        form.vendor_country.data = result.vendor_country
        form.vendor_city.data = result.vendor_city

        return render_template('edit_vendor.html', form=form, form_name='Edit Vendor')
    elif request.method == 'POST':

        result.vendor_name = form.vendor_name.data
        result.vendor_balance = form.vendor_balance.data
        result.vendor_country = form.vendor_country.data
        result.vendor_city = form.vendor_city.data
        db.session.commit()
        return redirect('/vendor')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    query1 = (
        db.session.query(
            Products.product_name,
            func.count(Recommendation.recommendation_id).label('recommendation_id')
        ).join(Recommendation, Products.recommendation_id == Recommendation.recommendation_id).
            group_by(Products.product_name)
    ).all()

    print(query1)

    query2 = (
        db.session.query(
            Products.product_name,
            func.count(Vendor.vendor_balance).label('vendor_balance')
        ).join(Vendor, Products.vendor_name == Vendor.vendor_name).
            group_by(Products.product_name)
    ).all()

    print(query2)

    product_name, recommendation_id = zip(*query1)
    bar = go.Bar(
        x=product_name,
        y=recommendation_id
    )

    product_name, vendor_balance = zip(*query2)
    pie = go.Pie(
        labels=product_name,
        values=vendor_balance
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphs_json)


if __name__ == "__main__":
    app.run()