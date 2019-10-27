from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.meta import DefaultMeta
from wtforms.validators import DataRequired, Email
from wtforms_alchemy import ModelForm, ModelFormField

from app.models import Users, Repo, Doc, Note


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
