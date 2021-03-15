from flask import Flask
from flask import render_template
import pandas
import random


app = Flask(__name__)

def new_movie():
	df = pandas.read_csv("data.csv", sep=",")
	nrows = len(df.index)
	row = random.randint(0, nrows)
	id = df.iloc[row][0]
	return id

def get_title(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	title = df.iloc[0]["primaryTitle"]
	return title

def get_time(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	time = df.iloc[0]["runtimeMinutes"]
	return time

@app.route('/home')
def Welcome():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route("/movie")
def movie():
	m_id = new_movie()
	return render_template('layout.html', m_title = get_title(m_id), m_time = get_time(m_id))

# these two lines of code should always be the last in the file
if __name__ == '__main__':
	app.run(debug=True)