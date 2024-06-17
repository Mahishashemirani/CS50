import sys
import random
from pyfiglet import Figlet

def main():

    figlet = Figlet()
    available_fonts = figlet.getFonts()


    if len(sys.argv) not in [1, 3]:
        print("Usage: python figlet.py [--font FONT_NAME]")
        sys.exit(1)

    if len(sys.argv) == 3:
        option = sys.argv[1]
        font = sys.argv[2]
        if option not in ["-f", "--font"] or font not in available_fonts:
            print("Invalid font or option")
            sys.exit(1)
        figlet.setFont(font=sys.argv[2])
    else:

        font = random.choice(available_fonts)


    user_text = input("Input: ")



    ascii_art = figlet.renderText(user_text)
    print(ascii_art)
if __name__ == "__main__":
    main()
