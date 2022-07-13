import pandas

# with open("C:\Gm/Book1.csv",  'r', encoding='utf-8-sig') as weather:
data = pandas.read_csv("C:\Gm/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len([data["Primary Fur Color"] == "Cinnamon"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

framing = pandas.DataFrame(data_dict)
framing.to_csv("Squirrel Color Totals.csv")
