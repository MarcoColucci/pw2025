import wbgapi as wb
import pandas as pd

gdp = wb.data.DataFrame('FS.AST.DOMO.GD.ZS', 'BRZ')
print(gdp)
# s = wb.search('gdp ')
# print(s)