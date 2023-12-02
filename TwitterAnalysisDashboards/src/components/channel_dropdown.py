# import pandas as pd
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output

# from ..data.loader import DataSchema
# from . import ids

# def render(app: Dash, data: pd.DataFrame) -> html.Div:
#     all_channels: list[str] = data[DataSchema.USERNAME].tolist()
#     unique_channels: list[str] = sorted(set(all_channels))

#     @app.callback(
#         Output(ids.CHANNEL_DROPDOWN, "options"),
#         Output(ids.CHANNEL_DROPDOWN, "value"),  # Add this output to set the values
#         Input(ids.SELECT_ALL_CHANNELS_BUTTON, "n_clicks"),
#     )
#     def select_all_channels(_):
#         return [{"label": channel, "value": channel} for channel in unique_channels], unique_channels

#     return html.Div(
#         children=[
#             html.H6("Channel"),
#             dcc.Dropdown(
#                 id=ids.CHANNEL_DROPDOWN,
#                 options=[],
#                 value=unique_channels,
#                 multi=True,
#                 placeholder="Select",
#             ),
#             html.Button(
#                 className="dropdown-button",
#                 children=["Select All"],
#                 id=ids.SELECT_ALL_CHANNELS_BUTTON,
#                 n_clicks=0,
#             ),
#         ],
#     )
