A=1
B=2
C=3
D=4
E=5
F=6

G= A>0 and B<0
print(f"G: {G}")

H= A!=B and A!=C and B!=C
print(f"H: {H}")

I= E!=0 and not(F>G)

J= (A<B and B<C) or (C<B and B<A) 
print(f"J: {J}")

K= not(F<0) and not(E<0) or F<0 and E<0
print(f"K: {K}")