import pandas

all_squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_series = all_squirrels["Primary Fur Color"]
undupe_color_series = color_series.drop_duplicates()

color_series_with_counts = []
for squirrel_color in undupe_color_series:
    new_dict = {}
    new_dict.update({"Fur Color": squirrel_color})
    squirrels_with_color = all_squirrels[all_squirrels["Primary Fur Color"] == squirrel_color]
    squirrel_count = squirrels_with_color["X"].count()
    new_dict.update({"Count": squirrel_count})
    if squirrel_count > 0:
        color_series_with_counts.append(new_dict)

data_out = pandas.DataFrame(color_series_with_counts)
data_out.to_csv("squirrel_counts.csv")
