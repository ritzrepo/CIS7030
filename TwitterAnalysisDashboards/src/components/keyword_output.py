import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.KEYWORD_OUTPUT, "value"),
        Input(ids.KEYWORD_OUTPUT, "value"),
    )
    def select_all_keywords(selected_keywords):
        # Your callback logic here
        # You can access the selected keywords directly using "selected_keywords"
        return selected_keywords

    return html.Div(
        children=[
            html.H6("Keyword"),
            dcc.Input(
                id=ids.KEYWORD_OUTPUT,
                value="Party",  # Initial value for the text input
                type="text",
                placeholder="Enter keywords (comma-separated)",
            ),
        ],
    )
