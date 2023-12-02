import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from ..data.loader import DataSchema

from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.LINE_CHART_KEYWORD, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value"),
         Input(ids.KEYWORD_OUTPUT, "value")]
    )
    def update_line_chart_keyword(years, months, keywords):
        # Check if 'year', 'month', and 'text' exist in data.columns
        if DataSchema.YEAR not in data.columns or DataSchema.MONTH not in data.columns or DataSchema.TEXT not in data.columns:
            return html.Div("Year, Month, or Keyword not found in the data.", id=ids.LINE_CHART_KEYWORD)

        # Filter the data based on the selected years and months
        filtered_data = data[(data[DataSchema.YEAR].astype(str).isin(map(str, years))) &
                             (data[DataSchema.MONTH].astype(str).isin(map(str, months)))]

        # Ensure keywords is a list, even if only one keyword is selected
        if not isinstance(keywords, list):
            keywords = [keywords]

        # Filter data based on keywords using a pattern match
        if keywords:
            filtered_data = filtered_data[filtered_data[DataSchema.TEXT].str.contains('|'.join(keywords), case=False, regex=True)]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.LINE_CHART_KEYWORD)

        def create_line_chart_keyword(data_column: str, title: str):
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

        fig_view = create_line_chart_keyword(DataSchema.TWEETID, "Tweet frequency based on keyword")

        return html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(figure=fig_view)
                ], className="fig_view columns"),
            ], className="row")
        ], id=ids.LINE_CHART_KEYWORD)

    return html.Div(id=ids.LINE_CHART_KEYWORD)
