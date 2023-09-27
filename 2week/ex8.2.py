lenght = int(input())
numbers = list(map(int, input().split()))
side = lenght//2
for num1 in numbers:
    count_num_in_side = 0
    for num2 in numbers:
        if num1 > num2:
            count_num_in_side += 1
    if count_num_in_side == side:
        ans = num1
        break
print(ans)
