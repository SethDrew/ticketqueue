from dash.dependencies import Input, Output, State

from dash import Dash, dash_table, html, dcc
import plotly.express as px
import pandas as pd
import threading
app = Dash(__name__)


camper_table = pd.DataFrame()

camper_table_radio_options = ['No Ticket', 'Has Ticket', 'All']

init = False


def update(people):
    global camper_table
    
    camper_table = pd.DataFrame(people)
    camper_table.ticket = camper_table.ticket.apply(lambda x: "yes" if x else "no")
    global init
    if not init:
        make_layout()
        init = True

def make_layout():

    app.layout = html.Div(children=[
        html.H1(children='Camp Ticket Queue'),

        html.Div(children='''
            Ticket queue administrative dashboard for swing city
        '''),
        
        html.Div([
            html.H1('Camper Table')
        ]),
        dcc.RadioItems(
            camper_table_radio_options,
            'No Ticket',
            id='ticket-status',
            inline=True
        ),
        dash_table.DataTable(
            id='camper-table',
            columns=[{"name": i, "id": i} for i in camper_table.columns if i != 'id'],
            data=camper_table.to_dict(orient="records"),
            editable=False
        ),
        html.Div(id='data-selection'),

        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])



# people should be something that a dataframe is assignable from, like [{}]
@app.callback(
    Output('camper-table', 'data'),
    Input('ticket-status', 'value'),
    Input('interval-component', 'n_intervals'))
def render(selection, n_intervals):
    global camper_table
    df = camper_table

    # print(df)
    if selection == 'No Ticket':
        df = df[df.ticket=='no']
    if selection == 'Has Ticket':
        df = df[df.ticket=='yes']
    if selection == 'All':
        pass

    df = df.sort_values('score', ascending=False)
    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    return df.to_dict(orient="records")


def start(main=False):
    if main:
        app.run_server(debug=True)
    else :
        thread = threading.Thread(target = app.run_server)
        thread.start()
