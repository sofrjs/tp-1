import cmath
A=1.0
B=3.0
C=4.0

F = ((A*B)/cmath.sqrt(C).real)/(C-1/B)-(2*C/A)
print(f"F: {F}")

G = (2*A-B/cmath.sqrt(C).real)/(C+1/B)*B/4
print(f"G: {G}")