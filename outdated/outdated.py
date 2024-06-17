months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date_str = input("Date: ")
        try:
           
            if "/" in date_str:
                month, day, year = date_str.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:

                month_str, day_year = date_str.split(" ", 1)
                day, year = day_year.split(", ")
                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)


            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except (ValueError, IndexError):

            pass

if __name__ == "__main__":
    main()
