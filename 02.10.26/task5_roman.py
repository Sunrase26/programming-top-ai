def int_to_roman(num):
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    roman = ""
    for value, symbol in roman_map:
        while num >= value:
            roman += symbol
            num -= value
            
    return roman


def roman_to_int(roman_str):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0 # Хранит значение символа, который стоял справа
    
    # Идем по строке в обратном порядке
    for char in reversed(roman_str):
        current_value = roman_dict[char]
        
        # Если текущее значение меньше предыдущего, значит это вычитание (например, IV = 5 - 1)
        if current_value < prev_value:
            total -= current_value  # Вычитаем
        else:
            total += current_value  # Иначе прибавляем
            
        prev_value = current_value # Запоминаем текущее значение для следующего шага
        
    return total


# Проверка
roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
print("Из римских в обычные:")
for r in roman_tests:
    print(f"{r} = {roman_to_int(r)}")

print("\nИз обычных в римские:")
for n in [4, 9, 42, 99, 2023]:
    print(f"{n} = {int_to_roman(n)}")