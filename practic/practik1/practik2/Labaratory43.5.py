def remove_duplicates(s):
    words = s.split()
    unique_words = [words[i] for i in range(len(words)) if i == 0 or words[i] != words[i-1]]
    return " ".join(unique_words)
s = "hello world world world this is a test test"
result = remove_duplicates(s)
print(result)

#удалить копии слов в строке s при
# условии, что одинаковые слова записаны
# рядом одно с другимудалить копии слов
# в строке s при условии, что одинаковые
# слова записаны рядом одно с другим