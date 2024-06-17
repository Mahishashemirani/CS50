def main():
    a= input("Greeting: ")
    print(value(a))



def value(greeting):
    x = x.lower()
    x = x.strip()

    if x[0]== "h" :
        if x[0:5] != "hello" :
            return "$20"
        elif x[0:5] == "hello" :
            return"$0"
    else :
        return "$100"



if __name__ == "__main__":
    main()
