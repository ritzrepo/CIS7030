# import dash
# import pandas as pd
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output

# from ..data.loader import DataSchema
# from . import ids

# def render(app: Dash, data: pd.DataFrame) -> html.Div:
#     all_dates: list[str] = data[DataSchema.DATE].tolist()
#     unique_dates = sorted(set(all_dates))

#     @app.callback(
#         Output(ids.DATE_DROPDOWN, "value"),
#         [
#             Input(ids.DATE_DROPDOWN, "value"),
#             Input(ids.SELECT_ALL_DATES_BUTTON, "n_clicks"),
#             # prevent_initial_call=True
#         ],
#     )
#     def select_all_dates(dates: list[str], _: int) -> list[str]:
#         filtered_data = data.query("down_date in @dates")
#         return sorted(set(filtered_data[DataSchema.DATE].tolist()))
#     # def select_all_dates(n_clicks):
#     #     if n_clicks is None:
#     #         raise dash.exceptions.PreventUpdate

#     #     all_dates = data[DataSchema.DATE].unique().tolist()
#     #     return all_dates
    
#     return html.Div(
#         children=[
#             html.H6("Date"),
#             dcc.Dropdown(
#                 id=ids.DATE_DROPDOWN,
#                 options=[{"label": date, "value": date} for date in unique_dates],
#                 value=unique_dates,  #Set the initial value to an empty list
#                 multi=True,
#             ),
#             html.Button(
#                 className="dropdown-button",
#                 children=["Select All"],
#                 id=ids.SELECT_ALL_DATES_BUTTON,
#                 n_clicks=0,
#             ),
#         ]
#     )
