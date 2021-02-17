
import pandas as pd

correio_string = pd.read_csv('./../Data/news_correio.csv')

#print(correio_string)

correio_string.to_excel('./../Excel/news_correio.xls', index=False, encoding='utf-8')
