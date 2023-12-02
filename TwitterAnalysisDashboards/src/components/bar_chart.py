import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from ..data.loader import DataSchema
from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value")]
    )
    def update_bar_chart(years, months):
        # Check if 'year' and 'month' exist in data.columns
        if DataSchema.YEAR not in data.columns or DataSchema.MONTH not in data.columns:
            return html.Div("Year or Month not found in the data.", id=ids.BAR_CHART)

        # Filter the data based on the selected years and months
        filtered_data = data[(data[DataSchema.YEAR].astype(str).isin(map(str, years))) &
                             (data[DataSchema.MONTH].astype(str).isin(map(str, months)))]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        def create_pivot_table(data_column: str, title: str):
            pt = filtered_data.pivot_table(
                values=[data_column],
                index=[DataSchema.MONTH],
                aggfunc="sum",
                fill_value=0
            )
            pt.reset_index(inplace=True)
            fig = px.bar(
                pt,
                x=DataSchema.MONTH,
                y=data_column,
                color=DataSchema.MONTH,
                title=title
            )
            return fig

        fig_video = create_pivot_table(DataSchema.LIKES, "Likes Count")
        fig_sub = create_pivot_table(DataSchema.RETWEETS, "Retweets Count")

        return html.Div([
            dcc.Graph(figure=fig_video, className="fig_video columns"),
            dcc.Graph(figure=fig_sub, className="fig_sub columns"),
        ], id=ids.BAR_CHART, style={'display': 'flex', 'flex-wrap': 'wrap', 'height': '600px'})

    return html.Div(id=ids.BAR_CHART)
