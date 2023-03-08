from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, render_template
from functools import lru_cache
from datetime import datetime, timedelta

def scrape_daily_injuries():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--window-size=1920,1080")
    url = "https://www.cbssports.com/nba/injuries/"
    chrome_driver = "chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(options=opts, service=Service(chrome_driver))
    driver.set_page_load_timeout(20)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    team_injuries = soup.select('div.TableBaseWrapper')
    team_data = [{'Team': team.select_one('div.TeamLogoNameLockup-name').text,
                  'Name': player.select_one('span.CellPlayerName--long').text,
                  'POS': player.select('td.TableBase-bodyTd')[1].get_text(strip=True),
                  'Updated': player.select_one('span.CellGameDate').get_text(strip=True),
                  'Injury': player.select('td.TableBase-bodyTd')[3].get_text(strip=True),
                  'Status': player.select('td.TableBase-bodyTd')[4].get_text(strip=True)}
                 for team in team_injuries
                 for player in team.select('tr.TableBase-bodyTr')]
    driver.quit()
    df = pd.DataFrame(team_data).sort_values('Team')
    return df


app = Flask(__name__)

@lru_cache(maxsize=1)
def cached_injuries():
    return scrape_daily_injuries()

@app.route('/')
def index():
    global last_cached_time
    if not hasattr(cached_injuries, 'cached_time') or datetime.now() - cached_injuries.cached_time > timedelta(hours=1):
        injuries = scrape_daily_injuries()
        cached_injuries.cached_time = datetime.now()
        cached_injuries.data = injuries
    else:
        injuries = cached_injuries.data
    return render_template('index.html', injuries=injuries)

if __name__ == "__main__":
    cached_injuries.cached_time = datetime.min
    cached_injuries.data = None
    app.run(debug=True)