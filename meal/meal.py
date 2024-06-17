def convert(time):
    time = time.split(":")
    minute = float(time[1])/60
    hour = float(time[0])
    time = hour+minute

    return time
def main ():
    x = input("what time is it?")

    x = convert(x)
    x = float(x)
    if 7<=x<=8 :
        print("breakfast time")
    if 12<=x<=13 :
        print("lunch time")
    if 18<=x<=19 :
        print("dinner time")
if __name__ == "__main__":
    main()
