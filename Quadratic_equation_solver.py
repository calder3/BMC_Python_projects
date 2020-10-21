
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
            	self.root1 = f'({-self.b} + sqrt({self.discriminant()}))/{2*self.a}'
            	return f'({-self.b} + sqrt({self.discriminant()}))/{2*self.a}'
            else:
            	self.root1 = (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)		
            	return (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)
    def root2(self):
            if self.discriminant() < 0:
            	self.root2 = f'({-self.b} - sqrt({self.discriminant()}))/{2*self.a}'
            	return f'({-self.b} - sqrt({self.discriminant()}))/{2*self.a}'            	
            else:
            	self.root2 = (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)
            	return (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)
    def __str__(self):
    	return (self.root1)
    	return (self.root2)
    	return (self.discriminant)


    def virtex_form(self):
    	h = -self.b / (2 * self.a)
    	k = self.c - (h**2)
    	return f'{self.a}(x-{h})+{k}'

    def facoted_form(self):
    	return f'(x-{self.root1})(x-{self.root2})'


q1 = Quadratic_Equation(1,4,4)
print(q1.virtex_form())
print(q1.root1())
print(q1.root2())
print(q1.facoted_form())





