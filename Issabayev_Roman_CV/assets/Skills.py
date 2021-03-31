import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import base64
import main
import plotly.graph_objs as go

tab_3_layout = [
    html.H1('SKILLS', style={'textAlign': 'center', "color": "gold"}),
    html.Div(
        [
            dbc.Button("Languages", id="lng", color="primary", n_clicks=0, n_clicks_timestamp=-1, className="mr-1"),
            dbc.Button("Technical", id="tec", color="primary", n_clicks=0, n_clicks_timestamp=-1, className="mr-1"),
            dbc.Button("Soft", id="sof", color="primary", n_clicks=0, n_clicks_timestamp=-1, className="mr-1"),
            dbc.Button("Data Science", id="dst", color="primary", n_clicks=0, n_clicks_timestamp=-1, className="mr-1")
        ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='SKL_GRP',
                figure={}
            )
        ], width=12)
    ])

]
