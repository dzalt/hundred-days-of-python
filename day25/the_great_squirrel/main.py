# make dataframe of fur color and count

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black = data[data["Primary Fur Color"] == "Black"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
gray = data[data["Primary Fur Color"] == "Gray"]

squirrel = {
    "Fur color": ["Black", "Cinnamon", "Gray"],
    "Count": [len(black), len(cinnamon), len(gray)]
}

squirrel_color = pandas.DataFrame(squirrel)
squirrel_color.to_csv("data.csv")


# ,Fur color,Count
# 0,Black,103
# 1,Cinnamon,392
# 2,Gray,2473