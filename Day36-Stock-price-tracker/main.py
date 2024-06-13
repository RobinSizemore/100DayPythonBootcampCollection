import os
import requests
import datetime as dt

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla, Inc."
ALPHAVANTAGE_API = os.environ.get("ALPHAVANTAGE_API")
ALPHAVANTAGE_URL = "https://alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWSAPI_KEY")
telegram_bot_key = os.environ.get("TG_TOKEN")
my_tg_id = os.environ.get("TG_RECIPIENT")


# Functions for Step 1 - get Stock price from alphavantage and calculate change.
def get_stock_data(symbol):
    av_params = {"apikey": ALPHAVANTAGE_API, "function": "TIME_SERIES_DAILY", "symbol": symbol}
    stock_data = requests.get(url=ALPHAVANTAGE_URL, params=av_params)
    return stock_data.json()["Time Series (Daily)"]


def calculate_price_change(stock_data):
    yesterday = dt.datetime.now() - dt.timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    yesterday_close = float(stock_data[yesterday_str]["4. close"])

    day_before_yesterday = dt.datetime.now() - dt.timedelta(days=2)
    day_before_yesterday_str = day_before_yesterday.strftime('%Y-%m-%d')
    day_before_yesterday_close = float(stock_data[day_before_yesterday_str]["4. close"])

    percent_change = (yesterday_close - day_before_yesterday_close) / day_before_yesterday_close
    return percent_change


# Functions for step 2 - get first 3 news articles for COMPANY_NAME
def get_news(COMPANY_NAME):
    ereyesterday = dt.datetime.now() - dt.timedelta(days=2)
    ereyesterday_str = ereyesterday.strftime('%Y-%m-%d')

    news_params = {"apiKey": NEWS_API_KEY,
                   "q": COMPANY_NAME,
                   "from": ereyesterday_str,
                   "sortBy": "popularity",
                   "pageSize": 5}
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    articles = news_response.json()["articles"]
    return articles


# Functions for Step 3 - send notifications.
def send_telegram_message(message):
    telegram_req_params = {"chat_id": my_tg_id, "text": message}
    method = "sendMessage"
    telegram_url = f"https://api.telegram.org/bot{telegram_bot_key}/{method}"

    tg_response = requests.get(url=telegram_url, params=telegram_req_params)
    return tg_response


# Workflow

daily_series = get_stock_data(STOCK)
change_in_price = calculate_price_change(daily_series)

message = ""
up_down = "🔺"
if change_in_price < 0:
    up_down = "🔻"

if abs(change_in_price) > 0.05:
    message += f"{STOCK}: {up_down}{round(change_in_price * 100, 2)}\n"
    news_articles = get_news(COMPANY_NAME)
    for article in news_articles:
        message += f"<u><b>Headline</b></u>: {article["title"]}\n"
        message += f"<b>Brief</b>: {article["description"]}\n\n"
else:
    print(f"Change in price was only {round(change_in_price * 100, 2)}%")

send_telegram_message(message)
