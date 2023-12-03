import pandas as pd
from dash import Dash, html
# from .data.loader import DataSchema,VideoDataSchema
from src.components import (
    date_dropdown,
    channel_dropdown,
    video_dropdown,
    month_dropdown,
    year_dropdown,
    keyword_output,
    bar_chart,
    tweeter_time_chart,
    # instagram_bar_chart,
    line_chart,
    # channel_bar_chart ,
    scatter_chart,
    scatter_chart_like_retweet,
    # pie_chart,
    # # video_bar_chart,
    # video_time_chart,
    # video_scatter_chart,
    # cv_comment_video_time_chart,
    # cv_comment_video_table,
    word_cloud,
    line_chart_keyword ,
    word_cloud_sentiment,
)
# def create_layout(app: Dash, data: pd.DataFrame, videodata: pd.DataFrame, instagramdata : pd.DataFrame,ch_comment_videodata : pd.DataFrame,) -> html.Div:
def create_layout(app: Dash, data: pd.DataFrame ) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    
                    year_dropdown.render(app, data),
                    month_dropdown.render(app, data),
                    keyword_output.render(app,data)
                ],
            ),
            html.Hr(),
            html.H1("Tweeter Data Analysis"),
            html.Hr(),
            html.H3("Keyword Analysis"),
            html.Div(
                className="flex-container",
                children=[
                    html.Div(
                        className="bar-charts-container",
                        children=[
                            line_chart_keyword.render(app,data),
                           
                            

                        ],
                        style={'flex': 1},
                    ),
                ],
                style={'display': 'flex', 'flex-wrap': 'wrap'},
                # , 'width': '100%'
            ),
            html.Hr(),
            html.H3("Simple Frequency Analysis"),
            html.Hr(),
            html.Div(
                className="channelnonflex-container",
                children=[
                    bar_chart.render(app, data ),
                    line_chart.render(app, data ),
                    
            
                    tweeter_time_chart.render(app, data),
                    scatter_chart.render(app, data),
                    scatter_chart_like_retweet.render(app, data),
                    
                   
                ],
            ),
            html.Div(className="spacing-div", style={'height': '20px'}),
            html.Hr(),
            html.H3("Sentiment Analysis"),
            html.Hr(),
            html.Div(
                className="video-flex-container",
                children=[
                     
                    # # pie_chart.render(app, data),
                    word_cloud_sentiment.render(app,data)
                ],
                # style={'display': 'flex', 'flex-wrap': 'wrap'},
                #  'width': '100%'
            ),
            # html.Div(
            #     className="video-channelnonflex-container",
            #     children=[
                   
            #         # 
            #     ],style={'flex': 1},
            # ),
            html.Div(className="spacing-div", style={'height': '20px'}),
            html.Hr(),
            html.H3("Word Cloud"),
 
            html.Hr(),
            html.Div(
                className="videocomments-flex-container",
                children=[
                    html.Div(
                        className="videocomments-bar-charts-container",
                        children=[
                             word_cloud.render(app, data),
                        ],
                        # style={'display': 'flex', 'flex-wrap': 'wrap'},
                    ),
                ],
                style={'display': 'flex', 'flex-wrap': 'wrap'},
                # , 'width': '100%'
            ),
            # html.Div(
            #     className="videocomments-channelnonflex-container",
            #     children=[
                   
            #          
            #     ],
            # ),
        ],
    )
