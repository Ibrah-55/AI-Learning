import matplotlib.pyplot as plt
import pandas as pd 

births = pd.read_csv('data/births.csv')

births = births[births.day <= 31]  

births['date'] = pd.to_datetime(
    births.year * 10000 + births.month * 100 + births.day, format='%Y%m%d', errors='coerce'
)
births = births.dropna(subset=['date'])

births.set_index('date', inplace=True)

births['dayofweek'] = births.index.dayofweek

births['decade'] = 10 * (births.year // 10)
pivot_table = births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='mean')

pivot_table.plot()
plt.gca().set_xticks(range(7)) 
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])  # Label x-axis
plt.ylabel('Mean Births by Day')
plt.title('Mean Births by Day of the Week Over Decades')
plt.show()
