# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:17:52 2016

@author: Mandar
"""
from urllib.request import urlopen
import json
import csv

Pincode = ['30322','30329','92799']
print(Pincode[0])
URL_Pre = 'https://api.weathersource.com/v1/75fdebce9e0417074545/''history_by_postal_code.json?period=day&postal_code_eq='
URL_Post = '&country_eq=US&timestamp_between=2012-02-10T00:00:00-05:00,2012-02-12T00:00:00-05:00&fields=postal_code,country,timestamp,tempMax,tempAvg,tempMin,precip,snowfall,windSpdMax,windSpdAvg,windSpdMin,cldCvrMax,cldCvrAvg,cldCvrMin,dewPtMax,dewPtAvg,dewPtMin,feelsLikeMax,feelsLikeAvg,feelsLikeMin,relHumMax,relHumAvg,relHumMin,sfcPresMax,sfcPresAvg,sfcPresMin,spcHumMax,spcHumAvg,spcHumMin,wetBulbMax,wetBulbAvg,wetBulbMin'
URL_Fetch = ''
pin = ''
#URL_Fetch = 'https://api.weathersource.com/v1/75fdebce9e0417074545/''history_by_postal_code.json?period=day&postal_code_eq='+PinCode[0]+'&country_eq=US&timestamp_between=2012-02-10T00:00:00-05:00,2012-02-15T00:00:00-05:00&fields=postal_code,country,timestamp,tempMax,tempAvg,tempMin,precip,snowfall,windSpdMax,windSpdAvg,windSpdMin,cldCvrMax,cldCvrAvg,cldCvrMin,dewPtMax,dewPtAvg,dewPtMin,feelsLikeMax,feelsLikeAvg,feelsLikeMin,relHumMax,relHumAvg,relHumMin,sfcPresMax,sfcPresAvg,sfcPresMin,spcHumMax,spcHumAvg,spcHumMin,wetBulbMax,wetBulbAvg,wetBulbMin'
weather_data = open('WeatherData.csv', 'a',newline = '')
csvwriter = csv.writer(weather_data)
count = 0

for i in Pincode:
            
            URL_Fetch = URL_Pre + i + URL_Post
            print(URL_Fetch)
            response=urlopen(URL_Fetch).read().decode('utf-8')
            with open('outputfile.json', 'a') as outf:
                { outf.write(response)}
            json_parsed = json.loads(response)          
            for wh in json_parsed:
                    if count == 0:
                        header = wh.keys()
                        csvwriter.writerow(header)
                    count += 1
                    csvwriter.writerow(wh.values())

weather_data.close()
''' with open('outputfile.json') as json_file:  
     json_parsed = json.load(json_file) 

print(json_parsed)

weather_data = open('WeatherData.csv', 'a',newline = '')


csvwriter = csv.writer(weather_data)

count = 0

for wh in json_parsed:

      if count == 0:

             header = wh.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(wh.values())

weather_data.close()
   
'''
