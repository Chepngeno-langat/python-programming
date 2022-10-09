import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_sq_count)
print(red_sq_count)
print(black_sq_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq_count, red_sq_count, black_sq_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")