def greetings(name, thurname):
    print("Доброго времени суток," + name + " Человек " + thurname + "!")

fullname = input().split(" ")
name = fullname[0]
thurname = fullname[1]

print(greetings(name, thurname))

