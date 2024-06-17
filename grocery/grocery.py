def main():
    grocery_list=[]
    grocery_dict = {}
    while True:
        try:
            item = input().upper()
            grocery_list.append(item)
        except EOFError:
            print("")

            for i in grocery_list :
                if i in grocery_dict:
                    grocery_dict[i] += 1
                else:
                    grocery_dict[i] = 1

            for key, value in sorted(grocery_dict.items()):
                    print(value,key)
            exit()

if __name__=="__main__":
     main()

