import pandas as pd
import plotly.express as px


df = pd.read_csv("project107.csv")
figure = px.scatter(df, x = "level", y = "student_id", color = "level", size = "attempt", size_max = 50)
figure.show()

