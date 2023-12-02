import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from ..data.loader import DataSchema   

from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.SCATTER_CHART, "children"),
         [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value")]
    )
    def update_scatter_chart(years, months): #(channels: list) -> html.Div:
        # Check if 'year' and 'month' exist in data.columns
        if DataSchema.YEAR not in data.columns or DataSchema.MONTH not in data.columns:
            return html.Div("Year or Month not found in the data.", id=ids.SCATTER_CHART)

        # Filter the data based on the selected years and months
        filtered_data = data[(data[DataSchema.YEAR].astype(str).isin(map(str, years))) &
                             (data[DataSchema.MONTH].astype(str).isin(map(str, months)))]

        # Check if 'channel' exists in data.columns
        # if DataSchema.YEAR not in data.columns:
        #     return html.Div("Year not found in the data.", id=ids.SCATTER_CHART)

        # filtered_data = data[data[DataSchema.YEAR].isin(channels)]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.SCATTER_CHART)

        fig = px.scatter(
            filtered_data,
            x=DataSchema.USERNAME,
            y=DataSchema.LIKES,
            color=DataSchema.USERNAME ,
            title="Scatter chart: Likes count based on username"
        )

        return html.Div([
            # html.H1("No.of view count based on downloaded date for channels"),
                         dcc.Graph(figure=fig)], id=ids.SCATTER_CHART
                        #  , style={'display': 'flex', 
                        #             'flex-wrap': 'wrap' ,
                        #               'height': '600px'}
                                      )

    return html.Div(id=ids.SCATTER_CHART)