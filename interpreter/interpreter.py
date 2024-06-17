def calc(x, y, z):
    x,z = float(x) , float(z)
    if y == "+" :
        print(float(x+z))
    if y == "-" :
        print(x-z)
    if y == "*" :
        print(x*z)
    if y == "/" :
        print(x/z)
x,y,z= input("expression:") .split(" ")
calc(x,y,z)

