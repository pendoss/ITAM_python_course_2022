def summation(start, end):
    s = 0
    for i in range(int(start), int(end)+1):
        s += i
    return s

nums = input().split(" ")
start = nums[0]
end = nums[1]

print(summation(start,end))

