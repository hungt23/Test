##package for data analysis
import pandas as pd
##math package
from math import cos, asin, sqrt, pi
##package that should be able to decipher geographic stuff like distance between two points
import geopy.distance
from geopy import distance

##my file path
file_name= "C:/Users/hungd/Documents/Data Analyst Projects/Bike Project/1321.xlsx"

##reads excel and assigns it to a data frame through pandas
df = pd.read_excel(file_name)

## The following was my attempted at dropping null values in the larger set. I sent you a smaller one w/o nulls
#df.dropna(subset=df['end_lat'],inplace=True)

##Method 1: This is just raw computing using tha math pacakges. In theory this should work but a float error happens
#def distance(lat1, lon1, lat2, lon2):
    #p=pi/180
    #a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    #return 12742 * asin(sqrt(a))

##Method 2: This uses the geopy package and should just take them and work.
## below is pandas creating the new column and accessing the other columns. This works up to the point of just easy summing.
#df['sum']=distance(df['start_lat'],df['start_lng'], df['end_lat'], df['end_lng'])


##Method 3: Different way of trying to use the distance function
#Beginning=(df['start_lat'],df['start_lng'])
#End=(df['end_lat'],df['end_lng'])
#df['Distance_traveled']=(distance.distance(Beginning,End).m)

#this exports the result as an excel titled sum, with sheet name attemptfsdf
df.to_excel("sum.xlsx", sheet_name='attemptfsdsf')

#way to check first 5 rows of result
print(df.head(5))