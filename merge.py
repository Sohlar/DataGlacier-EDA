import scipy 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


#Read Cab Data (Master)
#can we add arguments to sort?
Cab_Data = pd.read_csv('./DataSets/Cab_Data.csv', memory_map=True, na_filter=False)

#replace spaces with underscores in column names
Cab_Data.columns = Cab_Data.columns.str.replace(' ', '_')
Cab_Data = (Cab_Data.sort_values('Date_of_Travel', ascending=True, inplace=False)
        .reset_index(drop=True)
)

#Read City Data
City_Data = pd.read_csv('./DataSets/City.csv')
City_Data.columns = City_Data.columns.str.replace(" ", "_")
#Read Transaction Data
Transaction_Data = pd.read_csv('./DataSets/Transaction_ID.csv')
Transaction_Data.columns = Transaction_Data.columns.str.replace(" ", "_")
print('Transaction Data Shape: ' + str(Transaction_Data.shape))
#Read Customer Data
Customer_Data = pd.read_csv('./DataSets/Customer_ID.csv')
Customer_Data = Customer_Data.columns.str.replace(" ", "_")
print('Customer Data Shape' + str(Customer_Data.shape))

#Profit Column added
Cab_Data['Profit'] = Cab_Data['Price_Charged'] - Cab_Data['Cost_of_Trip']
#Cab_Data split by Company

yC_group_sum = (Cab_Data[Cab_Data['Company'] == 'Yellow Cab']
                .groupby('Date_of_Travel')
                .sum(numeric_only=True)
                .reset_index(drop=True))

pC_group_sum = (Cab_Data[Cab_Data['Company'] == 'Pink Cab']
                .groupby('Date_of_Travel')
                .sum(numeric_only=True)
                .reset_index(drop=True))

yCFrame = (Cab_Data[Cab_Data['Company'] == 'Yellow Cab']
        .reset_index(drop=True))
pCFrame = (Cab_Data[Cab_Data['Company'] == 'Pink Cab']
        .reset_index(drop=True))


##NON-GROUPED
##GROUPED

def group_sum_Customer_data():
    #Group by customer and sum transactions

    # for each transaction in each grouped customer id in Transaction_Data

    yC_group_sum_Customer = (Transaction_Data.groupby('Customer_ID'))
    print(yC_group_sum_Customer.shape)
    pC_group_sum_Customer = (Transaction_Data.groupby('Customer_ID'))
    print(pC_group_sum_Customer.shape)

    plt.style.use('dark_background')
    fig, ax = plt.subplots(1,2)
    ax[0,0] = (yC_group_sum_Customer.index, yC_group_sum_Customer)
    ax[0,0].set_title("Yellow")
    ax[0,1] = (pC_group_sum_Customer.index, pC_group_sum_Customer)
    ax[0,1].set_title("Pink")

group_sum_Customer_data()


#Date sorted frame summed   
yC_grouped_date_summed = yCFrame.groupby('Date_of_Travel').sum(numeric_only=True)
yC_grouped_date_summed = yC_grouped_date_summed.reset_index(drop=True)
pC_grouped_date_summed = pCFrame.groupby('Date_of_Travel').sum(numeric_only=True)
pC_grouped_date_summed = pC_grouped_date_summed.reset_index(drop=True)

pC_slope, pC_intercept = np.polyfit(pC_grouped_date_summed.index, pC_grouped_date_summed['Profit'], 1)
yC_slope, yC_intercept = np.polyfit(yC_grouped_date_summed.index, yC_grouped_date_summed['Profit'], 1)




plt.style.use("dark_background")
plt.plot(yC_grouped_date_summed.index, yC_grouped_date_summed['Profit'], label="Yellow", color='yellow')
plt.plot(pC_grouped_date_summed.index, pC_grouped_date_summed['Profit'], label="Pink", color='pink')
#plt.plot(yC_grouped_date_summed.index, yC_slope*yC_grouped_date_summed.index + yC_intercept, label="white", color='black')
#plt.plot(pC_grouped_date_summed.index, pC_slope*pC_grouped_date_summed.index + pC_intercept, label="black", color='black')
plt.plot(yC_grouped_date_summed.index, yC_grouped_date_summed['Profit'].mean, label="black", color='black')
plt.plot(yC_grouped_date_summed.index, pC_grouped_date_summed['Profit'].mean, label="black", color='black')


plt.xlabel("Date")
plt.ylabel("Profit")
plt.title("Profit Over Time")

# Add a legend to the plot
plt.legend()

# Show the plot
plt.show()