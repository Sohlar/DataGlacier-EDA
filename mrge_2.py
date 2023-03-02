import numpy as np
import pandas as pd
import json
import datetime


Cab_Data = pd.read_csv('./DataSets/Cab_Data.csv', memory_map=True, na_filter=False)
start_date = datetime.datetime(1900,1,1)
print(start_date)
Cab_Data.columns = Cab_Data.columns.str.replace(' ', '_')
Cab_Data['Date_of_Travel'] = pd.to_datetime(Cab_Data['Date_of_Travel'], unit='d', origin=start_date)
Cab_Data[['KM_Travelled', 'Price_Charged', 'Cost_of_Trip']] = Cab_Data[['KM_Travelled', 'Price_Charged', 'Cost_of_Trip']].astype('int64')
Cab_Data['Profit'] = Cab_Data['Price_Charged'] - Cab_Data['Cost_of_Trip']

Cab_Data_f = (Cab_Data.sort_values('Date_of_Travel', ascending=True)).copy()

print(Cab_Data['Date_of_Travel'].head)

#Read City Data
City_Data = pd.read_csv('./DataSets/City.csv')
City_Data.columns = City_Data.columns.str.replace(" ", "_")

#Read Transaction Data
Transaction_Data = pd.read_csv('./DataSets/Transaction_ID.csv')
Transaction_Data.columns = Transaction_Data.columns.str.replace(" ", "_")

#Read Customer Data
Customer_Data = pd.read_csv('./DataSets/Customer_ID.csv')
Customer_Data.columns = Customer_Data.columns.str.replace(" ", "_")

Cab_Data_f.to_csv('./DataSets/fff.csv')

merged_data = pd.merge(Cab_Data_f, Transaction_Data, how='left', on='Transaction_ID')
final_data = pd.merge(merged_data, Customer_Data, how='left', on='Customer_ID')

final_data.to_csv('./DataSets/final_data.csv')
final_data.to_json('./DataSets/final_data.json')