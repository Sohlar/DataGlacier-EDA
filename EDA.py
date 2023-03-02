import scipy 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import json
import seaborn as sns


df = pd.read_json('./DataSets/final_data.json')


'''
def create_df_average_value_per_group(company, group, value):
    df_out = (df.query(f"Company == {company}")
              .groupby(f"{group}")[f"{value}"]
              .mean()
              .sort_values(ascending=False)
              .copy()
              )

              
# AVG PROFIT for RIDES LESS THAN AVERAGE KM_Travelled
#
fig2, ax2 = plt.subplots()
df_out = (df.query("Company == 'Yellow Cab' and KM_Travelled < 22")
          .groupby('City')[['KM_Travelled','Profit', 'Price_Charged', 'Cost_of_Trip']]
          .mean()
          .sort_values(by='Profit', ascending=False)
          .copy()
          )
df_out['Profit'].plot.bar(ax=ax2, color='yellow', width=0.4, position=0)

df_out = (df.query("Company == 'Pink Cab' and KM_Travelled < 22")
          .groupby('City')[['KM_Travelled','Profit', 'Price_Charged', 'Cost_of_Trip']]
          .mean()
          .sort_values(by='Profit', ascending=False)
          .copy()
          )
df_out['Profit'].plot.bar(ax=ax2, color='pink', width=0.4, position=1)
#print(df_out.head(5))



# AVG PROFIT for RIDES LESS THAN AVERAGE KM_Travelled
#
fig3, ax3 = plt.subplots()
df_out = (df.query("Company == 'Yellow Cab' and KM_Travelled > 22")
          .groupby('City')[['KM_Travelled','Profit', 'Price_Charged', 'Cost_of_Trip']]
          .mean()
          .sort_values(by='Profit', ascending=False)
          .copy()
          )
df_out['Profit'].plot.bar(ax=ax3, color='yellow', width=0.4, position=0)


df_out = (df.query("Company == 'Pink Cab' and KM_Travelled > 22")
          .groupby('City')[['KM_Travelled','Profit', 'Price_Charged', 'Cost_of_Trip']]
          .mean()
          .sort_values(by='Profit', ascending=False)
          .copy()
          )
df_out['Profit'].plot.bar(ax=ax3, color='pink', width=0.4, position=1)
#df_out.plot.bar(ax=ax3, color='pink', width=0.8, position=1)
#ax3.plot(df_out.index, df_out['Profit'])


#Plot Total Transactions by City
fig, ax = plt.subplots()
df_out = (df.query("Company == 'Pink Cab'")
          .groupby('City')['Transaction_ID']
          .count()
          .sort_values(ascending=False)
          .copy())
df_out.plot.bar(ax=ax, color='Pink', width=0.4, position=0)

df_out = (df.query("Company == 'Yellow Cab'")
          .groupby('City')['Transaction_ID']
          .count()
          .sort_values(ascending=False)
          .copy())
df_out.plot.bar(ax=ax, color = "yellow", width=0.4, position=1)


#Average (City: Profit/KM )
df_out = (df.groupby("City")
          .apply(lambda x: x['Profit'].sum() / x['KM_Travelled'].sum())
          .sort_values(ascending=False)
          )
print(df_out)

df_out = (df.query("Company == 'Yellow Cab'")
          .groupby("City")
          .apply(lambda x: x['Profit'].sum() / x['KM_Travelled'].sum())
          .sort_values(ascending=False)
          )
print(df_out)

df_out = (df.query("Company == 'Pink Cab'")
          .groupby("City")
          .apply(lambda x: x['Profit'].sum() / x['KM_Travelled'].sum())
          .sort_values(ascending=False)
          )
print(df_out)

sns.pairplot(df.query("Company == 'Yellow Cab'"), 
             vars=['KM_Travelled','Income_(USD/Month)', 'Profit'], hue='Company')
plt.show()
'''

df_corr = df[['KM_Travelled', 'Income_(USD/Month)', 'Cost_of_Trip','Price_Charged','Profit', 'Company']].dropna().corr()

sns.heatmap(df_corr, annot=True)
plt.show()


#df_out = (df.query("Company == 'Yellow Cab'")
#          .agg(df['Profit'].sum() / df['KM_Travelled'].sum()))

#          .agg({'Profit': 'sum', 'KM_Travelled': 'sum'})
#          .apply(lambda x: x['Profit'] / x['KM_Travelled']))



