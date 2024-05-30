a=10
b=12
c=13
d=10

A= ((a>b) or (a<c)) and ((a==c) or (a>=b))
print(f"A: {A}")

B= ((a>=b) or (a<d)) and ((a>=d) and (c>d))
print(f"B: {B}")

C= not(a==c) and (c>b)
print(f"C: {C}")