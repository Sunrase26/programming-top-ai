import random
import string

while True:
    print("ГЕНЕРАТОР СЛОЖНЫХ ПАРОЛЕЙ")
    length_str = input("Введите длину пароля (или 0 для выхода): ")
    if length_str == "0":
        break
        
    length = int(length_str)
    use_lower = input("Использовать нижний регистр? (да/нет): ").lower() == "да"
    use_upper = input("Использовать верхний регистр? (да/нет): ").lower() == "да"
    use_digits = input("Использовать цифры? (да/нет): ").lower() == "да"
    use_spec = input("Использовать спецсимволы? (да/нет): ").lower() == "да"
    
    chars = ""
    if use_lower: chars += string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_spec: chars += string.punctuation
    
    if not chars:
        print("❌ Ошибка: нужно выбрать хотя бы одну настройку!")
    else:
        password = ""
        for _ in range(length):
            password += random.choice(chars)
        print("Ваш сгенерированный пароль:", password)