from task0_calculator.calculator import add_numbers, divide, multiply, square_root, subtract

print("=== ТЕСТИРОВАНИЕ КАЛЬКУЛЯТОРА ===")

# Проверка сложения (Задача #3)
print("Сложение 5 + 3:", add_numbers(5.0, 3.0))

# Проверка остальных операций
print("Вычитание 10 - 4:", subtract(10.0, 4.0))
print("Умножение 3 * 4:", multiply(3.0, 4.0))

# Проверка обычного деления и деления на 0 (Задача #4)
print("Деление 10 / 2:", divide(10.0, 2.0))
print("Деление на 0:", divide(10.0, 0.0))

# Проверка корня из numpy
print("Корень из 16:", square_root(16.0))

print("=== ВСЕ ТЕСТЫ ВЫПОЛНЕНЫ ===")