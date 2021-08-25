import csv
import pandas as pd
import plotly.figure_factory as pff

df = pd.read_csv("data.csv")
figure = pff.create_distplot([df["Weight(Pounds)"].to_list()],["Weight"],show_hist= False)
figure.show()