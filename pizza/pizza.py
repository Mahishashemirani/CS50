import sys
import os
import csv
from tabulate import tabulate

def read_pizza_menu(filename):

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)


    if not filename.endswith(".csv"):
        print(f"Error: File '{filename}' is not a CSV file (.csv).")
        sys.exit(1)


    menu_data = []
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            menu_data.append(row)

    return menu_data

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Error: Please provide exactly one argument - the CSV file name.")
        sys.exit(1)

    filename = sys.argv[1]


    menu_data = read_pizza_menu(filename)


    table = tabulate(menu_data, headers='keys', tablefmt='grid')

    print(table)
