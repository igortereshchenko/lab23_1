from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.meta import DefaultMeta
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms_alchemy import ModelForm, ModelFormField

from app.models import Users, Repo, Doc, Note, Soft


class UsersForm(ModelForm):
    class Meta:
        model = Users


class RepoForm(ModelForm):
    class Meta:
        model = Repo

    user_id = IntegerField()


class DocForm(ModelForm):
    class Meta:
        model = Doc

    repo_id = IntegerField()


class NoteForm(ModelForm):
    class Meta:
        model = Note

    repo_id = IntegerField()


class SoftForm(ModelForm):
    class Meta:
        model = Soft

    def validate_cost(form, field):
        if not (100 > field.data > 0):
            raise ValidationError("Invalid cost")
        form.cost = int(field.data)

    def validate_version(form, field):
        if int(field.data) not in [1,2,3]:
            raise ValidationError("Invalid version")
        form.version = int(field.data)
