def bank(x) :
    x = x.lower()
    x = x.strip()
    print(x[0:5])

    if x[0]== "h" :
        if x[0:5] != "hello" :
            print("$20")
        elif x[0:5] == "hello" :
            print("$0")
    else :
        print("$100")
x = input("greeting :")
bank(x)
