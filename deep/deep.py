def deep(x) :
    x = str(x)
    x = x.lower()
    x = x.strip()
    if x == "forty two" :
        print("yes")
    elif x == "forty-two" :
        print("yes")
    elif x == "42":
        print("yes")
    else :
        print("no")
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
deep(x)

