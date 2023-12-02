# import pandas as pd
# from dash import Dash, html
# from src.components import (
#     date_dropdown,
#     channel_dropdown ,
#     month_dropdown,
#     year_dropdown,
#     bar_chart,
#     line_chart,
#     scatter_chart,
#     pie_chart,
    
# )


# def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:

#     return html.Div(
#         className="app-div",
#         children=[
#             html.H1(app.title),
#             html.Hr(),
#             html.Div(
#                 className="dropdown-container",
#                 children=[
#                     channel_dropdown.render(app, data),
#                     # date_dropdown.render(app, data),
#                     # year_dropdown.render(app, data),
#                     # month_dropdown.render(app,data),
                    
#                 ],
#             ),
            
#             bar_chart.render(app, data),
#             html.Hr(),
#             # line_chart.render(app, data),
#             scatter_chart.render(app,data),
#             # pie_chart.render(app, data),

#         ],
#     )
