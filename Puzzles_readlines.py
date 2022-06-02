import pandas as pd
import requests
import bz2
import wget
import pandas as pd
import csv

url= "https://database.lichess.org/lichess_db_puzzle.csv.bz2"
#file = wget.download(url)
df=pd.read_csv("lichess_db_puzzle.csv.bz2", header=None)
df.columns=['PuzzleId','FEN','Moves','Rating','RatingDeviation','Popularity','NbPlays','Themes','GameUrl']
print(df)

df.to_csv("lichess_db_puzzle.csv")

#rint(data.column)
# assuming the filepath ends with .bz2
f = open("lichess_db_puzzle.csv", "r")
print(f.readlines())