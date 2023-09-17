list_ = list(input().split())
mx_count = 0
for i in list_:
    if list_.count(i) > mx_count:
        mx_count = list_.count(i)
        elem = i
print(elem)
