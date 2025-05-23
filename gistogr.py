import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0      # Среднее значение
std_dev = 1   # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')

# Добавляем заголовок и подписи осей
plt.title('Нормально распределённые данные')
plt.xlabel('Значения')
plt.ylabel('Частота')

# Отображаем график
plt.show()