#!/usr/bin/python3

from flask import Flask 
from flask import request #allows specification of HTTP requests other than GET
from flask import url_for
from flask import render_template
from flask import send_from_directory 
from flask import send_file

base = '/home/krocodial/web-development/flask'

app = Flask(__name__)
#app.static_folder =  '/home/krocodial/web-development/flask/static/'


def show_the_login_form():
	#print(url_for('static', filename='index.html')
	app.send_static_file(url_for('static', filename='index.html'))


@app.route('/')
def hello_world():
	#app.send_static_file('/static/index.html'
	return send_file(base + url_for('static', filename='index.html'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		#return url_for('static', filename='index.html')
		return send_file(base + url_for('static', filename='login.html'))
		show_the_login_form()
