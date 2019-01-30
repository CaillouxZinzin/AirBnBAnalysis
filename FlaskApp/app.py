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
    return render_template("home.html")

@app.route('/paris')
def graphsParis():

    paris_listings = pd.read_csv(PARIS_PATH+"clean_paris_listing.csv", low_memory=False)
    paris_reviews = pd.read_csv(PARIS_PATH+"year_reviews.csv", low_memory=False)

    paris_listings["price"] = pd.to_numeric(paris_listings["price"])
    mean_price_paris = paris_listings.price.mean()

    price_paris = paris_listings['price']
    hist_paris = build_hist(price_paris)

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
    hist_berlin = build_hist(price_berlin)

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

    #top10

    lot_of_rev = berlin_listings.nlargest(100, "number_of_reviews")
    berlin_top_10 = lot_of_rev.nlargest(10, "review_scores_rating")
    berlin_top_10 = berlin_top_10.loc[:,['id', 'room_type', 'host_id', 'host_since', 'reviews_per_month', 'review_scores_rating', 'price', 'zipcode', 'number_of_reviews']]

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

@app.route('/lyon')
def graphsLyon():

    lyon_listings = pd.read_csv(LYON_PATH + "clean_lyon_listing.csv", low_memory=False)
    lyon_reviews = pd.read_csv(LYON_PATH + "year_reviews.csv", low_memory=False)

    lyon_listings["price"] = pd.to_numeric(lyon_listings["price"])
    mean_price_lyon = lyon_listings.price.mean()

    price_lyon = lyon_listings['price']
    hist_lyon = build_hist(price_lyon)

    total_houses_lyon = len(lyon_listings)

    #type of room

    lyon_room = lyon_listings
    lyon_entire_house = lyon_room.loc[lyon_room['room_type']=="Entire home/apt"]
    lyon_private_room = lyon_room.loc[lyon_room['room_type']=="Private room"]
    lyon_total_private_room = len(lyon_private_room)
    lyon_total_entire_house = len(lyon_entire_house)
    lyon_percentage_entire_house = (lyon_total_entire_house/total_houses_lyon)*100
    lyon_percentage_private_room = (lyon_total_private_room/total_houses_lyon)*100

    reviews_date = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    lyon_reviews_number = [0, 4, 69, 397, 1470, 4968, 13775, 32628, 51774, 66418]
    lyon_reviews_plot = build_graph(reviews_date, lyon_reviews_number)

    #top10

    lot_of_rev = lyon_listings.nlargest(100, "number_of_reviews")
    lyon_top_10 = lot_of_rev.nlargest(10, "review_scores_rating")
    lyon_top_10 = lyon_top_10.loc[:,['id', 'room_type', 'host_id', 'host_since', 'reviews_per_month', 'review_scores_rating', 'price', 'zipcode', 'number_of_reviews']]

    return render_template('lyon.html',
        mean_price_lyon = round(mean_price_lyon, 2),
        hist_lyon=hist_lyon,
        total_houses_lyon= total_houses_lyon,
        lyon_total_private_room= lyon_total_private_room,
        lyon_total_entire_house= lyon_total_entire_house,
        lyon_percentage_entire_house= round(lyon_percentage_entire_house,3),
        lyon_percentage_private_room= round(lyon_percentage_private_room,3),
        lyon_private_room_mean_price= round(lyon_private_room.price.mean(), 2),
        lyon_entire_house_mean_price= round(lyon_entire_house.price.mean(), 2),
        lyon_reviews_plot= lyon_reviews_plot,
        debug= 'debug'
    )

