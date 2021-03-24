from flask import Flask
from flask import render_template
import pandas
import random


app = Flask(__name__)

def new_movie(prev):
	df = pandas.read_csv("data.csv", sep=",")
	hist = pandas.read_csv("history.csv", sep = ",")
	hist.at[len(hist.index)-1, 'B'] = prev
	if hist.shape[0] == 10:
		return "stop"
	nrows = len(df.index)
	row = random.randint(0, nrows)
	id = df.iloc[row][0]
	new_row = pandas.DataFrame([id], columns=list('A'))
	hist = hist.append(new_row, ignore_index = True)
	hist.to_csv("history.csv", index = False)
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

def get_year(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	year = df.iloc[0]["startYear"]
	return year

@app.route('/home')
def Welcome():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route("/movie")
def movie():
	m_id = new_movie("None")
	if m_id == "stop":
		end = pandas.read_csv("history.csv", sep = ",")
		end.to_csv("end.csv", index = False)
		start = pandas.read_csv("start.csv", sep = ",")
		start.to_csv("history.csv", index = False)
		return render_template('end.html')
	return render_template('layout.html', m_title = get_title(m_id), m_time = get_time(m_id), m_year = get_year(m_id))

@app.route("/yes")
def movieY():
	m_id = new_movie("Yes")
	if m_id == "stop":
		end = pandas.read_csv("history.csv", sep = ",")
		end.to_csv("end.csv", index = False)
		start = pandas.read_csv("start.csv", sep = ",")
		start.to_csv("history.csv", index = False)
		return render_template('end.html')
	return render_template('layout.html', m_title = get_title(m_id), m_time = get_time(m_id), m_year = get_year(m_id))

@app.route("/no")
def movieN():
	m_id = new_movie("No")
	if m_id == "stop":
		end = pandas.read_csv("history.csv", sep = ",")
		end.to_csv("end.csv", index = False)
		start = pandas.read_csv("start.csv", sep = ",")
		start.to_csv("history.csv", index = False)
		return render_template('end.html')
	return render_template('layout.html', m_title = get_title(m_id), m_time = get_time(m_id), m_year = get_year(m_id))

# these two lines of code should always be the last in the file
if __name__ == '__main__':
	app.run(debug=True)