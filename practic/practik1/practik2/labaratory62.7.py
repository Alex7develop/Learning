def remove_words(s1, s2):
    words_to_remove = s2.split()
    for word in words_to_remove:
        s1 = s1.replace(word, '')
    return s1
s1 = 'The quick brown fox jumps over the lazy dog'
s2 = 'quick dog'
result = remove_words(s1, s2)
print(result)

# Удалить из строки s1 все слова, которые есть в строке s2



