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

tab_4_layout = [html.H1('Contacts', style={'textAlign': 'center', "color": "gold"}),
                dbc.Row([
                    html.P('Mobile Phone:', style={
                        'margin-right': '10px',
                        'color': 'gold',
                        'font-size': 20
                    }),
                    html.P('+36 70 619 30 58', style={
                        'margin-right': '10px',
                        'color': 'white',
                        'font-size': 20
                    })
                ]),
                dbc.Row([
                    html.P('WhatsApp:', style={
                        'margin-right': '10px',
                        'color': 'gold',
                        'font-size': 20
                    }),
                    html.P('+7 775 321 24 74', style={
                        'margin-right': '10px',
                        'color': 'white',
                        'font-size': 20
                    })
                ]),
                dbc.Row([
                    html.P('Email Address:', style={
                        'margin-right': '10px',
                        'color': 'gold',
                        'font-size': 20
                    }),
                    html.P('romanissabayev@gmail.com', style={
                        'margin-right': '10px',
                        'color': 'white',
                        'font-size': 20
                    })
                ]),
                dbc.Row([
                    html.P('Location:', style={
                        'margin-right': '10px',
                        'color': 'gold',
                        'font-size': 20
                    }),
                    html.P('Hungary - Budapest', style={
                        'margin-right': '10px',
                        'color': 'white',
                        'font-size': 20
                    })
                ]),
                dbc.Row([
                    html.P('Passport:', style={
                        'margin-right': '10px',
                        'color': 'gold',
                        'font-size': 20
                    }),
                    html.P('Kazakhstan', style={
                        'margin-right': '10px',
                        'color': 'white',
                        'font-size': 20
                    })
                ])
                ]
