numbers = list(map(int, input().split()))
for i in range(0, len(numbers), 2):
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(numbers)
