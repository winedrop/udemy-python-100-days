# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()

#weather_data = open('weather_data.csv', 'r')
#Lines = weather_data.readlines()

# count = 0
# #Strips the newline character
# for line in Lines:
#     count+=1
#     print("Line{}: {}".format(count, line.strip()))

#------------------------------------------------------------

# count = 0

# while True:
#     count += 1

#     #get next line from file
#     line = weather_data.readline()

#     #if line is empty
#     #end of file is reached
#     if not line:
#         break
#     print("Line{}: {}".format(count, line.strip()))


# main issue with using this is that the rows are read in as lines and it is difficult to work with
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


#can use a python library for csv files, can see how this would be difficult as data gets larger, need to use pandas
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)

#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             print(row)
#             temperatures.append(int(row[1]));
        
#     print(temperatures)


#use pandas as the above would be difficult to use in larger datasets
#import pandas 

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))#pretty much pandas 2d data structure/table
# print(type(data["temp"]))#pandas series a 1d structure/list

# #there are many other functions that you can call to convert pandas data frame object
# data_dict = data.to_dict()
# print(data_dict)

# #there are other functions that you can call on the pandas series structure
# temp_list = data["temp"].to_list()
# print(temp_list)

# average = 0
# count = 0
# for temp_value in temp_list:
#     average += temp_value
#     count += 1
# average /= count
#--------- better way of doing average
#average = sum(temp_list) / len(temp_list)
#--------- using pandas to do average
# average = data["temp"].mean()
# print(average)
    
# #find max using pandas
# max = data["temp"].max()
# print(max)

# #both case sensitive
# #get data in columns
# print(data["condition"])
# #equivalent to above
# print(data.condition)

#get data in row
# print(data[data.day == "Monday"])

# #get row of data where temp is max
# #max = data["temp"].max()
# max = data.temp.max()
# print(data[data.temp == max])

# #after finding a row you can specify further and get columns
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# # print(monday.temp)
# # print(monday.day)

# monday_temp_C = int(monday.temp)
# monday_temp_F = monday_temp_C * 9/5 + 32
# print(monday_temp_F)

#create a dataframe from scratch
# data_dict = {
#     "students": ["Amay", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#--------------squirrel project------------
#desc: create new csv from data that contains fur color and count of each
from ast import Set
from mimetypes import types_map
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data["Primary Fur Color"]);


#gets the unique colors from Primary Fur Color
# list_primary_colors = data["Primary Fur Color"]
# color_list = list_primary_colors.drop_duplicates('first').to_list()
# for element in color_list:
#     if pandas.isnull(element):
#         color_list.remove(element)
# print(color_list)

# #add count to each color
# color_count = {0,0,0}
# for color in list_primary_colors:
#     if(color == color_list[0]){
#         color_count
#     }

color_counts = data["Primary Fur Color"]

df = color_counts.value_counts().rename_axis('Fur Color').to_frame('counts').reset_index()
print(type(df))
print(df)
ans = pandas.DataFrame(data = data["Primary Fur Color"].value_counts().to_dict(),index =[0], )
#DataFrame.from_dict({})
print(ans)
