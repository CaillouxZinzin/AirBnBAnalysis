from flask import Flask, render_template
from graph import *
import sys
import os
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

DIR_PATH =  os.getcwd()
DATA_PATH = os.path.join(DIR_PATH + os.sep, "data")
FRANCE_PATH = os.path.join(DATA_PATH + os.sep, "France")
LYON_PATH = os.path.join(FRANCE_PATH + os.sep, "Lyon" + os.sep)
PARIS_PATH = os.path.join(FRANCE_PATH + os.sep, "Paris" + os.sep)
BDX_PATH = os.path.join(FRANCE_PATH + os.sep, "Bordeaux" + os.sep)
WRLD_PATH = os.path.join(DATA_PATH + os.sep, "World")
BRL_PATH = os.path.join(WRLD_PATH + os.sep, "Berlin" + os.sep)

@app.route('/')
def hello():
    return "Hello"

@app.route('/paris')
def graphsParis():

    paris_listings = pd.read_csv(PARIS_PATH+"clean_paris_listing.csv", low_memory=False)
    paris_reviews = pd.read_csv(PARIS_PATH+"year_reviews.csv", low_memory=False)

    paris_listings["price"] = pd.to_numeric(paris_listings["price"])
    mean_price_paris = paris_listings.price.mean()

    price_paris = paris_listings['price']
    hist_paris = build_hist_paris(price_paris)

    total_houses_paris = len(paris_listings)

    #type of room

    paris_room = paris_listings
    paris_entire_house = paris_room.loc[paris_room['room_type'] == "Entire home/apt"]
    paris_private_room = paris_room.loc[paris_room['room_type'] == "Private room"]
    paris_total_private_room = len(paris_private_room)
    paris_total_entire_house = len(paris_entire_house)
    paris_percentage_entire_house = (paris_total_entire_house/total_houses_paris)*100
    paris_percentage_private_room = (paris_total_private_room/total_houses_paris)*100

    reviews_date = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    paris_reviews_number = [10, 508, 2217, 7617, 21317, 53060, 118278, 185578, 293940, 420842]
    paris_reviews_plot = build_graph(reviews_date, paris_reviews_number)

    return render_template('paris.html',
        mean_price_paris= round(mean_price_paris,2),
        hist_paris=hist_paris,
        total_houses_paris= total_houses_paris,
        paris_total_private_room= paris_total_private_room,
        paris_total_entire_house= paris_total_entire_house,
        paris_percentage_entire_house= round(paris_percentage_entire_house,3),
        paris_percentage_private_room= round(paris_percentage_private_room,3),
        paris_private_room_mean_price= round(paris_private_room.price.mean(), 2),
        paris_entire_house_mean_price= round(paris_entire_house.price.mean(), 2),
        paris_reviews_plot= paris_reviews_plot,
        debug= 'debug'
    )

@app.route('/berlin')
def graphsBerlin():

    berlin_listings = pd.read_csv(BRL_PATH + "clean_listing.csv", low_memory=False)
    berlin_reviews = pd.read_csv(BRL_PATH + "year_review.csv", low_memory=False)

    berlin_listings["price"] = pd.to_numeric(berlin_listings["price"])
    mean_price_berlin = berlin_listings.price.mean()

    price_berlin = berlin_listings['price']
    hist_berlin = build_hist_paris(price_berlin)

    total_houses_berlin = len(berlin_listings)

    #type of room

    berlin_room = berlin_listings
    berlin_entire_house = berlin_room.loc[berlin_room['room_type']=="Entire home/apt"]
    berlin_private_room = berlin_room.loc[berlin_room['room_type']=="Private room"]
    berlin_total_private_room = len(berlin_private_room)
    berlin_total_entire_house = len(berlin_entire_house)
    berlin_percentage_entire_house = (berlin_total_entire_house/total_houses_berlin)*100
    berlin_percentage_private_room = (berlin_total_private_room/total_houses_berlin)*100

    reviews_date = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    berlin_reviews_number = [3, 107, 617, 3092, 7422, 17702, 39470, 69303, 111180, 152450]
    berlin_reviews_plot = build_graph(reviews_date, berlin_reviews_number)

    return render_template('berlin.html',
        mean_price_berlin = round(mean_price_berlin, 2),
        hist_berlin=hist_berlin,
        total_houses_berlin= total_houses_berlin,
        berlin_total_private_room= berlin_total_private_room,
        berlin_total_entire_house= berlin_total_entire_house,
        berlin_percentage_entire_house= round(berlin_percentage_entire_house,3),
        berlin_percentage_private_room= round(berlin_percentage_private_room,3),
        berlin_private_room_mean_price= round(berlin_private_room.price.mean(), 2),
        berlin_entire_house_mean_price= round(berlin_entire_house.price.mean(), 2),
        berlin_reviews_plot= berlin_reviews_plot,
        debug= 'debug'
    )

@app.route('/compare')
def compare():
    bdx_listings = pd.read_csv(BDX_PATH+"clean_bdx_listing.csv", low_memory=False)
    lyon_listings = pd.read_csv(LYON_PATH+"clean_lyon_listing.csv", low_memory=False)
    paris_listings = pd.read_csv(PARIS_PATH+"clean_paris_listing.csv", low_memory=False)

    #bdx_listings.price = [x.strip('$') for x in bdx_listings.price]
    #bdx_listings.price = bdx_listings.price.apply(lambda x: x.replace(',',''))
    bdx_listings["price"] = pd.to_numeric(bdx_listings["price"])

    #lyon_listings.price = [x.strip('$') for x in lyon_listings.price]
    #lyon_listings.price = lyon_listings.price.apply(lambda x: x.replace(',',''))
    lyon_listings["price"] = pd.to_numeric(lyon_listings["price"])

    #paris_listings.price = [x.strip('$') for x in paris_listings.price]
    #paris_listings.price = paris_listings.price.apply(lambda x: x.replace(',',''))
    paris_listings["price"] = pd.to_numeric(paris_listings["price"])

    paris_bdx_lyon_compare_hist = build_hist_compare_3(paris_listings["price"], lyon_listings["price"], bdx_listings["price"])
    bdx_lyon_compare_hist = build_hist_compare_2(lyon_listings["price"], bdx_listings["price"])


    return render_template('compare.html',
    paris_bdx_lyon_compare_hist= paris_bdx_lyon_compare_hist,
    bdx_lyon_compare_hist= bdx_lyon_compare_hist)

if __name__ == '__main__':
    app.run(debug=True)
