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

data = [['Russian Federation', 'Moscow', 'Skill Factory', '2020 - Present', 'RUS'],
        ['Hungary','Budapest','IBS (International Business School)', '2018 - 2020', 'HUN'],
        ['Malaysia','Kuala Lumpur','ELC (English Language Company)', '2018 - 2018', 'MYS'],
        ['Malta', 'Swieqi', 'Club Class', '2017 - 2017', 'MLT'],
        ['Malaysia','Kuala Lumpur','ELC (English Language Company)', '2016 - 2016', 'MYS'],
        ['Russian Federation', 'Saint-Petersburg', 'Saint-Petersburg University of the Humanities and Social Science', '2011 - 2016', 'RUS']
        ]
df = pd.DataFrame(data, columns = ['country', 'City', 'uni', 'dates', 'iso_alpha'])

fig = px.choropleth(df, locations='iso_alpha',
                    color='City',
                    hover_name='uni',
                    projection='natural earth',
                    title='EDUCATION MAP',
                    color_continuous_scale=px.colors.sequential.Plasma,
                    template='plotly_dark',
                    )
fig.update_layout({
'paper_bgcolor': '#002b36',
'height':600,
})
fig.update_layout(title = dict(font=dict(color="gold")), legend=dict(font=dict(color='gold'),title=dict(font=dict(color="Gold"))))
fig.update_layout(title_x=0.45)
fig.update_layout(font=dict(
            size=16))
fig.update_layout(geo=dict(bgcolor= '#002b36'))


tab_1_layout = [
    html.H1('EDUCATION', style={'textAlign': 'center', "color": "gold"}),
    dbc.Row([
        html.P('2020 Aug - Present', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['Data Scientist', html.Br(), 'Skill Factory, Russian Federation - Moscow (on line)', html.Br(),
                '-Python', html.Br(),
                '-SQL', html.Br(),
                '-Data Visualization'],
               style={'color': 'white'})
    ]),
    dbc.Row([
        html.P('2018 Sep - 2020 Feb', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['MSc in Financial Management', html.Br(), 'IBS (International Business School), Hungary - Budapest',
                html.Br(),
                '-Market Evaluation (FCFF, FCFE, DCF)', html.Br(),
                '-Statistic'],
               style={'color': 'white'}
               )
    ]),
    dbc.Row([
        html.P('2018 Feb - 2018 Jun', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['English Classes', html.Br(), 'ELC (English Language Company), Malaysia - Kuala Lumpur', html.Br(),
                '-Improving English Skills'],
               style={'color': 'white'}
               )
    ]),
    dbc.Row([
        html.P('2017 Jan - 2017 Apr', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['English Classes', html.Br(), 'Club Class, Malta - Swieqi', html.Br(),
                '-Improving English Skills'],
               style={'color': 'white'}
               )
    ]),
    dbc.Row([
        html.P('2016 Aug - 2016 Dec', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['English Classes', html.Br(), 'ELC (English Language Company), Malaysia - Kuala Lumpur', html.Br(),
                '-Improving English Skills'],
               style={'color': 'white'}
               )
    ]),
    dbc.Row([
        html.P('2011 Sep - 2016 May', style={
            'margin-right': '10px',
            'color': 'gold'
        }),
        html.P(['BSc in Economics', html.Br(),
                'Saint-Petersburg University of the Humanities and Social Science, Russian Federation - Saint Petersburg',
                html.Br(),
                '-Economics in Organizations', html.Br(),
                '-Budgeting', html.Br(),
                '-TAX Formation'], style={'color': 'white'})
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='EDU_MAP',
                figure=go.Figure(
                    data=fig
                )
            )
        ], width=12)
    ])
]
