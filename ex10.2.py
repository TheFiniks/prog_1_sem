with open('input.txt', 'r', encoding='utf-8') as f:
    sentencens = f.read()
list_sent = list(sentencens.split())
new_list_sent = []
last_letter = ''
for word in list_sent:
    new_word = ''
    for letter in word:
        if letter in 'уеыаоэяию' and last_letter not in 'уеыаоэяию':
            new_word += f'{letter}c{letter}'
        else:
            new_word += letter
        last_letter = letter
    print(new_word, sep='\n', end=' ')
