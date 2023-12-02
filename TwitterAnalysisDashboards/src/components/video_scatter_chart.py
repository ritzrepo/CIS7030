# import pandas as pd
# import plotly.express as px
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output
# from ..data.loader import VideoDataSchema   

# from . import ids

# def render(app: Dash, data: pd.DataFrame) -> html.Div:
#     @app.callback(
#         Output(ids.VIDEO_SCATTER_CHART, "children"),
#         [Input(ids.CHANNEL_DROPDOWN, "value") 
          
#          ]
#     )
#     def update_scatter_chart(channels: list) -> html.Div:
#         # Check if 'channel' exists in data.columns
#         if VideoDataSchema.VDOCHANNELTITLE not in data.columns:
#             return html.Div("No 'channel' column found in the data.", id=ids.VIDEO_SCATTER_CHART)

#         filtered_data = data[data[VideoDataSchema.VDOCHANNELTITLE].isin(channels)]

#         if filtered_data.shape[0] == 0:
#             return html.Div("No data selected.", id=ids.VIDEO_SCATTER_CHART)

#         fig = px.scatter(
#             filtered_data,
#             x=[VideoDataSchema.VDOPUBLISHEDON],
#             y=VideoDataSchema.VDOLIKES,
#             color=VideoDataSchema.VDOCHANNELTITLE ,
#             title="Likes based on published date"
#         )

#         return html.Div([
#             # html.H1("No.of view count based on downloaded date for channels"),
#                          dcc.Graph(figure=fig)], id=ids.VIDEO_SCATTER_CHART
#                         #  , style={'display': 'flex', 
#                         #             'flex-wrap': 'wrap' ,
#                         #               'height': '600px'}
#                                       )

#     return html.Div(id=ids.VIDEO_SCATTER_CHART)