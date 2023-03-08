# NBA-Injuries-Flask-Application
This is a Python script that scrapes data from the website "https://www.cbssports.com/nba/injuries/" and displays it on a Flask web application. The script uses Selenium and BeautifulSoup to scrape the data and Pandas to store it in a DataFrame. The web application uses Flask and Jinja2 templates to render the data in an HTML table. The table is also made interactive using DataTables, a JavaScript library for adding advanced features to HTML tables. The script includes caching functionality to reduce the number of requests made to the website. The cached data is refreshed every hour.

## Example Output

![image](https://user-images.githubusercontent.com/87671757/223770326-62d297ea-0777-4302-978c-0baf0497969d.png)
