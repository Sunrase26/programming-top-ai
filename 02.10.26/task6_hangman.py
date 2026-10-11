def get_hangman_art(mistakes):
    """Возвращает рисунок виселицы в зависимости от количества ошибок."""
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return stages[mistakes]


word = "ПРОГРАММА"
guessed_letters = []
mistakes = 0
max_mistakes = 6

print("Добро пожаловать в игру Виселица!")

while mistakes < max_mistakes:
    print(get_hangman_art(mistakes))
    
    # Формируем слово с отгаданными буквами и пропусками
    display_word = ""
    for char in word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
            
    print("Слово:", display_word)
    print(f"Ошибок: {mistakes} из {max_mistakes}")
    
    # Проверка на победу
    if "_" not in display_word:
        print("\nВы победили! Загаданное слово:", word)
        break
        
    guess = input("\nВведите букву: ").upper()
    
    if guess in guessed_letters:
        print("⚠️ Вы уже называли эту букву!")
    elif guess in word:
        print("✅ Верно!")
        guessed_letters.append(guess)
    else:
        print("❌ Нет такой буквы!")
        guessed_letters.append(guess)
        mistakes += 1
        
# Проверка на проигрыш
if mistakes == max_mistakes:
    print(get_hangman_art(mistakes))
    print("Вы проиграли! Загаданное слово было:", word)