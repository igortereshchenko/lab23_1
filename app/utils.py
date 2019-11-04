from sqlalchemy import create_engine

from app.forms import UsersForm, DocForm, NoteForm, RepoForm
from app.models import Users, Repo, Doc, Note

DB_STRING = "postgres://postgres@localhost:5432/postgres"


key_to_model = {
    "users": Users,
    "repo": Repo,
    "doc": Doc,
    "note": Note
}

key_to_form = {
    "users": UsersForm,
    "repo": RepoForm,
    "doc": DocForm,
    "note": NoteForm
}


def get_form_from_key(key):
    return key_to_form[key]


def get_model_from_key(key):
    return key_to_model[key]


def update_extra(extra):
    extra["models"] = key_to_model.keys()


def db_connect():
    return create_engine(DB_STRING)

