from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

#create instance of Flask app

app = Flask(__name__)

#create connection variable

conn = 'mongodb://localhost:27017'

#Pass connection to the pymongo instance
client = pymongo.MongoClient(conn)

#connect to DB
db = client.mars_scrape_db

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_scrape_db")

#creates a collection in the db and inserts documents

db.mars_headlines.insert_many(
    [
        {
            'news_title': 'Another First: Perseverance Captures the Sounds of Driving on Mars'
            },
        {
            'news_p': 'NASA’s newest rover recorded audio of itself crunching over the surface of the Red Planet, adding a whole new dimension to Mars exploration.'
            },

        {
            'title': 'Cerberus Hemisphere Enhanced',
            'full_img': 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'
            },
        {
            'title': 'Schiaparelli Hemisphere Enhanced',
            'full_img': 'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'
            },
        {
            'title': 'Syrtis Major Hemisphere Enhanced',
            'full_img': 'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'
            },
        {
            'title': 'Valles Marineris Hemisphere Enhanced',
            'full_img': 'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'
            }
    ]
)



# Set route
@app.route('/')
def index():
    #store collection in a list
    mars_headlines = list(db.mars_headlines.find())
    print(mars_headlines)

    #Return the template with headlines list passed
    return render_template('index.html', mars_headlines=mars_headlines)





# @app.route("/")
# def index():
#     listings = mongo.db.listings.find_one()
#     return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    mars_headlines = mongo.db.mars_headlines
    mars_data = scrape_mars.scrape()
    mars_headlines.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
