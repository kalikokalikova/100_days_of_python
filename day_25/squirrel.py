import pandas

data = pandas.read_csv("squirrel_data.csv")

# print(data["Primary Fur Color"])
colors_list = data["Primary Fur Color"].to_list()

color_dict = {i:colors_list.count(i) for i in colors_list}
print(color_dict)
# {nan: 55, 'Gray': 2473, 'Cinnamon': 392, 'Black': 103}

new_color_dict = { 'Fur Color': ['Gray', 'Cinnamon', 'Black'],
                   'Count': [color_dict['Gray'], color_dict['Cinnamon'], color_dict['Black']]
                  }
# {'colors': ['Gray', 'Cinnamon', 'Black'],
#  'number': [2473, 391, 103]  }

colors_df = pandas.DataFrame(new_color_dict)
print(colors_df)