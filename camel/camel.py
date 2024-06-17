def camel_to_snakes(x):
    s = ""
    for char in x:
        if char.isupper():
            s+= "_"+char.lower()
        else:
            s +=char
    if s.startswith("_"):
        s = s[1:]
    print(s)
x=input("espression:")
camel_to_snakes(x)
