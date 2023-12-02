from dash import Dash, html 
from dash_bootstrap_components.themes import BOOTSTRAP
from src.layout  import create_layout
from src.data.loader import load_twitter_data 
# import string

TWITTER_FILE ='tweeter_data.csv'
 
DATA_PATH ='./data/'

TWITTER_DATA_PATH=f"{DATA_PATH}{TWITTER_FILE}"
 
def main() -> None:
    twitterdata = load_twitter_data(TWITTER_DATA_PATH)
    
     #the below line disable to test without comment data
    # Video_channel_Comment_data = load_Video_channel_Comment_data(CV_COMMENTVIDEO_DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP] )

    # Enabling debug mode
    app.debug = True

    app.title = "Dashboard for Event Detection -CIS 7030 - Task 4"
    #the below line disable to test without comment data
    # app.layout = create_layout(app,twitterdata,channelvideodata ,instragramvideodata,Video_channel_Comment_data)
    app.layout = create_layout(app,twitterdata  )
    app.run(debug=True)


if __name__ == "__main__":
    main()