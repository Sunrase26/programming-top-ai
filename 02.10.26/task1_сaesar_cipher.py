def caesar_cipher(text, shift, mode="encrypt"):
    """Шифрует или дешифрует текст сдвигом Цезаря."""
    if mode == "decrypt":
        shift = -shift
        
    ru_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    en_lower = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.lower() in ru_lower:
            alf = ru_lower

        elif char.lower() in en_lower:
            alf = en_lower

        else:
            result += char
            continue
            
        is_upper = char.isupper()
        old_index = alf.index(char.lower())
        new_index = (old_index + shift) % len(alf)
        new_char = alf[new_index]
        
        if is_upper:
            result += new_char.upper()
        else:
            result += new_char
            
    return result
# Проверка
print("Шифр (RU):", caesar_cipher("Привет, мир!", 3, "encrypt"))
print("Дешифр (RU):", caesar_cipher("Тулезх, плу!", 3, "decrypt"))
print("Шифр (EN):", caesar_cipher("Hello, World!", 3, "encrypt"))