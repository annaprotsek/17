import pandas as pd
import numpy as np

initial_data = {
    'Місяць': ['Вересень', 'Жовтень'],
    'Обсяг продажів': [1500, 1800]
}
initial_df = pd.DataFrame(initial_data)
initial_df.to_csv('sales_sep_oct.csv', index=False, encoding='utf-8')

df = pd.read_csv('sales_sep_oct.csv')

df['Листопад'] = np.random.randint(1000, 2000, size=len(df))
df['Грудень'] = np.random.randint(1000, 2000, size=len(df))

df.to_csv('sales_sep_dec.csv', index=False, encoding='utf-8')

print("Оновлена таблиця збережена у файл 'sales_sep_dec.csv'.")
