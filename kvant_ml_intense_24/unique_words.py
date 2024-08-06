def unique_words(text1, text2):
    word_list_1 = text1.lower().replace('.', '').split()
    word_list_2 = text2.lower().replace('.', '').split()

    set1 = set(word_list_1)
    set2 = set(word_list_2)

    return set1.union(set2)


def vectorize(text, unique_words):
    word_list = text.lower().replace('.', '').split()
    words = {}
    unique_words = list(unique_words)
    for i in range(len(unique_words)):
        words[unique_words[i]] = 0

    for i in range(len(word_list)):
        if word_list[i] in words.keys():
            words[word_list[i]] += 1
    return words
        
text1 = "Маша мыла раму. Ей нужно много мыла"
text2 = 'Еду домой. Машину не мыла'

un_words = unique_words(text1, text2)
vector_1 = vectorize(text1, un_words)
vector_2 = vectorize(text2, un_words)

print(vector_1)
print(vector_2)
