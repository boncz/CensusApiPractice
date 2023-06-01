import pandas as pd
import requests
import csv
# making a request for all counties in the state of KY:
#Will find the total number of commuters, and the number of commuters for different time groups
#ideally, later I can find the percentage of people who must travel different lengths of time, and compare the different counties.
r=requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_004E,B08303_005E,B08303_006E,B08303_007E,B08303_008E&for=county:*&in=state:21')

r_json=r.json()

with open('commute_times_ky.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(r_json)

commute_times_df = pd.read_csv("commute_times_ky.csv")
commute_times_df.columns = ["Name", "Total Number of Commuters","Commute 10-14 Minutes","Commute 15-19 Minutes","Commute 20-24 Minutes","Commute 25-29 Minutes","Commute 30-34 Minutes","State Code","County Code"]

#viewing some of the data frame instead of the whole:
print(commute_times_df.head())
