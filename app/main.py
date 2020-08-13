from app import app
from flask import Flask, render_template, request, redirect, url_for


#defining the various routes for the pages

@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/services')
def services():
	return render_template('services.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/thanks')
def thanks():
	return render_template('thanks.html')


@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		msg = Message ('CUSTOMER\'S REQUEST',
			sender = request.form["email"],
			recipients = ['thecheftee00@gmail.com'])
		name = request.form["user_name"]
		email = request.form["email"]
		subject = request.form["subject"]
		message = request.form["message"]
		msg.body = "Customer Name: %s \nCustomer Mail: %s \nMail Subject: %s \nCustomer's Request: %s" %(name,email,subject,message)
		mail.send(msg)
		return redirect('/thanks')
	else:
		return 'Try again'

if __name__ == '__main__':
	app.run()





