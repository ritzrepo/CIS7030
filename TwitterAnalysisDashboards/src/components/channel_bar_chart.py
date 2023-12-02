# import pandas as pd
# import plotly.express as px
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output
# from ..data.loader import DataSchema
# from . import ids

# def render(app: Dash, data: pd.DataFrame ) -> html.Div:
#     @app.callback(
#         Output(ids.CHANNEL_BAR_CHART, "children"),
#         Input(ids.CHANNEL_DROPDOWN, "value")
#     )
#     def update_bar_chart(channels: list[str]) -> html.Div:
#         filtered_data = data[data[DataSchema.CHANNEL].isin(channels)]

#         if filtered_data.shape[0] == 0:
#             return html.Div("No data selected.", id=ids.CHANNEL_BAR_CHART)

#         def create_pivot_table(data_column: DataSchema, title: str) -> px.bar:
#             pt = filtered_data.pivot_table(
#                 values=[data_column],
#                 index=[DataSchema.CHANNEL],
#                 aggfunc="max",
#                 fill_value=0
#             )
#             pt.reset_index(inplace=True)
#             fig = px.bar(
#                 pt,
#                 x=DataSchema.CHANNEL,
#                 y=data_column,   
#                 color=DataSchema.CHANNEL,
#                 title=title
#             )
#             return fig

#         fig_chartdata = create_pivot_table(chartdata_column, "Chart Data Title")

#         return html.Div([
#             # html.H1("Channel Analysis"),
#             dcc.Graph(figure=fig_chartdata, className="fig_chartdata columns"),
#         ], id=ids.CHANNEL_BAR_CHART)

#     return html.Div(id=ids.CHANNEL_BAR_CHART)
