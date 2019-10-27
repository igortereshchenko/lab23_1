from flask import render_template, request, url_for
from werkzeug.utils import redirect

from app import app, db

from app.forms import UsersForm
from app.models import Users
from app.utils import update_extra, get_model_from_key, key_to_form, get_form_from_key

app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def main():
    extra = {}
    update_extra(extra)
    return render_template('index.html', **extra)


@app.route('/get/<model>', methods=['GET'])
def get(model):
    instance = get_model_from_key(model).query.first()
    form_cls = get_form_from_key(model)
    form = form_cls(**{"obj": instance} if instance else {})
    is_exist = bool(instance)
    extra = {
        "form": form,
        "submit_value": "Update" if is_exist else "Create",
        "is_exist": is_exist,
        "model_name": instance.__class__.__name__.lower() if instance else model,
    }

    update_extra(extra)
    return render_template('index.html', **extra)


@app.route('/edit/<model>', methods=['POST'])
def edit(model):
    instance = get_model_from_key(model).query.first()
    form_cls = get_form_from_key(model)
    form = form_cls(request.form, obj=instance)
    if form.validate():
        form.populate_obj(instance)
        db.session.add(instance)
        db.session.commit()
        return redirect(url_for('get', model=model))


@app.route('/create/<model>', methods=['POST'])
def create(model):
    instance = get_model_from_key(model)()
    form_cls = get_form_from_key(model)
    form = form_cls(request.form, obj=instance)
    if form.validate():
        form.populate_obj(instance)
        db.session.add(instance)
        db.session.commit()
        return redirect(url_for('get', model=model))


@app.route('/delete/<model>', methods=['GET'])
def delete(model):
    instance = get_model_from_key(model).query.first()
    db.session.delete(instance)
    db.session.commit()
    return redirect(url_for('get', model=model))