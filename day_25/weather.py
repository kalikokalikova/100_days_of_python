# with open('weather_data.csv') as weather_csv:
#     data = weather_csv.read().splitlines()
#     print(data)

# import csv

# with open('weather_data.csv') as weather_csv:
#     reader = csv.reader(weather_csv)
#     rows = list(reader)[1:]
#     temps = []
#     for row in rows:
#         temps.append(int(row[1]))

# print(temps)
# TOO MUCH FAFF

import pandas

data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])

# temp_list = data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())

monday_row = data[data.day == "Monday"]
# print(monday_row)

max_temp_row = data[data.temp == data.temp.max()]
# print(max_temp_row)

print(monday_row.temp)


# create dataframe from scratch
data_dict = {
    "students": ["calico", "fry", "evan"],
    "scores": [70, 80, 90]
}

data = pandas.DataFrame(data_dict)
print(data)
