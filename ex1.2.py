numbers = list(map(int, input().split()))
last_number = numbers[0]
for i in range(1, last_number + 1):
    if i not in numbers[1:]:
        print(i)
        break
