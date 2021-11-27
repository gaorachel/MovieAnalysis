import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import dash
from dash import dcc
from dash import html

app = dash.Dash()

# app.layout = html.Div('div')


colours = {'background': '#111111', 'text': '#7FDBFF'}

# app.layout = html.Div(children=[
#             html.H1('Hello Dash!', style={'textAlign': 'center',
#                                           'color': '#7FDBFF'}),
#             html.H2('Small Hello Dash!'),
#             html.H2('H3 Hello Dash!'),
#             html.Div('Dash: Web Dashboard with Python.'),
#
# ])

app.layout = html.Div([html.H1('this is H1')])
if __name__ == '__main__':
    app.run_server()
