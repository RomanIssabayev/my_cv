import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import base64
from assets import Education, Experiance, Skills, Contacts
import plotly.graph_objs as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR], suppress_callback_exceptions=True)

lngSkills = go.Figure(
    data=[
        go.Bar(
            x=['Russian', 'English'],
            y=[5, 4],
            text=['Native', 'Advanced'],
            textposition='outside',
            textfont_size=20,
            showlegend=False,
            textfont=dict(
                color="white"
            ))
    ],
    layout=go.Layout(
        legend_orientation='h',
        height=600,
        plot_bgcolor='#002b36',
        paper_bgcolor='#002b36',
        yaxis=dict(showgrid=False, range=[0, 6], tickfont=dict(color='#002b36')),
        xaxis=dict(showgrid=False, tickfont=dict(size=22, color='gold'))
    )
)

sofSkills = go.Figure(
    data=[
        go.Pie(
            labels=['Teamwork', 'Problem-Solving', 'Adaptability', 'Self-Motivation', 'Time Management',
                    ' Responsibility', 'Creativity', 'Communication', 'Fast-Learner'],
            values=[1, 1, 1, 1, 1, 1, 1, 1, 1],
            hole=.9,
            textinfo='label',
            textposition='outside',
            showlegend=False,
            textfont={'color': 'gold', 'size': 22}
        )],
    layout=go.Layout(
        height=600,
        plot_bgcolor='#002b36',
        paper_bgcolor='#002b36',
        yaxis=dict(tickfont=dict(size=22, color='gold')),
    ))

tecSkills = go.Figure(
    data=[
        go.Scatterpolar(
            r=[2, 4, 2, 3, 3, 5, 2],
            theta=['HTML', 'Python', 'SAP Scripting', 'VBA', 'Git', 'Microsoft Office', 'CSS'],
            fill='toself',
            line=dict(color='salmon'),
            textfont={'color': 'gold', 'size': 22},
            textposition='top right',
        )
    ],
    layout=go.Layout(xaxis=dict(visible=False),
                     yaxis=dict(visible=False),
                     font=dict(size=22, color='gold'),
                     paper_bgcolor='#002b36',
                     polar=dict(bgcolor='#002b36',
                         radialaxis=dict(
                             visible=True,
                             range=[0, 5],
                             tickvals=[1, 2, 3, 4, 5],
                             ticktext=['Basic - 1', 'Pre-Intermediate - 2', 'Intermediate - 3', 'Upper-Intermediate - 4', 'Advanced - 5'],
                             tickmode='array',
                             tickangle=25,
                             tickfont=dict(
                                 family='Arial',
                                 size=14,
                                 color='gold'
                             )
                         )
                     ),
                     showlegend=False,
                     height=700
                     )
)

dstSkills = go.Figure(
    data=[
        go.Scatterpolar(
            r=[5,2,3,1,3,5,5,3,3,4],
            theta=['Pandas','SQL', 'Research', 'Machine Learning', 'Statistics', 'Excel', 'Data Viz', 'Tableau', 'Numpy', 'Plotly <br>Dash'],
            fill='toself',
            line=dict(color='salmon'),
            textfont={'color': 'gold', 'size': 22},
            textposition='top right',
        )
    ],
layout=go.Layout(xaxis=dict(visible=False),
                     yaxis=dict(visible=False),
                     font=dict(size=22, color='gold'),
                     paper_bgcolor='#002b36',
                     polar=dict(bgcolor='#002b36',
                         radialaxis=dict(
                             visible=True,
                             range=[0, 5],
                             tickvals=[1, 2, 3, 4, 5],
                             ticktext=['Basic - 1', 'Pre-Intermediate - 2', 'Intermediate - 3', 'Upper-Intermediate - 4', 'Advanced - 5'],
                             tickmode='array',
                             tickangle=25,
                             tickfont=dict(
                                 family='Arial',
                                 size=14,
                                 color='gold'
                             )
                         )
                     ),
                     showlegend=False,
                     height=700
                     )
)

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "19rem",
    "padding": "2rem 1rem",
    "background-color": "#35404b",
    "overflow-y": "auto"
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("ROMAN ISSABAYEV", className="display-4", style={'color': 'gold', 'font-weight': 'bold'}),
        html.H3("DATA ANALYST", style={'color': 'white'}),
        html.Hr(style={'background': '#fff'}),
        html.P(
            "About Me", style={"color": "gold"}, className="lead",
        ),
        html.P(
            'Highly self-motivated data analyst with experiance in Python, Excel, VBA commited to pursuing a long term career change in data science and data analytics'
            , style={"color": "white"}),
        html.Hr(style={'background': '#fff'}),
        dbc.Nav(
            [
                dbc.NavLink("Education", href="/", active="exact", style={"color": "gold"}),
                dbc.NavLink("Experiance", href="/Experiance", active="exact", style={"color": "gold"}),
                dbc.NavLink("Skills", href="/Skills", active="exact", style={"color": "gold"}),
dbc.NavLink("Contacts", href="/Contacts", active="exact", style={"color": "gold"})
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="pages"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("pages", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return Education.tab_1_layout
    elif pathname == "/Experiance":
        return Experiance.tab_2_layout
    elif pathname == "/Skills":
        return Skills.tab_3_layout
    elif pathname == "/Contacts":
        return Contacts.tab_4_layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(Output('SKL_GRP', 'figure'),
              [Input('lng', 'n_clicks'),
               Input('lng', 'n_clicks_timestamp'),
               Input('tec', 'n_clicks'),
               Input('tec', 'n_clicks_timestamp'),
               Input('sof', 'n_clicks'),
               Input('sof', 'n_clicks_timestamp'),
               Input('dst', 'n_clicks'),
               Input('dst', 'n_clicks_timestamp')])
def update_skills(button_1_clicks, button_1_timestamp, button_2_clicks, button_2_timestamp, button_3_clicks,
                  button_3_timestamp, button_5_clicks, button_5_timestamp):
    if (button_1_timestamp == button_2_timestamp) and (button_1_timestamp == button_3_timestamp) and (
            button_1_timestamp == button_5_timestamp) and (button_2_timestamp == button_3_timestamp) \
            and (button_2_timestamp == button_5_timestamp) and (button_3_timestamp == button_5_timestamp):
        return lngSkills
    elif (button_1_timestamp > button_2_timestamp) and (button_1_timestamp > button_3_timestamp) and (
            button_1_timestamp > button_5_timestamp):
        return lngSkills
    elif (button_2_timestamp > button_1_timestamp) and (button_2_timestamp > button_3_timestamp) and (
            button_2_timestamp > button_5_timestamp):
        return tecSkills
    elif (button_3_timestamp > button_1_timestamp) and (button_3_timestamp > button_2_timestamp) and (
            button_3_timestamp > button_5_timestamp):
        return sofSkills
    elif (button_5_timestamp > button_1_timestamp) and (button_5_timestamp > button_2_timestamp) and (
            button_5_timestamp > button_3_timestamp):
        return dstSkills


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
