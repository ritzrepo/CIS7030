import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from ..data.loader import DataSchema   

from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.LINE_CHART, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value")]
    )
    def update_bar_chart(years, months):
        # Check if 'year' and 'month' exist in data.columns
        if DataSchema.YEAR not in data.columns or DataSchema.MONTH not in data.columns:
            return html.Div("Year or Month not found in the data.", id=ids.LINE_CHART)

        # Filter the data based on the selected years and months
        filtered_data = data[(data[DataSchema.YEAR].astype(str).isin(map(str, years))) &
                             (data[DataSchema.MONTH].astype(str).isin(map(str, months)))]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.LINE_CHART)

        def create_line_chart(data_column: str, title: str):
            pt = filtered_data.pivot_table(
                values=[data_column],
                index=[DataSchema.DATE],
                aggfunc="count",  # Use count for tweet count
                fill_value=0
            )
            pt.reset_index(inplace=True)
            fig = px.line(
                pt,
                x=DataSchema.DATE,
                y=data_column,
                title=title
            )
            return fig

        fig_view = create_line_chart(DataSchema.TWEETID, "Daily tweet Count")

        return html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(figure=fig_view)
                ], className="fig_view columns"),
            ], className="row")
        ], id=ids.LINE_CHART)

    return html.Div(id=ids.LINE_CHART)
