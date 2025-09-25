import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt

gdp = wb.data.DataFrame('NE.RSB.GNFS.CD', 'USA').transpose()
dfgdp = pd.DataFrame(gdp)
dfgdp['USA'].plot(x='USA', kind ='line', title='GDP (USA)')
plt.show() 
# s = wb.search('gdp ')
# print(s)