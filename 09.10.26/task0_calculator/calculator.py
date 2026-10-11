import numpy as np


def add_numbers(a: float, b: float) -> float:
    """Функция складывает два числа."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Функция вычитает число b из числа a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Функция умножает два числа."""
    return a * b


def divide(a: float, b: float):
    """Функция делит a на b с защитой от нуля."""
    if b == 0:
        return "Ошибка: на ноль делить нельзя!"
    return a / b


def square_root(a: float) -> float:
    """Функция извлекает квадратный корень через numpy."""
    return float(np.sqrt(a))