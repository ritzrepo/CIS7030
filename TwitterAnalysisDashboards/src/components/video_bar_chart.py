# import pandas as pd
# import plotly.express as px
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output
# from ..data.loader import VideoDataSchema
# from . import ids

# def render(app: Dash, data: pd.DataFrame ) -> html.Div:
#     @app.callback(
#         Output(ids.VIDEO_BAR_CHART, "children"),
#         Input(ids.CHANNEL_DROPDOWN, "value")
#     )
#     def update_bar_chart(channels: list[str]) -> html.Div:
#         filtered_data = data[data[VideoDataSchema.VDOCHANNELTITLE].isin(channels)]

#         if filtered_data.shape[0] == 0:
#             return html.Div("No data selected.", id=ids.VIDEO_BAR_CHART)

#         def create_pivot_table(data_column: VideoDataSchema, title: str) -> px.bar:
#             pt = filtered_data.pivot_table(
#                 values=[data_column],
#                 index=[VideoDataSchema.VDOCHANNELTITLE],
#                 aggfunc="max",
#                 fill_value=0
#             )
#             pt.reset_index(inplace=True)
#             fig = px.bar(
#                 pt,
#                 x=data_column ,
#                 y=VideoDataSchema.VDOCHANNELTITLE,   
#                 color=VideoDataSchema.VDOCHANNELTITLE,
#                 title=title
#             )
#             return fig

#         fig_comdata = create_pivot_table(VideoDataSchema.VDOCOMMENTS, "Video comments")
#         # fig_likedata = create_pivot_table(VideoDataSchema.VDOLIKES, "Video likes")
#         return html.Div([
#             # html.H1("video Analysis"),
#             dcc.Graph(figure=fig_comdata, className="fig_comdata columns"),
#             # dcc.Graph(figure=fig_view, className="fig_view columns"),
#             # dcc.Graph(figure=fig_likedata, className="fig_likedata columns"),
#         ], id=ids.BAR_CHART
#         # , style={'display': 'flex', 
#         #                             'flex-wrap': 'wrap' ,
#         #                               'height': '600px'}
#                                       )
#     return html.Div(id=ids.VIDEO_BAR_CHART)
