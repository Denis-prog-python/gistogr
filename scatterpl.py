import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(50)
y = np.random.rand(50)

# Построение scatter-плоттинга
plt.scatter(x, y, c='blue', marker='o', s=50, label='Случайные точки')

# Добавление заголовков и легенды
plt.title('Диаграмма рассеяния случайных точек')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.legend(loc='upper right')

# Отображение графика
plt.show()