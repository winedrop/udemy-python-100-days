import requests
import datetime as dt
import pandas as pd

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_endpoint = "https://www.alphavantage.co/query"
stock_api_key = "6YL9384Q6LX5BO02"




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# alphavantage api setup
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype":"csv",
    "apikey": stock_api_key,
}

sp_function = "TIME_SERIES_DAILY"
sp_symbol = STOCK
sp_outputsize = "compact"
sp_datatype = "csv"
sp_apikey = stock_api_key

stock_url = f"https://www.alphavantage.co/query?function={sp_function}&symbol={sp_symbol}&outputsize={sp_outputsize}&datatype={sp_datatype}&apikey={sp_apikey}"

#----- way of reading in csv without writing to file
import contextlib
import codecs
import csv




#----------------------------------------------------

stock_data_response = requests.get(stock_endpoint, params= stock_params)
# stock_data = stock_data_response.json()["Time Series (Daily)"]#data in "Time Series (Daily)", days stored "yyyy-mm-dd"
stock_data_csv = stock_data_response.content.decode("utf-8")

with open("stock_data.csv", "w") as stock_data_empty:
    stock_data_empty.write(stock_data_csv)
    
stock_data_df = pd.read_csv("stock_data.csv")
print(stock_data_df)

###doesn't work with python 3.X
# with contextlib.closing(requests.get(stock_endpoint, params= stock_params, stream=True)) as r:
#     reader = codecs.iterdecode(csv.reader(r.iter_lines(), "utf-8"),
#     delimiter=",",
#     quotechar='"')
#     for row in reader:
#         print(row)
###should work with python 3.X and 2.X
import os
with open(os.path.split(stock_endpoint)[1]+".csv", "wb")as f, \
        requests.get(stock_url, params=stock_params, stream=True) as r:
    for line in r.iter_lines():
        f.write(line+'\n'.encode())
stock_df = pd.read_csv("query.csv", index_col = "timestamp")
print(stock_df)
stock_df = stock_df.sort_values(by="timestamp", ascending=True)
print(stock_df)

#NOTE dictionary comprehension example NOTE NOTE NOTE NOTE NOTE

stock_row_list = {index:row.close for (index,row) in stock_df.iterrows()}
print(stock_row_list)

# Create a column comparing previous Adj Close with current Adj Close
import numpy as np
stock_df['change'] = np.where(stock_df['close'].shift(1) < stock_df['close'],1,0)
print(stock_df)
stock_df['5% change'] = np.where((np.abs((stock_df['close'].shift(1)-stock_df['close'])
        /((stock_df['close'].shift(1)+stock_df['close'])/2)) >= .05) ,1,0)
print(stock_df)
stock_df = stock_df.sort_values(by="timestamp", ascending=False)
print(stock_df)
if stock_df["5% change"][1]==1:
    print("get news")

#how df.loc[] works, finds rows, can specify range of rows then the column  
chg_list = stock_df.loc[stock_df["5% change"]==1]
print(chg_list)
test_list = stock_df.loc[:,["5% change", "change"]]
print(test_list)



# get today and yesterdays date as strings for stock data
today = dt.datetime.today()
daysbefore_1 = today - dt.timedelta(days = 1)
daysbefore_1_str = daysbefore_1.strftime("%Y-%m-%d")
daysbefore_2 = today - dt.timedelta(days = 2)
daysbefore_2_str = daysbefore_2.strftime("%Y-%m-%d")
# print(type(daysbefore_1))

# # find stock price change between yesterday and day before yesterday
# close_daysbefore_1 = stock_data[daysbefore_1_str]["4. close"]
# close_daysbefore_2 = stock_data[daysbefore_2_str]["4. close"]

# close_price_delta = close_daysbefore_1 - close_daysbefore_2
# #if(c)


##-----

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
##-----news api setup

news_api_key = "ce20b3b3343f49df8ff4e5b4db9f2de6"
news_endpoint = "https://newsapi.org/v2/Everything"

news_api_params = {
    "apiKey":news_api_key,
    "q":STOCK,
    "from":daysbefore_2_str,
    "to":today,
    "pageSize":3,
}

news_api_response = requests.get(news_endpoint, params=news_api_params)
news_api_response.raise_for_status()
print(news_api_response.json())










##-----
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

