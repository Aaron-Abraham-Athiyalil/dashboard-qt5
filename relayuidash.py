import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Sample data for visualization
df = pd.DataFrame({
    "Relay": ["Relay 1", "Relay 2", "Relay 3", "Relay 4", "Relay 5", "Relay 6", "Relay 7", "Relay 8"],
    "State": [1, 0, 1, 1, 0, 0, 1, 0]
})

# Dash layout with Tesla-inspired styling
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARK])  # Use DARK theme for Tesla vibe

app.layout = html.Div(
    children=[
        # Centered header with prominent font size and Tesla-like font family
        dbc.Row(
            dbc.Col(
                html.H1("Relay Control Dashboard", style={'text-align': 'center', 'font-size': '36px'}),
                width=12
            )
        ),
        # Card component with rounded corners and dark background for chart
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            "Relay Status",
                            style={
                                'background-color': '#212529',  # Darker header for Tesla feel
                                'color': 'white',
                                'border-radius': '0.5rem'  # Rounded corners for card header
                            }
                        ),
                        dbc.CardBody(
                            dcc.Graph(
                                id='relay-status',
                                figure=px.bar(
                                    df, x="Relay", y="State", title="Relay Status",
                                    color_discrete_sequence=['#3f7eb9', '#ff4500']  # Green for ON, red for OFF
                                )
                            ),
                            style={'background-color': '#212529', 'border-radius': '0.5rem'}  # Dark background, rounded corners
                        )
                    ]
                ),
                width=12
            )
        ),
        # Row for additional controls (example)
        dbc.Row(
            [
                # Button with custom styles for Tesla-like look
                dbc.Col(
                    dbc.Button(
                        "Activate Relay 1",
                        id='activate-button',
                        n_clicks=0,
                        style={
                            'background-color': '#3f7eb9',  # Light blue for action
                            'color': 'white',
                            'border-color': '#3f7eb9',
                            'border-radius': '0.5rem',
                            'margin-top': '20px',
                            'margin-bottom': '10px'
                        }
                    ),
                    width=3
                ),
                dbc.Col(width=6),  # Spacer
                # Another custom button with Tesla-like styling
                dbc.Col(
                    dbc.Button(
                        "Deactivate Relay 2",
                        id='deactivate-button',
                        n_clicks=0,
                        style={
                            'background-color': '#ff4500',  # Light red for stopping action
                            'color': 'white',
                            'border-color': '#ff4500',
                            'border-radius': '0.5rem',
                            'margin-top': '20px',
                            'margin-bottom': '10px'
                        }
                    ),
                    width=3
                )
            ]
        )
    ]
)

# Interactive callbacks to update data or trigger actions (example)
@app.callback(
    Output('relay-status', 'figure'),
    [Input('activate-button', 'n_clicks'), Input('deactivate-button', 'n_clicks')]
)
def update_relay_status(activate_clicks, deactivate_clicks):
    if activate_clicks > 0:
        # Update data for relay activation here (example)
        df.loc[df['Relay'] == 'Relay 1', 'State'] = 1
    elif deactivate_clicks > 0:
        # Update data for relay deactivation here (example)
        df.loc[df['Relay'] == 'Relay 1', 'State'] = 0
