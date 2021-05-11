import pandas as pd
# data = pd.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(data['temp'].max())
# print(data[data.temp == data['temp'].max()])


squirell_df = pd.read_csv('squirell_data.csv')
squirells_by_color_df = squirell_df.groupby('Primary Fur Color').size()
print(squirells_by_color_df)
