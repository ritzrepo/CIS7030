import base64
import pandas as pd
import io
import matplotlib
 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from ..data.loader import DataSchema   
from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
     # Set the backend to Agg
    matplotlib.use('Agg')
    @app.callback(
        Output(ids.WORD_CLOUD, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value")]
    )
    def update_word_cloud(years, months):
        # Check if 'year' and 'month' exist in data.columns
        if DataSchema.YEAR not in data.columns or DataSchema.MONTH not in data.columns or DataSchema.TEXT not in data.columns:
            return html.Div("Year, Month, or Text not found in the data.", id=ids.WORD_CLOUD)

        # Filter the data based on the selected years and months
        filtered_data = data[(data[DataSchema.YEAR].astype(str).isin(map(str, years))) &
                             (data[DataSchema.MONTH].astype(str).isin(map(str, months)))]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.WORD_CLOUD)

        # Concatenate tweet texts into a single string
        all_text = ' '.join(filtered_data[DataSchema.TEXT])

        # Generate word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

        # Display the word cloud using matplotlib
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')  # Turn off axis labels
        plt.tight_layout()

        # Save the figure to a BytesIO object
        img_stream = io.BytesIO()
        plt.savefig(img_stream, format='png')
        img_stream.seek(0)
        plt.close()

        # Display the image in Dash
        return html.Div([
            html.Img(src='data:image/png;base64,{}'.format(base64.b64encode(img_stream.read()).decode()), style={'width': '100%'})
        ], id=ids.WORD_CLOUD)

    return html.Div(id=ids.WORD_CLOUD)
