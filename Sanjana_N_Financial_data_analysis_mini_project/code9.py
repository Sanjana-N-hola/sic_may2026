from code_demo import *

periods = 75
stock_daily_pc = (stock-stock.shift(1))/stock.shift(1)*100
vol = stock_daily_pc.rolling(window=periods).std()

vol["SPY"].plot()
vol["TLT"].plot()
vol["DBA"].plot()
plt.show()