import base64
import pandas as pd
import io
import matplotlib
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from ..data.loader import DataSchema   
from . import ids

# Download NLTK resources (you only need to do this once)
nltk.download('vader_lexicon')

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    # Set the backend to Agg
    matplotlib.use('Agg')
    
    # Create a SentimentIntensityAnalyzer instance
    sia = SentimentIntensityAnalyzer()

    @app.callback(
        Output(ids.WORD_CLOUD_SENTIMENT, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value")]
    )
    def update_word_cloud(years, months):
        # Check if 'year' and 'month' exist in data.columns
        if DataSchema.YEAR not in data.columns or DataSchema.MONTH not in data.columns or DataSchema.TEXT not in data.columns:
            return html.Div("Year, Month, or Text not found in the data.", id=ids.WORD_CLOUD_SENTIMENT)

        # Filter the data based on the selected years and months
        filtered_data = data[(data[DataSchema.YEAR].astype(str).isin(map(str, years))) &
                             (data[DataSchema.MONTH].astype(str).isin(map(str, months)))]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.WORD_CLOUD_SENTIMENT)

        # Perform sentiment analysis and categorize into positive, negative, and neutral
        filtered_data['Sentiment'] = filtered_data[DataSchema.TEXT].apply(lambda x: 'Positive' if sia.polarity_scores(x)['compound'] >= 0.05 else ('Negative' if sia.polarity_scores(x)['compound'] <= -0.05 else 'Neutral'))

        # Concatenate tweet texts for each sentiment category
        positive_text = ' '.join(filtered_data[filtered_data['Sentiment'] == 'Positive'][DataSchema.TEXT])
        negative_text = ' '.join(filtered_data[filtered_data['Sentiment'] == 'Negative'][DataSchema.TEXT])
        neutral_text = ' '.join(filtered_data[filtered_data['Sentiment'] == 'Neutral'][DataSchema.TEXT])

        # Generate word clouds for each sentiment category
        positive_wordcloud = WordCloud(width=150, height=200, background_color='white').generate(positive_text)
        negative_wordcloud = WordCloud(width=150, height=200, background_color='white').generate(negative_text)
        neutral_wordcloud = WordCloud(width=150, height=200, background_color='white').generate(neutral_text)

        # Display the word clouds using matplotlib
        plt.figure(figsize=(15, 5))

        plt.subplot(131)
        plt.imshow(positive_wordcloud, interpolation='bilinear')
        plt.title('Positive Sentiment')
        plt.axis('off')

        plt.subplot(132)
        plt.imshow(negative_wordcloud, interpolation='bilinear')
        plt.title('Negative Sentiment')
        plt.axis('off')

        plt.subplot(133)
        plt.imshow(neutral_wordcloud, interpolation='bilinear')
        plt.title('Neutral Sentiment')
        plt.axis('off')

        plt.tight_layout()

        # Save the figure to a BytesIO object
        img_stream = io.BytesIO()
        plt.savefig(img_stream, format='png')
        img_stream.seek(0)
        plt.close()

        # Display the image in Dash
        return html.Div([
            html.Img(src='data:image/png;base64,{}'.format(base64.b64encode(img_stream.read()).decode()), style={'width': '100%'})
        ], id=ids.WORD_CLOUD_SENTIMENT)

    return html.Div(id=ids.WORD_CLOUD_SENTIMENT)
