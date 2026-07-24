from code_demo import *

ticker = 'PDBC'
start = datetime(2020, 1, 1)
end = datetime.today()

df = get_stock_data(ticker, start, end)
df.drop(['Ticker', 'High', 'Low', 'Open', 'Close'], axis = 1, inplace = True)

x = df.index
y = df['Volume'].squeeze()
plt.figure(figsize=(15,3))
plt.bar(x, y)
plt.show()