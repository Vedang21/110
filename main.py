import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean = statistics.mean(data)
fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.show()