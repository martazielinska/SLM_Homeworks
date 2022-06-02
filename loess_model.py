import pandas as pd
from numpy import median, quantile
import numpy as np
import matplotlib.pylab as plt
from sklego.linear_model import LowessRegression


# lichess_db_puzzle.csv automatically downloaded in the previous homework
puzzles = pd.read_csv("lichess_db_puzzle.csv")
print(puzzles)
plays_lo = median(puzzles["NbPlays"])

rating_lo = 1500
rating_hi = quantile(puzzles["Rating"], 0.99)

row_selector = puzzles.loc[(puzzles['NbPlays'] > plays_lo) & (puzzles['Rating'] > rating_lo) & (puzzles['Rating'] < rating_hi)]
good=row_selector[["Rating", "NbPlays"]]

good=good.groupby(by="Rating").mean()
good=good.reset_index()
print(good)

NbPlays=np.array(good['NbPlays'])
Rating=np.array(good['Rating'])
model = LowessRegression(sigma=1.0, span=0.9).fit(Rating.reshape(-1, 1), NbPlays)

NbPlays_new = model.predict(Rating.reshape(-1, 1))

print(NbPlays_new)
good['NbPlays_new']=NbPlays_new.tolist()
print(good)
plt.scatter(good['Rating'],good['NbPlays'],color= 'green')
plt.plot(good['Rating'],good['NbPlays_new'],color= 'gold')
plt.show()


