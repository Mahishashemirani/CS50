from datetime import date
import inflect
import sys

inflector = inflect.engine()


def main():
        birthday = input("enter your birthday: ")
        return minutes(birthday)

def minutes(birthday):
    try:
        year, month, day = birthday.split("-")
        birthday = date(int(year), int(month), int(day))
    except:
        return sys.exit("Invalid")
    duration =  (date.today() - birthday).days * 1440
    result = inflector.number_to_words(duration, andword="").capitalize()
    print(result + " minutes")
    return result + " minutes"


if __name__ == "__main__":
    main()

