from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
   __tablename__ = 'products'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Integer)
   picture_link = Column(String)
   description = Column(String)

class Cart(Base):
   __tablename__ = 'Cart'
   id = Column(Integer, primary_key=True)
   productID = Column(Integer)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    password_hash = Column(String)
    username = Column(String)