list_ = input().split()
step = int(list_[0])
word_str = list_[1]
word = []
for elem in word_str:
    word += elem
new_word = ''
for i in range(0, len(word), step):
    piece = ''
    for letter in word[i:step+i]:
        piece = letter + piece
    new_word += piece
print(new_word)
