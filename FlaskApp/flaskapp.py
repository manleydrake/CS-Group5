from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/home')
def Welcome():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route("/movie/<id>/")
def movie(id):
	return render_template('layout.html', title = id)

# these two lines of code should always be the last in the file
if __name__ == '__main__':
	app.run(debug=True)