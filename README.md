# web-scraping-challenge

* This repository contains a web application that scrapes several websites for data related to the Mission to Mars and shows the information in a single HTML page. 
* This application was built in three parts:
    1. The application was tested and developed using Jupyter. Scraping was performed using BeautifulSoup, Pandas, and Splinter. This notebook is included in the respository.
    2. The notebook was then converted into a Python script called `scrape_mars.py` with a function called `scrape` that executes all of the scraping code from above and returns one Python dictionary containing all of the scraped data. This infomation is then stored in MongoDB.
    3. Finally, Flask is used to query the Mongo database and pass the mars data into an HTML template to display the data. Bootstrap is used to style the application.
* Screenshots of final application can be found in the folder titled "Final_app screenshots".

