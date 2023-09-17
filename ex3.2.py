word = input()
word_inverted = word[::-1]
word_list = []
word_list_inverted = []
for letter in word:
    word_list += letter
for letter in word_inverted:
    word_list_inverted += letter
flag_palindrome = False
flag_mirror = False
if word == word_inverted:
    flag_palindrome = True
for index in range(len(word_list)):
    if word_list[index] in 'E, J, S, Z, 3, L, 2, 5':
        if word_list[index] == 'E' and word_list_inverted[index] == '3':
            flag_mirror = True
        elif word_list[index] == 'J' and word_list_inverted[index] == 'L':
            flag_mirror = True
        elif word_list[index] == 'S' and word_list_inverted[index] == '2':
            flag_mirror = True
        elif word_list[index] == 'Z' and word_list_inverted[index] == '5':
            flag_mirror = True
        elif word_list[index] == '3' and word_list_inverted[index] == 'E':
            flag_mirror = True
        elif word_list[index] == 'L' and word_list_inverted[index] == 'J':
            flag_mirror = True
        elif word_list[index] == '2' and word_list_inverted[index] == 'S':
            flag_mirror = True
        elif word_list[index] == '5' and word_list_inverted[index] == 'Z':
            flag_mirror = True
        elif word_list[index] == 'E' and word_list_inverted[index] != '3':
            flag_mirror = False
        elif word_list[index] == 'J' and word_list_inverted[index] != 'L':
            flag_mirror = False
        elif word_list[index] == 'S' and word_list_inverted[index] != '2':
            flag_mirror = False
        elif word_list[index] == 'Z' and word_list_inverted[index] != '5':
            flag_mirror = False
        elif word_list[index] == '3' and word_list_inverted[index] != 'E':
            flag_mirror = False
        elif word_list[index] == 'L' and word_list_inverted[index] != 'J':
            flag_mirror = False
        elif word_list[index] == '2' and word_list_inverted[index] != 'S':
            flag_mirror = False
        elif word_list[index] == '5' and word_list_inverted[index] != 'Z':
            flag_mirror = False
    elif word_list[index] in 'A, H, I, M, O, T, U, V, W, X, Y, 1, 8':
        if word_list[index] == word_list_inverted[index]:
            flag_mirror = True
    else:
            flag_mirror = False
            break
if flag_palindrome and not flag_mirror:
    print(word, 'is a regular palindrom.')
elif not flag_palindrome and flag_mirror:
    print(word, 'is a mirrored string')
elif flag_palindrome and flag_mirror:
    print(word, 'is a mirrored palindrome')
else:
    print(word,'is not a palindrome')

