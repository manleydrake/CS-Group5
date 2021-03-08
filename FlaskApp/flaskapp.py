from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Hello from Flask!</h1>'

@app.route('/about')
def about ():
	return '<h2>Ab about page!</h2>'

@app.route("/hello/<id>/")
def hello_user(id):
	return render_template('layout.html', title = id)

# these two lines of code should always be the last in the file
if __name__ == '__main__':
	app.run(debug=True)