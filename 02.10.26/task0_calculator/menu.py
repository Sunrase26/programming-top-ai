from task0_calculator.calculator import add_numbers, divide, multiply, square_root, subtract

while True:
    print("\n" + "=" * 30)
    print("       КАЛЬКУЛЯТОР")
    print("=" * 30)
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Квадратный корень (√)")
    print("0. Выход")
    print("=" * 30)

    choice = input("Выберите действие (0-5): ")

    if choice == "0":
        print("Пока!")
        break

    if choice == "5":
        num = float(input("Введите число: "))
        print("Результат:", square_root(num))

    elif choice in ["1", "2", "3", "4"]:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == "1":
            print("Результат:", add_numbers(num1, num2))
        elif choice == "2":
            print("Результат:", subtract(num1, num2))
        elif choice == "3":
            print("Результат:", multiply(num1, num2))
        elif choice == "4":
            print("Результат:", divide(num1, num2))
    else:
        print("Нет такого действия, попробуйте снова!")