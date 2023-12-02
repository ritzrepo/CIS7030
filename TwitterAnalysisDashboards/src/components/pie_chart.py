# import pandas as pd
# import plotly.graph_objs as go
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output

# # Update the import statement based on your project structure
# from ..data.loader import DataSchema
# from . import ids

# def render(app: Dash, data: pd.DataFrame) -> html.Div:
#     @app.callback(
#         Output(ids.PIE_CHART, "children"),
#         [
#             Input(ids.CHANNEL_DROPDOWN, "value")
#         ],
#     )
#     def update_pie_chart(channels: list) -> html.Div:
#         filtered_data = data.query("Channel_name in @channels")

#         if filtered_data.shape[0] == 0:
#             return html.Div("No data selected.", id=ids.PIE_CHART)

#         # Group the data by DataSchema.CHANNEL and get the max VIEW value
#         grouped_data = filtered_data.groupby(DataSchema.CHANNEL)[DataSchema.VIEW].max().reset_index()

#         pie = go.Pie(
#             labels=grouped_data[DataSchema.CHANNEL].tolist(),
#             values=grouped_data[DataSchema.VIEW].tolist(),
#             hole=0.5,
#             title="Latest View count"
#         )

#         fig = go.Figure(data=[pie])
#         fig.update_layout(margin={"t": 40, "b": 0, "l": 0, "r": 0})
#         fig.update_traces(hovertemplate="%{label}<br>%{value:.2f}<extra></extra>")

#         return html.Div([
#             # html.H1("Latest channel Views"),
#             dcc.Graph(figure=fig)
#         ], id=ids.PIE_CHART)

#     return html.Div(id=ids.PIE_CHART)
