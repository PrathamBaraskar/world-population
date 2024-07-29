import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv("E:\data science internship task 1\worldpopulationdata.csv")

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("World Population Data Analysis"),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id="column-dropdown",
                options=[{"label": col, "value": col} for col in df.columns],
                value="2022"
            )
        ], style={"width": "49%", "display": "inline-block"}),
        html.Div([
            dcc.RadioItems(
                id="graph-type",
                options=[{"label": "Bar Graph", "value": "bar"}, {"label": "Line Graph", "value": "line"}],
                value="bar"
            )
        ], style={"width": "49%", "display": "inline-block"})
    ]),
    dcc.Graph(id="graph")
])

# Define the callback function
@app.callback(
    Output("graph", "figure"),
    [Input("column-dropdown", "value"), Input("graph-type", "value")]
)
def update_graph(column, graph_type):
    if graph_type == "bar":
        fig = plt.figure(figsize=(12, 6))
        sns.barplot(x="Country Name", y=column, data=df)
        plt.title(f"Bar Graph of {column}")
        plt.xlabel("Country")
        plt.ylabel("Population")
        return fig
    elif graph_type == "line":
        fig = plt.figure(figsize=(12, 6))
        sns.lineplot(x="Country Name", y=column, data=df)
        plt.title(f"Line Graph of {column}")
        plt.xlabel("Country")
        plt.ylabel("Population")
        return fig

# Run the app
if __name__ == "__main__":
    app.run_server()