@app.route('/bordeaux')
def graphsBordeaux():

    bdx_listings = pd.read_csv(BDX_PATH + "clean_bdx_listing.csv", low_memory=False)
    bdx_reviews = pd.read_csv(BDX_PATH + "year_reviews.csv", low_memory=False)

    bdx_listings["price"] = pd.to_numeric(bdx_listings["price"])
    mean_price_bdx = bdx_listings.price.mean()

    price_bdx = bdx_listings['price']
    hist_bdx = build_hist(price_bdx)

    total_houses_bdx = len(bdx_listings)

    #type of room

    bdx_room = bdx_listings
    bdx_entire_house = bdx_room.loc[bdx_room['room_type']=="Entire home/apt"]
    bdx_private_room = bdx_room.loc[bdx_room['room_type']=="Private room"]
    bdx_total_private_room = len(bdx_private_room)
    bdx_total_entire_house = len(bdx_entire_house)
    bdx_percentage_entire_house = (bdx_total_entire_house/total_houses_bdx)*100
    bdx_percentage_private_room = (bdx_total_private_room/total_houses_bdx)*100

    reviews_date = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    bdx_reviews_number = [0, 1, 60, 178, 1060, 3890, 13112, 32394, 55376, 75189]
    bdx_reviews_plot = build_graph(reviews_date, bdx_reviews_number)

    #top10

    lot_of_rev = bdx_listings.nlargest(100, "number_of_reviews")
    bdx_top_10 = lot_of_rev.nlargest(10, "review_scores_rating")
    bdx_top_10 = bdx_top_10.loc[:,['id', 'room_type', 'host_id', 'host_since', 'reviews_per_month', 'review_scores_rating', 'price', 'zipcode', 'number_of_reviews']]

    return render_template('bordeaux.html',
        mean_price_bdx = round(mean_price_bdx, 2),
        hist_bdx=hist_bdx,
        total_houses_bdx= total_houses_bdx,
        bdx_total_private_room= bdx_total_private_room,
        bdx_total_entire_house= bdx_total_entire_house,
        bdx_percentage_entire_house= round(bdx_percentage_entire_house,3),
        bdx_percentage_private_room= round(bdx_percentage_private_room,3),
        bdx_private_room_mean_price= round(bdx_private_room.price.mean(), 2),
        bdx_entire_house_mean_price= round(bdx_entire_house.price.mean(), 2),
        bdx_reviews_plot= bdx_reviews_plot,
        debug= 'debug'
    )

@app.route('/compare')
def compare():
    bdx_listings = pd.read_csv(BDX_PATH+"clean_bdx_listing.csv", low_memory=False)
    lyon_listings = pd.read_csv(LYON_PATH+"clean_lyon_listing.csv", low_memory=False)
    paris_listings = pd.read_csv(PARIS_PATH+"clean_paris_listing.csv", low_memory=False)
    berlin_listings = pd.read_csv(BRL_PATH+"clean_listing.csv", low_memory=False)

    #bdx_listings.price = [x.strip('$') for x in bdx_listings.price]
    #bdx_listings.price = bdx_listings.price.apply(lambda x: x.replace(',',''))
    bdx_listings["price"] = pd.to_numeric(bdx_listings["price"])

    #lyon_listings.price = [x.strip('$') for x in lyon_listings.price]
    #lyon_listings.price = lyon_listings.price.apply(lambda x: x.replace(',',''))
    lyon_listings["price"] = pd.to_numeric(lyon_listings["price"])

    #paris_listings.price = [x.strip('$') for x in paris_listings.price]
    #paris_listings.price = paris_listings.price.apply(lambda x: x.replace(',',''))
    paris_listings["price"] = pd.to_numeric(paris_listings["price"])

    berlin_listings["price"] = pd.to_numeric(berlin_listings["price"])

    paris_bdx_lyon_compare_hist = build_hist_compare_3(paris_listings["price"], lyon_listings["price"], bdx_listings["price"], "Paris", "Lyon", "Bordeaux")
    bdx_lyon_compare_hist = build_hist_compare_2(lyon_listings["price"], bdx_listings["price"], "Lyon", "Bordeaux")
    paris_berlin_compare_hist = build_hist_compare_2(paris_listings["price"], berlin_listings["price"], "Paris", "Berlin")


    return render_template('compare.html',
    paris_bdx_lyon_compare_hist= paris_bdx_lyon_compare_hist,
    bdx_lyon_compare_hist= bdx_lyon_compare_hist,
    paris_berlin_compare_hist=paris_berlin_compare_hist
    )

if __name__ == '__main__':
    app.run(debug=True)
