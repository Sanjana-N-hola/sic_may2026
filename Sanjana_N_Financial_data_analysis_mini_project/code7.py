from code_demo import *

stock_daily_pc = (stock-stock.shift(1))/stock.shift(1)*100
stock_d_cr = stock_daily_pc.cumsum()
stock_d_cr.plot(figsize=(20,10))
plt.show()
