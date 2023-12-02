# import pandas as pd
# import plotly.express as px
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output
# from ..data.loader import InstagramDataSchema
# from . import ids

# def render(app: Dash, data: pd.DataFrame) -> html.Div:
#     @app.callback(
#         Output(ids.INSTAGRAM_BAR_CHART, "children"),
#         Input(ids.CHANNEL_DROPDOWN, "value")
#     )
#     def update_bar_chart(channels: list[str]) -> html.Div:
#         filtered_data = data[data[InstagramDataSchema.CHANNEL].isin(channels)]

#         # if 'channel' not in filtered_data.columns:
#         #     return html.Div("No 'channel' column found in the data.", id=ids.INSTAGRAM_BAR_CHART)

#         if filtered_data.shape[0] == 0:
#             return html.Div("No data selected.", id=ids.INSTAGRAM_BAR_CHART)

#         def create_pivot_table() -> pd.DataFrame:
#             pt = filtered_data.pivot_table(
#                 values=[InstagramDataSchema.FOLLOWERSCOUNT],
#                 index=[InstagramDataSchema.CHANNEL],
#                 aggfunc="max",
#                 fill_value=0
#             )
#             return pt.reset_index()
        
#         fig = px.bar(
#             create_pivot_table(),
#             x=InstagramDataSchema.FOLLOWERSCOUNT,
#             y=InstagramDataSchema.CHANNEL,
#             color=InstagramDataSchema.CHANNEL,
#             title="Latest instagram followers count"
#         )
#         fig.update_layout(barmode='stack')  # Set barmode to 'stack' for a stacked bar chart

#         # Return the entire component (html.Div) containing the chart
#         return html.Div([
#             # html.H1("No.of video count for channels"),
#                          dcc.Graph(figure=fig)], id=ids.INSTAGRAM_BAR_CHART)
    
#     return html.Div(id=ids.INSTAGRAM_BAR_CHART)
