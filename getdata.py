import requests
import json
import datetime
from time import strftime
import time
import schedule
import os

def get_data():
    #Getting todays date
    datetime = strftime("%Y%m%d-%H")

    #Getting data from api call 
    url = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001e10038d88e794f72722fa6078a70a5ca&format=csv&offset=0&limit=1000"
    parameters = {}
    response = requests.get(url, params=parameters)
    with open(os.path.join("Data", datetime +".csv"), 'wb') as f:
        f.write(response.content)
    


def main():
    schedule.every(1).hour.do(get_data)

    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
