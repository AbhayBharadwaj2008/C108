import pandas as pd
import plotly_express as px
import csv
import plotly.figure_factory as pff

df = pd.read_csv("data.csv")
figure = pff.create_distplot([df["Height(Inches)"].to_list()],["Height"],show_hist= False)
figure.show()
