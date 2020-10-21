
import math
class Quadratic_Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def discriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)

    def root1(self):
            if self.discriminant() < 0:
            	return f'({-self.b} + sqrt({self.discriminant()}))/{2*self.a}'
            else:		
            	return (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)
    def root2(self):
            if self.discriminant() < 0:
            	return f'({-self.b} - sqrt({self.discriminant()}))/{2*self.a}'            	
            else:
            	return (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)
    def __str__(self):
    	return (self.root1)
    	return (self.root2)
    	return (self.discriminant)


    def virtex_form(self):
    	h = -self.b / (2 * self.a)
    	k = self.c - (h**2)
    	return f'{self.a}(x-{h})+{k}'


q1 = Quadratic_Equation(1,4,1)
print(q1.virtex_form())





