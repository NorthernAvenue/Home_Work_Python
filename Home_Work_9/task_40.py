# Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd


df = pd.read_csv(
    'Python_Task\\Home_Work_Python\\Home_Work_9\\csv\\california_housing_train.csv')

df_filtered = df[(df['population'] >= 0) & (df['population'] <= 500)]

mean_price = df_filtered['median_house_value'].mean()

print(
    f'Средняя стоимость дома, где количество людей от 0 до 500: {mean_price:.2f}$')
