import pandas
import random





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

test = new_movie()
print(test)
print(get_title(test))
print(get_time(test))
