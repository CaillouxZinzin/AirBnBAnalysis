import matplotlib.pyplot as plt
import io
import base64
import sys
import os
import numpy as np
import pandas as pd
 
def build_graph(x_coordinates, y_coordinates):
    img = io.BytesIO()
    plt.plot(x_coordinates, y_coordinates)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)


def build_hist_paris(price_paris):
    img = io.BytesIO()
    fig, ax = plt.subplots(figsize=(9, 5))
    bins = np.arange(0,300,20)
    xlabels = bins[1:].astype(str)
    xlabels[-1] += '+'
    N_labels = len(xlabels)
    plt.xlim([0, 350])
    plt.xticks(25 * np.arange(N_labels) + 12.5)
    ax.set_xticklabels(xlabels)
    plt.xlabel("Price per night ( $ )")
    plt.hist(price_paris, color='green', bins = bins)
    plt.savefig(img, format='png')
    img.seek(0)
    hist_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(hist_url)