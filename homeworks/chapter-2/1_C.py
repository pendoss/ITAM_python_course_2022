def summation(num):
    m = max(num)
    s = 0
    for i in range(0,len(num)):
        if num[i] < 0:
            num[i] = abs(num[i])
        num[i] = num[i] / m
        s+=num[i]
    return s

num = list(map(float, input().split(" ")))
print(summation(num))


