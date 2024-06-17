def is_valid(s):
    return (check_length(s) and
            check_start_with_letters(s) and
            check_numbers_at_end(s) and
            check_no_invalid_characters(s))

def check_length(s):
    return 2 <= len(s) <= 6

def check_start_with_letters(s):
    return s[:2].isalpha()

def check_numbers_at_end(s):

    for i in range(len(s)):
        if s[i].isdigit():

            if not s[i:].isdigit():
                return False

            if s[i] == '0':
                return False
            break
    return True

def check_no_invalid_characters(s):
    return s.isalnum()

def main():
    plate = input("Enter a vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
