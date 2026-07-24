from code_demo import *

covid = stock['2020-2-1':'2020-7-31']
plt.style.use('ggplot')
covid.plot(figsize = (20,10))
plt.show()
