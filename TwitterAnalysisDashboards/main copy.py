# from dash import Dash, html, dcc, Input, Output
# from dash_bootstrap_components.themes import BOOTSTRAP
# from src.layout import create_layout
# from src.data.loader import load_channelstats_data, load_channelvideostats_data, load_instagram_stats_data, load_Video_channel_Comment_data
# import pandas as pd

# CHANNEL_FILE = 'channelstats.csv'
# VIDEO_FILE = 'videostats.csv'
# INSTAGRAM_FILE = 'InstragramStats.csv'
# CV_COMMENTVIDEO_FILE = 'video_channel_comment.csv'
# DATA_PATH = './data/'

# CHANNEL_DATA_PATH = f"{DATA_PATH}{CHANNEL_FILE}"
# VIDEO_DATA_PATH = f"{DATA_PATH}{VIDEO_FILE}"
# INSTAGRAM_DATA_PATH = f"{DATA_PATH}{INSTAGRAM_FILE}"
# CV_COMMENTVIDEO_DATA_PATH = f"{DATA_PATH}{CV_COMMENTVIDEO_FILE}"

# def load_data(top_n=None):
#     # Load data and apply top_n filter
#     chstatdata = load_channelstats_data(CHANNEL_DATA_PATH)
#     channelvideodata = load_channelvideostats_data(VIDEO_DATA_PATH)
#     instragramvideodata = load_instagram_stats_data(INSTAGRAM_DATA_PATH)
#     Video_channel_Comment_data = load_Video_channel_Comment_data(CV_COMMENTVIDEO_DATA_PATH, top_n)
#     return chstatdata, channelvideodata, instragramvideodata, Video_channel_Comment_data

# def main() -> None:
#     app = Dash(external_stylesheets=[BOOTSTRAP])

#     # Enabling debug mode
#     app.debug = True

#     app.title = "Dashboard for Socialmedia Analysis-CIS7029-20285863-Q2"

#     # Initial load with top N = 100
#     chstatdata, channelvideodata, instragramvideodata, Video_channel_Comment_data = load_data(100)

#     # Define layout with a dropdown
#     app.layout = html.Div([
#         html.H1("Dashboard for Social Media Analysis"),
#         dcc.Dropdown(
#             id='top-n-dropdown',
#             options=[
#                 {'label': 'Top 100', 'value': 100},
#                 {'label': 'Top 200', 'value': 200},
#                 # Add more options as needed
#             ],
#             value=100  # Default selection
#         ),
#         create_layout(app, chstatdata, channelvideodata, instragramvideodata, Video_channel_Comment_data)
#     ])

#     @app.callback(
#         Output('top-n-dropdown', 'value'),
#         Output('dashboard-content', 'children'),
#         Input('top-n-dropdown', 'value')
#     )
#     def update_data(selected_value):
#         chstatdata, channelvideodata, instragramvideodata, Video_channel_Comment_data = load_data(selected_value)
#         return selected_value, create_layout(app, chstatdata, channelvideodata, instragramvideodata, Video_channel_Comment_data)

#     app.run(debug=True)

# if __name__ == "__main__":
#     main()
