import math

def lawOfCosines(B, C, a):
    rhs = B**2 + C**2 - 2*B*C*math.cos(a*math.pi/180)
    return math.sqrt(rhs)

def lawOfSines(A, a, B):
    rhs = B*math.sin(a*math.pi/180)/A
    return math.asin(rhs)*180/math.pi

print "Enter side B:"
B = float(raw_input())

print "Enter side C:"
C = float(raw_input())

print "Enter angle a:"
a = float(raw_input())

A = lawOfCosines(B, C, a)

b = lawOfSines(A, a, B)

c = lawOfSines(A, a, C)

print A, b, c
