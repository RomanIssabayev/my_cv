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

tab_2_layout = [
    html.H1('EXPERIANCE', style={'textAlign': 'center', "color": "gold"}),
dbc.Row([
        html.P('2020 Aug - Present', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['ExxonMobil Global Business Center Hungary Kft.', html.Br(), 'Stewardship Coordinator, Hungary - Budapest', html.Br(),
                '-Preparing Monthly and Quartely KPI reports', html.Br(),
                '-Automating daily routine processes', html.Br(),
                '-Providing Expertise in Excel and Automation', html.Br(),
                '-Organizing and Participating in Management Meetings', html.Br(),
                '-Developing End User Tools'
                ],
               style={'color': 'white'})
    ]),
dbc.Row([
        html.P('2019 Nov - 2020 Aug', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['ExxonMobil Global Business Center Hungary Kft.', html.Br(), 'MTO Business Analyst, Hungary - Budapest', html.Br(),
                '-Costs Allocation', html.Br(),
                '-Performance Analysis'
                ],
               style={'color': 'white'})
    ]),
dbc.Row([
        html.P('2019 Sep - 2020 Nov', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['ExxonMobil Global Business Center Hungary Kft.', html.Br(), 'Voyage Analyst, Hungary - Budapest', html.Br(),
                '-Costs Controll', html.Br(),
                '-Accruals Preparation'
                ],
               style={'color': 'white'})
    ]),
dbc.Row([
        html.P('2015 May - 2018 Jan', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['AiRom World Service LLC.', html.Br(), 'Purchaising Specialist, Kazakhstan - Atyrau', html.Br(),
                '-Suppliers Benchmarking', html.Br(),
                '-Goods Control', html.Br(),
                '-Monthly Performance Reports'
                ],
               style={'color': 'white'})
    ]),
dbc.Row([
        html.P('2012 Oct - 2015 Mar', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['Sport Club "Barsy Atyrau"', html.Br(), 'Accounting Assitant, Kazakhstan - Atyrau', html.Br(),
                '-Costs and Price Formation', html.Br(),
                '-Procurement Control'
                ],
               style={'color': 'white'})
    ])
]