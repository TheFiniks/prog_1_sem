list_ = list(input().split())
len_group = int(list_[0])
word_str = list_[1]
word = []
for elem in word_str:
    word += elem
for i in range(0, len(word), len_group):
    word[i], word[i+len_group-1] = word[i+len_group-1], word[i]
new_word = ''.join(word)
print(new_word)
