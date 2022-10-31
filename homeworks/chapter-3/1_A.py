class Binary:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other) :
        return Binary.ToBin(int(Binary.ToDec(self.num), base = 10) + int(Binary.ToDec(other.num), base = 10))
    
    def __sub__(self,  other):
        return Binary.ToBin(int(Binary.ToDec(self.num), base = 10) - int(Binary.ToDec(other.num), base = 10))
        
    def __mul__(self, other):
        return self.num * other.num
    
    def __floordiv__(self, other):
        return self.num // other.num
        

    def __str__(self):
        return str(self.num)
    
    @staticmethod
    def ToDec(num):
        dec = 0
        num = str(num)[::-1]
        
        for i in range(0,len(num)):
            
            dec += int(num[i])*pow(2,i)

        return str(dec)

    @staticmethod
    def ToBin(num):
        num = int(str(num))

        if num <= 0:
            return ''
        else:
            return Binary.ToBin(num//2) + str(num%2)

def main():
    b = Binary(10)
    a = Binary(101)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)




if __name__ == "__main__":
    main()
