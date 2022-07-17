#!/usr/bin/python

import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

company = str(input("Company?:  "))
period = int(input("How many days?: "))
symbol = str(yf.Ticker(company))

if int(period) > 50 and isinstance(company, str) == True and isinstance(period, int) == True:
    data = yf.download(tickers=company, period=(str(period)+'d'), interval='5d')
    pd.set_option('display.max_rows', 20)
    df = pd.DataFrame(data)

    old = data.reset_index()

    for i in ['Open', 'High', 'Low', 'Close']: 
        old[i] = old[i].astype('float64')
        fig = go.Figure(data=[go.Candlestick(x=old['Date'],
            open=old['Open'],
            high=old['High'],
            low=old['Low'],
            close=old['Close'])])

    fig.show()
    print("-" + "\n" + symbol + "\n" + "-")
    print(df)

elif int(period) <=50 and int(period) > 10 and isinstance(company, str) == True and isinstance(period, int) == True:
    data = yf.download(tickers=company, period=(str(period)+'d'), interval='1d')
    pd.set_option('display.max_rows', 20)
    df = pd.DataFrame(data)

    old = data.reset_index()

    for i in ['Open', 'High', 'Low', 'Close']: 
        old[i] = old[i].astype('float64')
        fig = go.Figure(data=[go.Candlestick(x=old['Date'],
            open=old['Open'],
            high=old['High'],
            low=old['Low'],
            close=old['Close'])])

    fig.show()
    print("-" + "\n" + symbol + "\n" + "-")
    print(df)

elif int(period) <= 10 and int(period) > 0 and isinstance(company, str) == True and isinstance(period, int) == True:
    data = yf.download(tickers=company, period=(str(period)+'d'), interval='1d')
    pd.set_option('display.max_rows', 20)
    df = pd.DataFrame(data)

    old = data.reset_index()

    for i in ['Open', 'High', 'Low', 'Close']: 
        old[i] = old[i].astype('float64')
        fig = go.Figure(data=[go.Candlestick(x=old['Date'],
                open=old['Open'],
                high=old['High'],
                low=old['Low'],
                close=old['Close'])])
    fig.show()
    print("-" + "\n" + symbol + "\n" + "-")
    print(df)

elif int(period) <= 0 and isinstance(company, str) == True and isinstance(period, int) == True:   
    print("No or negative days....yeah that makes sense....")

else:
    print("Try again :D")
