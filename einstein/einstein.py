def mc2(x):
    x = int(x)
    c = 300000000
    x = x*c**2
    x=int(x)
    return x
z = input("enter the mass: ")
s = mc2(z)
print(s)
