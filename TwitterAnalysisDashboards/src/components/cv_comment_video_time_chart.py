# import pandas as pd
# import plotly.express as px
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output
# from ..data.loader import Video_channel_CommentDataSchema   

# from . import ids

# def render(app: Dash, data: pd.DataFrame) -> html.Div:
#     @app.callback(
#         Output(ids.CH_COMMENT_VIDEO_TIME_CHART, "children"),
#         [Input(ids.CHANNEL_DROPDOWN, "value")]
#     )
#     def update_scatter_chart(channels: list) -> html.Div:
#         # Check if 'channel' exists in data.columns
#         if Video_channel_CommentDataSchema.CHANNELTITLE not in data.columns:
#             return html.Div("No 'channel' column found in the data.", id=ids.CH_COMMENT_VIDEO_TIME_CHART)

#         filtered_data = data[data[Video_channel_CommentDataSchema.CHANNELTITLE].isin(channels)]

#         if filtered_data.shape[0] == 0:
#             return html.Div("No data selected.", id=ids.CH_COMMENT_VIDEO_TIME_CHART)

#         fig = px.line(
#             filtered_data,
#             x=[Video_channel_CommentDataSchema.PUBLISHEDDATE],
#             y=Video_channel_CommentDataSchema.COMMENT,
#             color=Video_channel_CommentDataSchema.CHANNELTITLE,
#             title="Video Comments based on published date"
#         )

#         return html.Div([
#             # html.H1("No.of view count based on downloaded date for channels"),
#                          dcc.Graph(figure=fig)], id=ids.CH_COMMENT_VIDEO_TIME_CHART
#                         #  , style={'display': 'flex', 
#                         #             'flex-wrap': 'wrap' ,
#                         #               'height': '600px'}
#                                       )

#     return html.Div(id=ids.CH_COMMENT_VIDEO_TIME_CHART)