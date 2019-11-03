from sqlalchemy import Column, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, Text)
from sqlalchemy.schema import CreateTable
from app import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20))
    password = db.Column(db.String(20))
    email = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    repo_count = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.login)


class Repo(db.Model):
    repo_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String(30))
    deep_link = db.Column(db.String(50))
    related_link = db.Column(db.String(50))
    language = db.Column(db.String(50))

    def __repr__(self):
        return '<Repo {}>'.format(self.name)


class Note(db.Model):
    note_id = db.Column(db.Integer, primary_key=True)
    repo_id = db.Column(db.Integer, db.ForeignKey('repo.repo_id'))
    meta_data = db.Column(db.Text())
    body = db.Column(db.Text())

    def __repr__(self):
        return '<Note {}>'.format(self.note_id)


class Doc(db.Model):
    doc_id = db.Column(db.Integer, primary_key=True)
    repo_id = db.Column(db.Integer, db.ForeignKey('repo.repo_id'))
    path = db.Column(db.String(50))
    format = db.Column(db.String(30))

    def __repr__(self):
        return '<Doc {}>'.format(self.doc_id)

# DeclarativeBase = declarative_base()
#
#
# class Users(DeclarativeBase):
#     __tablename__ = "users"
#
#     user_id = Column('user_id', Integer, primary_key=True)
#     login = Column('login', VARCHAR(20))
#     password = Column('password', VARCHAR(20))
#     email = Column('email', VARCHAR(20))
#     phone = Column('phone', VARCHAR(20))
#     repo_count = Column('repo_count', Integer)
#
#
# class Repo(DeclarativeBase):
#     __tablename__ = "repo"
#
#     repo_id = Column('repo_id', Integer, primary_key=True)
#     user_id = Column('user_id', Integer, ForeignKey('users.user_id'))
#     name = Column('name', VARCHAR(30))
#     deep_link = Column('deep_link', VARCHAR(50))
#     related_link = Column('related_link', VARCHAR(50))
#
#
# class Note(DeclarativeBase):
#     __tablename__ = "note"
#
#     note_id = Column('note_id', Integer, primary_key=True)
#     repo_id = Column('repo_id', Integer, ForeignKey('repo.repo_id'))
#     meta = Column('meta', Text)
#     body = Column('body', Text)
#
#
# class Doc(DeclarativeBase):
#     __tablename__ = "doc"
#
#     doc_id = Column('doc_id', Integer, primary_key=True)
#     repo_id = Column('repo_id', Integer, ForeignKey('repo.repo_id'))
#     path = Column('path', VARCHAR(50))
#     format = Column('format', VARCHAR(30))
#
#
#
# if __name__ == '__main__':
#     print(CreateTable(Users.__table__))
#     print(CreateTable(Repo.__table__))
#     print(CreateTable(Note.__table__))
#     print(CreateTable(Doc.__table__))
