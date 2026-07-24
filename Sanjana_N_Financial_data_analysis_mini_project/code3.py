from code_demo import *

covid = stock['2020-2-1':'2020-7-31']
x = covid.index
s_y = covid[['SPY']]
i_y = covid[['IAU']]
t_y = covid[['TLT']]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].plot(x,s_y)
axs[1].plot(x,i_y)
axs[2].plot(x,t_y)
fig.suptitle('Covid 19')
plt.show()

