import numpy as np

# Заданная функция для интегрирования
def f(x):
    return 1/(1 + x)**2

# Функция для вычисления интеграла методом трапеций
def integrate_trapezoidal(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = (h/2) * (y[0] + 2*np.sum(y[1:n]) + y[n])
    return integral

# Функция для вычисления интеграла методом прямоугольников (средних прямоугольников)
def integrate_rectangular(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)
    y = f(x)
    integral = h * np.sum(y)
    return integral

# Функция для вычисления интеграла методом Симпсона
def integrate_simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Число отрезков n должно быть четным.")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = (h/3) * (y[0] + 4*np.sum(y[1:n:2]) + 2*np.sum(y[2:n-1:2]) + y[n])
    return integral

# Точное значение интеграла для сравнения
exact_integral = 2/3

# Заданный интервал интегрирования
a = 0
b = 2

# Количество отрезков для разбиения интервала
n = 100

# Вычисление интеграла методом трапеций
trapezoidal_result = integrate_trapezoidal(f, a, b, n)

# Вычисление интеграла методом прямоугольников
rectangular_result = integrate_rectangular(f, a, b, n)

# Вычисление интеграла методом Симпсона
simpson_result = integrate_simpson(f, a, b, n)

# Вывод результатов
print("Приближенное значение интеграла методом трапеций:", trapezoidal_result)
print("Приближенное значение интеграла методом прямоугольников:", rectangular_result)
print("Приближенное значение интеграла методом Симпсона:", simpson_result)
print("Точное значение интеграла:", exact_integral)
