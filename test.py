import pandas
df = pandas.read_csv("/Users/matth/Desktop/CS-Group5/FlaskApp/templates/data.csv", sep = ",")
print(df)

df = df.iloc[1: , :]
#print(df)

# Still the issue with the last movie not tracking
df = df[df["B"] == "Yes"]
#print(df)

df = df.rename(columns = {'A':'tconst'})
#print(df)

df2 = pandas.read_csv("/Users/matth/Desktop/CS-Group5/FlaskApp/base.csv", sep = ",")
#print(df2)

df = df.merge(df2, on='tconst', how='left')
print(df)


# Figure out what things to columns to actually display
# Then display the final table / df / file?
# Let the user choose one row
# Only display link to the final movie chosen?????