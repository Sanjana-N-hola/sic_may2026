from code_demo import *

spy_daily_pc = (stock['SPY']/stock['SPY'].shift(1)-1)*100
spy_daily_pc.plot()
plt.show()
spy_daily_pc.iloc[0] = 0

plt.hist(spy_daily_pc, bins= 50)
plt.show()