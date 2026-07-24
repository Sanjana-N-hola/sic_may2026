import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date, datetime, time, timezone

def get_stock_data(ticker, start, end):
    data = yf.download(tickers = [ticker], start = start, end = end)
    data.insert(0, 'Ticker', ticker)
    return data

start = datetime(2020, 1, 1)
end = datetime.today()

SPY = get_stock_data("SPY", start, end)
IYW = get_stock_data("IYW", start, end)
VT = get_stock_data("VT", start, end)
DBA = get_stock_data("DBA", start, end)
TLT = get_stock_data("TLT", start, end)
PDBC = get_stock_data("PDBC", start, end)
IAU = get_stock_data("IAU", start, end)

SPY.columns = SPY.columns.get_level_values(0)
SPY = SPY.reset_index().pivot(index = 'Date', columns = 'Ticker', values = 'Close')
IYW.columns = IYW.columns.get_level_values(0)
IYW = IYW.reset_index().pivot(index = 'Date', columns = 'Ticker', values = 'Close')
VT.columns = VT.columns.get_level_values(0)
VT = VT.reset_index().pivot(index = 'Date', columns = 'Ticker', values = 'Close')
DBA.columns = DBA.columns.get_level_values(0)
DBA = DBA.reset_index().pivot(index = 'Date', columns = 'Ticker', values = 'Close')
TLT.columns = TLT.columns.get_level_values(0)
TLT = TLT.reset_index().pivot(index = 'Date', columns = 'Ticker', values = 'Close')
PDBC.columns = PDBC.columns.get_level_values(0)
PDBC = PDBC.reset_index().pivot(index = 'Date', columns = 'Ticker', values = 'Close')
IAU.columns = IAU.columns.get_level_values(0)
IAU = IAU.reset_index().pivot(index = 'Date', columns = 'Ticker', values = 'Close')

stock = pd.concat(objs=[SPY, IYW, VT, DBA, TLT, PDBC, IAU], axis = 1, join = 'outer')



