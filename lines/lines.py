import sys
import os

def count_lines_of_code(filename):

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)

   
    if not filename.endswith(".py"):
        print(f"Error: File '{filename}' is not a Python file (.py).")
        sys.exit(1)


    lines_of_code = 0


    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if line == "" or line.startswith("#"):

                continue


            lines_of_code += 1

    return lines_of_code

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Error: Please provide exactly one argument - the Python file name.")
        sys.exit(1)

    filename = sys.argv[1]
    total_lines = count_lines_of_code(filename)

    print(f"Total lines of code in '{filename}': {total_lines}")
