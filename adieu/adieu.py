import inflect

def main():
    p = inflect.engine()
    names = []

    print("Enter names one per line. Press Ctrl-D (or Ctrl-Z on Windows) to end input:")

    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

   
    farewell_message = "Adieu, adieu, to " + p.join(names)
    print(farewell_message)

if __name__ == "__main__":
    main()
