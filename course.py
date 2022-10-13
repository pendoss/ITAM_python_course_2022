from unicodedata import decimal


class Binary:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other) :
        return Binary(int(bin(Binary.ToDec(int(self.num)))[2::]) + int(bin(Binary.ToDec(int(other.num)))[2::]))
    def __sub__(self,  other):
        return int(bin(Binary.ToDec(int(self.num))[2::] - bin(Binary.ToDec(other.num), 2))[2::])
    def __mul__(self, other):
        return int(bin(Binary.ToDec(int(self.num))[2::] *bin(Binary.ToDec(other.num), 2))[2::])
    def __floordiv__(self, other):
        return int(bin(Binary.ToDec(int(self.num)) // bin(Binary.ToDec(other.num), 2))[2::])

    def __str__(self):
        return str(self.num)
    
    @staticmethod
    def ToDec(num):
        dec = 0
        num = str(num)
        # print(len(num), [i for i in range(len(num)-1, -1 ,-1)])
        for i in range(len(num)-1, -1 ,-1):
            
            dec += int(num[i])*pow(2,i)

        return int(dec)
    
    



        


def main():
    b = Binary(10)
    a = Binary(101)

    print(a+b)


if __name__ == "__main__":
    main()