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
print(data_df['station'== 'Adarsh Nagar, Jaipur - RSPCB'])
