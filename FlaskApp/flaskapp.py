from flask import Flask
from flask import render_template
import pandas
import random
from flask import request


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
	title = df.iloc[0]["original_title"]
	return title

def get_time(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	time = df.iloc[0]["duration"]
	return time

def get_year(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	year = df.iloc[0]["year"]
	return year

def get_desc(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	desc = df.iloc[0]["description"]
	return desc

def get_director(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	director = df.iloc[0]["director"]
	return director

def get_writer(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	writer = df.iloc[0]["writer"]
	return writer

def get_votes(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	votes = df.iloc[0]["avg_vote"]
	return votes

def get_genre(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	genre = df.iloc[0]["genre"]
	return genre

def get_image(id):
	df = pandas.read_csv("data.csv", sep=",")
	df = df[df["tconst"] == id]
	url = df.iloc[0]["imageurls"]
	return url

@app.route('/home')
def Welcome():
	base = pandas.read_csv("base.csv", sep = ",")
	base.to_csv("data.csv", index = False)
	return render_template('home.html')

@app.route('/filter1')
def year_filter():
    return render_template('year.html')

@app.route('/filter1', methods=['POST'])
def year_filter_post():
	text = request.form['text']
	value = text.upper()
	text1 = request.form['text1']
	value1 = text1.upper()
	data = pandas.read_csv("data.csv", sep = ",")
	if value != "":
		data = data[data["year"] >= int(value)]
	if value1 != "":	
		data = data[data["duration"] <= int(value1)]
	data.to_csv("data.csv", index = False)
	return render_template('ready.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route("/movie")
def movie():
	m_id = new_movie("None")
	if m_id == "stop":
		end = pandas.read_csv("history.csv", sep = ",")
		end.to_csv("templates/data.csv", index = False)
		start = pandas.read_csv("start.csv", sep = ",")
		start.to_csv("history.csv", index = False)
		return render_template('end.html')
	return render_template('layout.html', m_title = get_title(m_id), m_time = get_time(m_id), m_year = get_year(m_id), m_desc = get_desc(m_id), m_director = get_director(m_id), m_writer = get_writer(m_id), m_votes = get_votes(m_id), m_genre = get_genre(m_id), m_url = get_image(m_id))

@app.route("/yes")
def movieY():
	m_id = new_movie("Yes")
	if m_id == "stop":
		end = pandas.read_csv("history.csv", sep = ",")
		end.to_csv("templates/data.csv", index = False)
		start = pandas.read_csv("start.csv", sep = ",")
		start.to_csv("history.csv", index = False)
		return render_template('end.html')
	return render_template('layout.html', m_title = get_title(m_id), m_time = get_time(m_id), m_year = get_year(m_id), m_desc = get_desc(m_id), m_director = get_director(m_id), m_writer = get_writer(m_id), m_votes = get_votes(m_id), m_genre = get_genre(m_id), m_url = get_image(m_id))

@app.route("/no")
def movieN():
	m_id = new_movie("No")
	if m_id == "stop":
		end = pandas.read_csv("history.csv", sep = ",")
		end.to_csv("templates/data.csv", index = False)
		start = pandas.read_csv("start.csv", sep = ",")
		start.to_csv("history.csv", index = False)
		return render_template('end.html')
	return render_template('layout.html', m_title = get_title(m_id), m_time = get_time(m_id), m_year = get_year(m_id), m_desc = get_desc(m_id), m_director = get_director(m_id), m_writer = get_writer(m_id), m_votes = get_votes(m_id), m_genre = get_genre(m_id), m_url = get_image(m_id))

@app.route("/restart")
def restart():
	end = pandas.read_csv("history.csv", sep = ",")
	end.to_csv("templates/data.csv", index = False)
	start = pandas.read_csv("start.csv", sep = ",")
	start.to_csv("history.csv", index = False)
	return render_template('home.html')

@app.route("/EndNow")
def EndNow():
	end = pandas.read_csv("history.csv", sep = ",")
	end.to_csv("templates/data.csv", index = False)
	start = pandas.read_csv("start.csv", sep = ",")
	start.to_csv("history.csv", index = False)
	return render_template('end.html')


# these two lines of code should always be the last in the file
if __name__ == '__main__':
	app.run(debug=True)