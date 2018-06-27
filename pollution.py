import json
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
'''
#Asking user about the data to access
date = input("Enter Date")
month = input("Enter Month")
year = input("Enter Year")
hour = input("Enter Hours(24 Hr Format)")
filename = "./Data/" + year + month + date + "-" + hour + ".csv"
print(filename)
'''
filename = './Data/20180626-23.csv'
#Load Data into a pandas dataframe
data_df = pd.read_csv(filename)

#Plotting various pollutants as a pie chart for a city at a particular time 

city_df = data_df[data_df['station'] == "Secretariat, Amaravati - APPCB"]
print(city_df.head())
for pollutant in city_df:
    plt.pie(city_df['pollutant_avg'],labels=city_df['pollutant_id'],autopct = '%0.2f%%',shadow= True)
plt.axis('equal')
plt.show()
