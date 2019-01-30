import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from bokeh.charts import Histogram
from bokeh.embed import components

DIR_PATH =  os.getcwd()
DATA_PATH = os.path.join(DIR_PATH + os.sep, "data")
FRANCE_PATH = os.path.join(DATA_PATH + os.sep, "France")
LYON_PATH = os.path.join(FRANCE_PATH + os.sep, "Lyon" + os.sep)
PARIS_PATH = os.path.join(FRANCE_PATH + os.sep, "Paris" + os.sep)
BDX_PATH = os.path.join(FRANCE_PATH + os.sep, "Bordeaux" + os.sep)


def build_graph(x_coordinates, y_coordinates):
    img = io.BytesIO()
    plt.plot(x_coordinates, y_coordinates)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)


def hist_paris_price(current_feature_name, bins):
    paris_listings = pd.read_csv(PARIS_PATH+"clean_paris_listings.csv", low_memory=False)
    p = Histogram(paris_listings, current_feature_name, title=current_feature_name, color='Species', bins=bins, legend='top_right', width=600, height=400)
    p.xaxis.axis_label = current_feature_name
    p.yaxis.axis_label = 'Count'
    return p
