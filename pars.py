import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Запрашиваем страницу
url = 'https://divan.ru/catalog/divany/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Извлекаем элементы с ценами
prices_elements = soup.find_all(class_='product__price')
prices = []
for price_element in prices_elements:
    try:
        # Преобразование строки в число
        price_text = price_element.get_text().strip()
        price_value = int(price_text.replace(' ', ''))  # убираем пробелы перед переводом в целое число
        prices.append(price_value)
    except ValueError:
        continue

# Сохраняем цены в CSV
df_prices = pd.DataFrame(prices, columns=["Цена"])
df_prices.to_csv('divan_prices.csv', index=False)

# Средняя цена
mean_price = df_prices["Цена"].mean()
print(f"Средняя цена диванов: {mean_price:.2f}")

# Гистограмма цен
plt.hist(df_prices["Цена"], bins=20, edgecolor='black')
plt.title('Распределение цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество товаров')
plt.show()