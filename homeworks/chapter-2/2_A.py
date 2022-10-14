def ladder_levels(n):
    l = 0
    b = 1
    while n>0:
        l+=1
        n-=b
        b+=1
    return l

def main():

    n = int(input())

    print(ladder_levels(n))


if __name__ == "__main__":
    main()
