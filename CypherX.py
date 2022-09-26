import random

class RSA:
    
    PublicKey = None
    PrivateKey = None
    
    def __init__(self , size):
        self.size = size
        self.psize = size >> 1
        
    def __make_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 
                  29, 31, 37, 41, 43, 47, 53, 59, 
                  61, 67, 71, 73, 79, 83, 89, 97, 
                  101, 103, 107, 109, 113, 127, 131, 
                  137, 139, 149, 151, 157, 163, 167, 
                  173, 179, 181, 191, 193, 197, 199, 
                  211, 223, 227]
        flag = True
        
        while flag:
            p = 1 | (1<< self.psize)
            p |= random.randrange(0,(1<<self.psize-1))
            flag = False
            for x in primes:
                flag = flag or (pow(x , p-1 , p) != 1)
                
        return p
    
    def __gcd(self , a , b):
        x0, x1 = 0, 1;
        while a != 0:
            (q, a), b = divmod(b, a), a
            x0, x1 = x1, x0 - q * x1
        return b, x0
    
    def MakeKey(self) -> None:
        p = self.__make_prime()
        q = self.__make_prime()
        
        n = p*q;
        phi = (p-1)*(q-1);
        
        flag = True
        while flag:
            e = random.randrange(2**(self.psize-1),2**(self.psize))
            g,d = self.__gcd(e , phi)
            if g == 1:
                flag = False
                
        self.PublicKey = [e , n]
        self.PrivateKey = [d , n]
        
    def Crypto(self , key , message):
        return pow(message , key[0] , key[1]);


if __name__ == '__main__':
    
    rsa = RSA(128)
    rsa.MakeKey()
    Message = 1<<129-1
    Encrypt = rsa.Crypto(rsa.PublicKey , Message)
    Decrypt = rsa.Crypto(rsa.PrivateKey , Encrypt)
    
    print(Message)
    print(Encrypt)
    print(Decrypt)