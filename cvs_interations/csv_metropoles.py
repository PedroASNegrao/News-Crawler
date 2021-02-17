
import pandas as pd

metropoles_string = pd.read_csv('./../Data/news_metropoles.csv')

#print(metropoles_string)

metropoles_string.to_excel('./../Excel/news_metropoles.xls', index=False, encoding='utf-8')
