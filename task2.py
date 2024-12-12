import numpy as np


def process_matrix(filename):
    """Обробка матриці: обчислення середнього та максимуму парних стовпців і векторний добуток."""
    matrix = np.loadtxt(filename)  # Завантаження матриці з файлу
    m, n = matrix.shape

    # Обчислення середнього та максимуму для парних стовпців
    results = []
    for col in range(1, n, 2):  # Парні стовпці (2, 4, ...)
        avg = np.mean(matrix[:, col])
        max_val = np.max(matrix[:, col])
        results.append((float(avg), float(max_val)))  # Перетворення в звичайні числа

    # Генерація випадкової матриці того ж розміру
    random_matrix = np.random.rand(m, n)

    # Векторний добуток
    product = np.multiply(matrix, random_matrix)

    return results, product


def task2():
    """Зовнішня функція для виклику обробки матриці."""
    filename = input("Введіть ім'я файлу з матрицею: ")
    results, product = process_matrix(filename)

    print("Середнє та максимум для парних стовпців:")
    for i, (avg, max_val) in enumerate(results, start=1):
        print(f"Стовпець {2 * i}: Середнє = {avg:.2f}, Максимум = {max_val:.2f}")

    print("\nВекторний добуток матриць:\n", product)

task2()
