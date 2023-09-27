numbers = list(input().split())
for i in range(1):numbers.insert(0, numbers.pop())
print(' '.join(numbers))
