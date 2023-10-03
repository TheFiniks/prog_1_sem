import string
with open("licence_agreement.txt", "r") as f:
    text = f.read()
d = dict()
words = ''
for line in text:
    line = line.lower()
    if line in str(string.punctuation) or line == '\n':
        words += ' '
    else:
        words += line
list_words = words.split()
for word in list_words:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
sort_d_keys = sorted(list(d.values()))[::-1]
max_d, count_ = 0, 0
for i in range(0, 10):
    for key in list(d.keys()):
        if d[key] == sort_d_keys[i] and count_!=10:
            print(d[key], key)
            count_ += 1

