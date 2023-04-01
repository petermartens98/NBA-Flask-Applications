## NBA-Injuries-Flask-Application
This is a Python script that scrapes data from the website "https://www.cbssports.com/nba/injuries/" and displays it on a Flask web application. The script uses Selenium and BeautifulSoup to scrape the data and Pandas to store it in a DataFrame. The web application uses Flask and Jinja2 templates to render the data in an HTML table. The table is also made interactive using DataTables, a JavaScript library for adding advanced features to HTML tables. The script includes caching functionality to reduce the number of requests made to the website. The cached data is refreshed every hour.

![image](https://user-images.githubusercontent.com/87671757/223770326-62d297ea-0777-4302-978c-0baf0497969d.png)

## NBA-Standings-Flask-Application
This project is a web application built with Python's Flask framework to display up-to-date NBA standings. The application imports required modules such as Flask, pandas, and datetime to handle web requests, data processing, and date/time operations.

The application defines a Flask route to serve as the main landing page and implements a function that leverages pandas and web scraping techniques to retrieve NBA standings data from a website. To optimize performance and reduce network traffic, the data is cached using the functools.lru_cache decorator.

Upon a user's request to view the standings, the application retrieves the cached data and passes it to an HTML template through Flask's render_template function. The HTML template is responsible for rendering the standings in a human-readable format. To ensure data accuracy, the application updates the cached data every hour.

Overall, this project showcases how Python and Flask can be used to create a web application that provides real-time NBA standings, highlighting key features such as web scraping, caching, and data visualization.

![image](https://user-images.githubusercontent.com/87671757/229258250-32dc7c00-bf61-47d0-ae75-7ebe737dfaae.png)

