import pandas as pd
import plotly.figure_factory as pf
import csv
import plotly.express as px

df=pd.read_csv("data.csv")
graph=pf.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"], show_hist = False)
graph.show()