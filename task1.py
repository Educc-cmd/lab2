import math


def TriangleP(a, h):
    """Обчислення периметра рівнобедреного трикутника за основою a і висотою h."""
    b = math.sqrt((a / 2) ** 2 + h ** 2)  # Знаходимо сторону b за теоремою Піфагора
    return a + 2 * b  # Периметр трикутника


def find_perimeters(base_heights):
    """Повертає список периметрів для заданого списку основ і висот."""
    perimeters = []
    for a, h in base_heights:
        perimeters.append(TriangleP(a, h))
    return perimeters


def task1():
    """Введення даних, виклик функції та виведення результатів."""
    base_heights = []
    for i in range(3):
        a = float(input(f"Введіть основу трикутника {i + 1}: "))
        h = float(input(f"Введіть висоту трикутника {i + 1}: "))
        base_heights.append((a, h))

    perimeters = find_perimeters(base_heights)
    print("Периметри трикутників:", perimeters)

task1()
