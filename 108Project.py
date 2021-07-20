import csv
import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv("108Project.csv")
fig = ff.create_distplot([df["Sr.No"].tolist()],["Mobile Brand"],show_hist = False)
fig.show()