# Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd


df = pd.read_csv(
    'Python_Task\\Home_Work_Python\\Home_Work_9\\csv\\california_housing_train.csv')
min_population = df['population'].min()

df_filtered = df[df['population'] == min_population]

max_households = df_filtered['households'].max()

print(
    f'Максимальное значение households в зоне минимального значения population: {max_households}')
