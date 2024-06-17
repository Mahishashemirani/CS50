def coke ():
    x = 50
    coins = ["25" , "10" , "5"]

    while x> 0 :
        s=input("enter_coin")
        if s in coins:

            s = int(s)
            x = x-s

        print("Amount Due: "+ str(x))


    print("Change Owed: " + str(abs(x)))
coke()


