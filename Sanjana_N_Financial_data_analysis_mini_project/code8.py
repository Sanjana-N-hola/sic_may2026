from code_demo import *

stock_daily_pc = (stock-stock.shift(1))/stock.shift(1)*100
df_corr = stock_daily_pc.corr()
plt.imshow(df_corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(df_corr)), df_corr.columns)
plt.yticks(range(len(df_corr)), df_corr.columns)

plt.gcf().set_size_inches(10,10)
plt.show()

plt.scatter(df_corr.SPY, df_corr.VT)
plt.show()