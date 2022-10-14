from distutils.filelist import translate_pattern


class Ternary:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other) :
        return Ternary.ToTernary(int(Ternary.ToDec(self.num), base = 10) + int(Ternary.ToDec(other.num), base = 10))
    
    def __sub__(self,  other):
        return Ternary.ToTernary(int(Ternary.ToDec(self.num), base = 10) - int(Ternary.ToDec(other.num), base = 10))
        
    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):
        return int(Ternary.ToDec(self.num)) // int(Ternary.ToDec(other.num))
        

    def __str__(self):
        return str(self.num)
    
    @staticmethod
    def ToTernary(num):
        num = int(str(num))

        if num <= 0:
            return ''
        else:
            return Ternary.ToTernary(num//3) + str(num%3)
    
    @staticmethod
    def ToDec(num):
        dec = 0
        num = str(num)[::-1]
        
        for i in range(0,len(num)):
            
            dec += int(num[i])*pow(3,i)

        return str(dec)
    

def main():
    a = Ternary(10)
    b = Ternary(2)
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)


if __name__ == "__main__":
    main()
