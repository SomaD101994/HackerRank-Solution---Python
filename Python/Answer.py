cube = lambda x: pow(x,3)# complete the lambda function 
 def fibonacci(n):
     # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])
  
  ----------------------------------------------------------------------------------
  
  
  def fun(email):
    try:
        username, url = email.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False

    if username.replace('-', '').replace('_', '').isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)





----------------------------------------------------------------------




from fractions import Fraction
from functools import reduce

def product(fracs):
    t = Fraction(reduce(lambda x, y: x * y, fracs))# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
    
    
    
    
    
    ---------------------------------------------------------------------
    
    
    
    
    
    
 for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
        
        
        
        
        
 --------------------------------------------------------------------------





import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)
    
    
    
    
    
 ------------------------------------------------------------------



import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a + c, b + d)

    def __sub__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a - c, b - d)

    def __mul__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_mult = (a * c) - (b * d)
        imag_mult = (a * d) + (b * c)
        return Complex(real_mult, imag_mult)

    def __truediv__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_numerator = a * c + b * d
        imag_numerator = b * c - a * d
        denom = c * c + d * d
        real_div = real_numerator / denom
        imag_div = imag_numerator / denom
        return Complex(real_div, imag_div)

    def mod(self):
        a = self.real
        b = self.imaginary
        return Complex(math.sqrt(a ** 2 + b ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = '%.2f+0.00i' % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = '0.00+%.2fi' % (self.imaginary)
            else:
                result = '0.00-%.2fi' % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = '%.2f+%.2fi' % (self.real, self.imaginary)
        else:
            result = '%.2f-%.2fi' % (self.real, abs(self.imaginary))
        return result
    
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    
    
    
------------------------------------------------------------------------------------


import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points((self.x - no.x), (self.y - no.y), (self.z - no.z))

    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        return Points((self.y * no.z - self.z * no.y), (self.z * no.x - self.x * no.z), (self.x * no.y - self.y * no.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)



if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
    
    
    
    
    
    
  -----------------------------------------------------------------------
  
  
  
  import datetime
import calendar

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())



----------------------------------------------------------------------------



import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
