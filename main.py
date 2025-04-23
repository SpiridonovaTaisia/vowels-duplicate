def count_vowels(sentence):
    vowels = 'аоуэыяеюиАОУЭЫЯЕЮИ'
    count = sum(1 for char in sentence if char in vowels)
    return count

user_input = input("Введите предложение: ")
vowel_count = count_vowels(user_input)
print(f"Количество гласных букв в предложении: {vowel_count}")