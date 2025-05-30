from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Настройки Chrome для headless режима (работа без открытия окна браузера)
chrome_options = Options()
chrome_options.add_argument("--headless=new")

# Запускаем драйвер
driver = webdriver.Chrome(options=chrome_options)

# Открываем страницу
url = 'https://www.divan.ru/category/divany'
driver.get(url)

# Ждем, пока загружается вся страница (может потребоваться увеличение тайминга)
import time
time.sleep(5)

# Получаем HTML страницы после выполнения JavaScript
page_source = driver.page_source

# Закрываем браузер
driver.quit()

# Парсим HTML с помощью BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Извлекаем элементы с ценами
prices_elements = soup.find_all(class_='ui-LD-ZU KIkOH')
prices = []
for price_element in prices_elements:
    try:
        # Преобразование строки в число
        price_text = price_element.get_text().strip()
        price_value = int(price_text.replace(' ', ''))
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