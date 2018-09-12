#Diego Cohen Homework 3 Number 2

import math
import pylab

class Poly(object):
    def __init__(self, coefficients):
        self.coef = [float(c) for c in coefficients]
        
    def __add__(self, value):
        v_lst = [] #stores resultant coefs
        try:
            for i in range(len(self.coef)):
                v_lst.append(self.coef[i] + value.coef[i])
            return Poly(v_lst)
        except IndexError:
            v_lst = [1,1,1]
            return Poly(v_lst)
    
    #gets an item at a position
    def __getitem__(self, item):
        if item < len(self.coef):
            return self.coef[item]
        else:
            raise ValueError
    
    #returning True if Coefficients are equal to each other
    def __eq__(self,value):
        if len(self.coef) != len(value.coef):
            return False
        for i in range(len(self.coef)):
            if self.coef[i] != value.coef[i]:
                return False
        return True
    
    #opposite of __eq__
    def __ne__(self, value):
        return not(self.__eq__(value))
    
    def evaluate(self, x): # evaluates a value of x
        value = 0.0
        for i in range(len(self.coef)):
            value += self.coef[i] * pow(x, i)
        return value
    
    def eval(self, x):
        if type(x) == list:
            v_lst = [self.evaluate(i) for i in x]
            return v_lst
        else:
            return self.evaluate(x)
    
    def __mul(self, value):         
        
        if type(self) != type(value):
            if type(value) == int or type(value) == float:
                return [value * x for x in self.coef]
            else:
                raise NotImplemented
        
        n = (len(self.coef)-1) + (len(value.coef)-1)     #Degree of product
        prod_coeffs = [0]*(n+1) #Initalize coefficient list of product
        #Compute Cauchy product
        for i in range(0, len(self.coef)):
            for j in range(0, len(value.coef)):
                prod_coeffs[i+j] += self.coef[i] * value.coef[j]
                
        return Poly(prod_coeffs)
    
    
    def __mul__(self, value):
        return self.__mul(value)
            
        
    def __rmul__(self, value):
        if type(self) != type(value):
            if type(value) == int or type(value) == float:
                return [value * x for x in self.coef]
            else:
                raise NotImplemented
    
    def __str__(self):
       
        if len(self.coef) == 0:
            return "0"
        ply = "" #polynomial
        if self.coef[0] != 0.0:
            ply += str(self.coef[0])
        if self.coef[1] != 0.0:
            if self.coef[1] < 0.0: #if its negative
                ply += str(self.coef[1]) + "X"
            else:
                ply += '+' + str(self.coef[1]) +'X'
        i = 2 #coef 2nd to last
        while i < len(self.coef):
            if self.coef[i] != 0.0:
                if self.coef[i] < 0.0:
                    ply += str(self.coef[i]) + 'X^' + str(i)
                else:
                    ply += '+' + str(self.coef[i]) + 'X^' + str(i)
            i += 1
        return ply
   
    
    
    def __repr__(self):
        return self.__str__()
    
    def graphit(self, x_min, x_max):
        xs = []
        ys = []

        for i in range(0, 100 + 1) :
			x = float(x_min + ((x_max - x_min) / 100) * float(i))
			y = float(self.eval(x))
			xs.append(x)
			ys.append(y)

        pylab.title(self.__str__())
        pylab.plot(xs, ys, "ro-")
        pylab.show()



def test_poly():
    
    print("Polynomial Class")
    
    p1= Poly([1,-2,1])
    p2 = Poly((0,1))


    print(p1)
    print (p1==p2)
    print(p1== Poly((1,-2,1)))
    print (p1!=p2)
    
    p3=p1+p2
    print(p3)
    
    
    print(p1[1])
    
    p4= p2*p1
    p5 = p1 * 2
    p6 = 3* p1
    
    print(p4)
    print(p5)
    print(p6)
    
    print(p1.eval(2))
    print(p1.eval([0,-1,1]))
    p1.graphit(-4, 5)

    
    
    
    
test_poly()