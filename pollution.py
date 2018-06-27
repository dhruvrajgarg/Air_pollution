import json
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Asking user about the data to access
date = input("Enter Date")
month = input("Enter Month")
year = input("Enter Year")
hour = input("Enter Hours(24 Hr Format)")
filename = "./Data/" + year + month + date + "-" + hour + ".csv"
print(filename)

#filename = './Data/20180626-23.csv'
#Load Data into a pandas dataframe
data_df = pd.read_csv(filename)

#Plotting various pollutants as a pie chart for a city at a particular time 
def current_polution_station_pie():
    all_stn = data_df['station']
    unique_stn = list(set(all_stn))
    print(unique_stn)
    selected_station = input('Please Enter Station name from above listed stations')
    stn_df = data_df[data_df['station'] == selected_station]
    #print(stn_df.head())
    for pollutant in stn_df:
        plt.pie(stn_df['pollutant_avg'],labels=stn_df['pollutant_id'] ,autopct = '%0.2f%%',shadow= True,radius= 3,pctdistance=0.8)
    plt.axis('equal')
    plt.show()

#Plotting max min avg value of a pollutant for a particular station a t a particular time 
def curr_pltn_stn_bar():
    all_stn = data_df['station']
    unique_stn = list(set(all_stn))
    print(unique_stn)
    selected_station = input(
        'Please Enter Station name from above listed stations')
    stn_df = data_df[data_df['station'] == selected_station]
    all_poll = stn_df['pollutant_id']
    print(all_poll)
    selected_pollutant = input('Please Enter pollutant name from above listed pollutants')
    pollutant = stn_df[stn_df['pollutant_id'] == selected_pollutant]
    print(pollutant['city'])
    xpos = np.arange(3)
    plt.bar(xpos[0],pollutant['pollutant_min'] , label='Minimum Value',width = 0.4,color = 'green')
    plt.bar(xpos[1],pollutant['pollutant_avg'] , label='Average Value',width = 0.4, color = 'blue')
    plt.bar(xpos[2],pollutant['pollutant_max'] , label='Maximum Value',width = 0.4, color = 'red' )
    plt.xticks(xpos, ['Minimum Value', 'Average Value','Maximum Value'])
    plt.legend()
    plt.title('Maximum, Minimum & Avgerage values for {} \n at {} in {} at {} on {}'.format(selected_pollutant,selected_station,pollutant['city'],hour + "Hrs",date + "-" + month + "-" + year))
    plt.show()

def main():
    #current_polution_station_pie()
    curr_pltn_stn_bar()



if __name__ == '__main__':
    main()
