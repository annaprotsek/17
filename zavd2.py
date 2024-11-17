import pandas as pd

with open('list.txt', 'w', encoding='utf-8') as file:
    file.write("apple\nbanana\norange\napple\nbanana\npear\norange\ngrape\n")

with open('list.txt', 'r', encoding='utf-8') as file:
    data = file.read().splitlines()

unique_data = pd.Series(list(set(data)))

with open('result.txt', 'w', encoding='utf-8') as file:
    for item in unique_data:
        file.write(item + '\n')

print("Оброблений список збережено у файл 'result.txt'.")
