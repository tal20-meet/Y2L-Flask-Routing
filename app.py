from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
import os
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def home():
	if "user" in login_session:
		return render_template("home.html",login=login_session["user"])
	else:
		login_session["user"]=""
	return render_template("store.html")

@app.route('/store')
def store():
	return render_template("store.html",products=allProducts())

@app.route('/cart')
def cart():
	return render_template("cart.html")


@app.route('/add_to_cart/<int:productID>')
def add_cart(productID):
	#add to cart
	return render_template("store.html")

@app.route('/about')
def about():
	return render_template("about.html")
#this is try number 1
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     user = get_user(request.form['username'])
#     if user != None and user.verify_password(request.form["password"]):
#         login_session['name'] = user.username
#         login_session['logged_in'] = True
#         return logged_in()
#     else:
#         return login()

#this is try number 2(from the internet)
# Route for handling the login page logic
@app.route('/log-in', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':

		#checking if the username that was entered exists in the database
		if None == get_user_by_username(request.form['username']): 
			print('Invalid Username. Please try again.')
			# Show a message/error 

		#checking if the password that was entered exists in the database
		elif None == get_user_by_password(request.form['password']): 
			print('Invalid password. Please try again.')
			#Show a message/error 
			return render_template("log-in.html")

		else: #You logged in
			login_session["user"]=request.form['username']
			return redirect(url_for("home"))

	return render_template("log-in.html")

#this is try number 3
# @app.route('/login', methods=['POST'])
# 	def do_admin_login():
# 		if request.form['password'] == 'password' and request.form['username'] == 'admin':
# 			session['logged_in'] = True
# 		else:
# 			flash('wrong password!')
# 		return home()
@app.route('/portal', methods=['GET', 'POST'])
def portal():
	return render_template("portal.html", products=allProducts())



if __name__ == '__main__':
    app.run(debug=True)