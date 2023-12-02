# import pandas as pd
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output

# from ..data.loader import VideoDataSchema
# from . import ids

# def render(app: Dash, data: pd.DataFrame) -> html.Div:
#     all_videos: list[str] = data[VideoDataSchema.VDOID].tolist()
#     unique_videos: list[str] = sorted(set(all_videos))

#     @app.callback(
#         Output(ids.VIDEO_DROPDOWN, "value"),
#         Output(ids.VIDEO_DROPDOWN, "options"),
#         [
#             Input(ids.CHANNEL_DROPDOWN, "value"),
#             Input(ids.SELECT_ALL_VIDEOS_BUTTON, "n_clicks"),
#         ],
#     )
#     def select_all_videos(selected_channels, n_clicks):
#         if not selected_channels:
#             return [], []  # No channels selected, return empty Dropdown

#         filtered_data = data[data[VideoDataSchema.VDOCHANNELTITLE].isin(selected_channels)]
#         dropdown_options = [
#             {"label": title_id, "value": videoid}
#             for title_id, videoid in zip(filtered_data[VideoDataSchema.VDOTITLEID], filtered_data[VideoDataSchema.VDOID])
#         ]
#         return [], dropdown_options

#     return html.Div(
#         children=[
#             html.H6("Video"),
#             dcc.Dropdown(
#                 id=ids.VIDEO_DROPDOWN,
#                 options=[],
#                 value=[],  # This will be updated by the callback
#                 multi=True,
#             ),
             
#             html.Button(
#                 className="dropdown-button",
#                 children=["Select All"],
#                 id=ids.SELECT_ALL_VIDEOS_BUTTON,
#                 n_clicks=0,
#             ),
#         ]
#     )
