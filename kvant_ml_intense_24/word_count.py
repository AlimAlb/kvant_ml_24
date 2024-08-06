
s = "Маша мыла раму. Ей нужно много мыла"
word_list = s.lower().replace('.', '').split()

words = {}
for i in range(len(word_list)):
    if word_list[i] in words.keys():
        words[word_list[i]] += 1
    else:
        words[word_list[i]] = 1

print(words)