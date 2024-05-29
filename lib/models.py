from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

class Movie(Base):
    pass

class Genre(Base):
    pass

class Actor(Base):
    pass

class MovieGenre(Base):
    pass

class Cast(Base):
    pass

class User(Base):
    pass

class Fave(Base):
    pass