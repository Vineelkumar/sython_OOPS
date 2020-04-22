import math
class Fraction(object):
    def __init__(self,numerator = 0,denominator = 0):
        if numerator < 0 and denominator < 0:
            self._numerator = abs(int(numerator))
            self._denominator = abs(int(denominator))
   
        elif denominator < 0:
            self._numerator = -(int(numerator))
            self._denominator = abs(int(denominator))
        else:
            self._numerator = int(numerator)
            self._denominator = int(denominator)
            
        for i in range(1,self.denominator+1):
            if int(self._numerator) % i == 0 and int(self._denominator) % i == 0:
                k = i
        self._numerator = self._numerator // k
        self._denominator = self._denominator // k
    
    def __add__(self,other): 
        self.p = math.gcd(self._denominator,other._denominator)
        self.lcm = (self._denominator * other._denominator) // self.p
        
        
        self.oo = self._numerator * (self.lcm // self._denominator )
        self.ll = other._numerator * (self.lcm // other._denominator )
        self._numerator1 = self.oo + self.ll
        self._denominator1 = self.lcm
        

        for i in range(1,self._denominator1+1):
            if int(self._numerator1) % i == 0 and int(self._denominator1) % i == 0:
                k = i
        self._numerator1 = self._numerator1 // k
        self._denominator1 = self._denominator1 // k
        #print(self.numerator1)
        #print(self.denominator1)
        return Fraction(self._numerator1,self._denominator1)
    
    #def __str__(self):
             #   return '{}/{}'.format(u66897589y eteighergkneriheu;tdi;ihtdihaqself.numerator,self._denominator)        
    
    @property
    def numerator(self):
        return self._numerator
        
    @property
    def denominator(self):
        return self._denominator


if __name__ == "__main__":
    import json

    input_args = list(json.loads(input()))

    fraction_one = Fraction(*input_args[0])
    fraction_two = Fraction(*input_args[1])

    result_fraction = fraction_one + fraction_two

    try:
        fraction_one._numerator
    except AttributeError:
        print("Missed protecting numerator")

    try:
        fraction_one._denominator
    except AttributeError:
        print("Missed protecting denominator")

    try:
        fraction_one.numerator = 1
        print("Missed setting safe access to numerator")
    except AttributeError:
        pass

    try:
        fraction_one.denominator = 1
        print("Missed setting safe access to numerator")
    except AttributeError:
        pass
    print('{}/{} + {}/{} = {}/{}'.format(fraction_one.numerator ,fraction_one.denominator,fraction_two.numerator,fraction_two.denominator,result_fraction.numerator,result_fraction.denominator))
    print(isinstance(fraction_one, Fraction))
    print(isinstance(fraction_two, Fraction))
    print(result_fraction.numerator)
    print(result_fraction.denominator)
