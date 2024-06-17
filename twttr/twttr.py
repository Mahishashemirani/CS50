def twttr (x):
    vowels=["A","U","O","E","I","a","u","o","e","i"]
    s = ""
    for i in range(len(x)):
        if x[i] in vowels:
            pass
        else:
            s+=x[i]
    print(s)
z= input("enter the sentence")
twttr(z)
