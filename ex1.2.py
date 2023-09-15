numbers = list(map(int, input().split()))
last_number = numbers[0]
for i in range(1, last_number + 1):
    count_ = numbers[1:].count(i)
    if count_ == 0:
        print(i)
