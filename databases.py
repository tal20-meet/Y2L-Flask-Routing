from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picture_link, description):
    Product1 = Product(name=name, price=price, picture_link=picture_link, description=description)
    session.add(Product1)
    session.commit()

def updateName(id, name):
   Product1 = session.query(Product).filter_by(id=id)
   Product1.name = name
   session.commit()

def updatePrice(id, price):
   Product1 = session.query(Product).filter_by(id=id)
   Product1.price = price
   session.commit()

def updatePicture_Link(id, picture_link):
   Product1 = session.query(Product).filter_by(id=id)
   Product1.picture_link = picture_link
   session.commit()

def updateDescription(id, description):
   Product1 = session.query(Product).filter_by(id=id)
   Product1.description = description
   session.commit()

def deleteProduct(id_number):
	session.query(Product).filter_by(id=id_number).delete()
	session.commit()

def allProducts():
	return session.query(Product).all()

def productID(id):
	return session.query(Product).filter_by(id=id_number)

def Add_To_Cart(productID):
    Product1 = Cart(productID)
    session.add(Product1)
    session.commit()

def add_user(name,secret_word):
    user = User(username=name)
    user.hash_password(secret_word)
    session.add(user)
    session.commit()

def get_user_by_username(username):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(username=username).first()

def get_user_by_password(password):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(password=password).first()





# add_product("Hoshen", 1, "pic1.jpeg", "Hoshen is a cheap boyyyy")
# add_product("Tal", 999, "pic1.jpeg", "A very good product for all")
# add_product("noy", 3, "pic1.jpeg", "avarege product")
# countinue from the error the picture link gives when trying to ad a product
# continue from part 2.3 int he seond comment