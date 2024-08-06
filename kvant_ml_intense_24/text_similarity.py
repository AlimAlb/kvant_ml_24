import numpy as np

def cosine_distance(a, b):
    cosine = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cosine

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

def dict_to_vector(dc):
    return np.array(list(dc.values()))

print('Введите первый текст: ')
text1 = input()
print('Введите второй текст: ')
text2 = input()

un_words = unique_words(text1, text2)
dict_1 = vectorize(text1, un_words)
dict_2 = vectorize(text2, un_words)

vector_1 = dict_to_vector(dict_1)
vector_2 = dict_to_vector(dict_2)


print(cosine_distance(vector_1, vector_2))



