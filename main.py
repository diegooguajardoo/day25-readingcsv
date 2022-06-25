import pandas

squirrel = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
weather = "weather_data.csv"
data = pandas.read_csv(squirrel)

cin_value = sum(data["Primary_Fur_Color"] == "Cinnamon")
black_value = sum(data["Primary_Fur_Color"] == "Black")
gray_value = sum(data["Primary_Fur_Color"] == "Gray")

output_dict = {
    "Color": [
        "Cinnamon",
        "Black",
        "Gray"
    ],
    "Value":
        [
            cin_value,
            black_value,
            gray_value
        ]
}

output_df = pandas.DataFrame(output_dict)
output_df.to_csv("squirrel_count.csv")