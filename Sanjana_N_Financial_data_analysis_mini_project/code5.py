from code_demo import *

ticker = 'PDBC'
start = datetime(2020, 1, 1)
end = datetime.today()

df = get_stock_data(ticker, start, end)

fig = plt.figure(figsize=(12, 8))
top_grid = plt.subplot2grid((4,4),(0,0),rowspan=3,colspan=4)
bottom_grid = plt.subplot2grid((4,4),(3,0),rowspan=1,colspan=4)

top_grid.plot(df.index, df['Close'], label = 'Close')
bottom_grid.plot(df.index, df['Volume'], label = 'Volume')

plt.tight_layout()
plt.legend()
plt.show()