from pyfiglet import Figlet
from random import randrange
import sys

figlet = Figlet()
fonts = figlet.getFonts()

try:
    if len(sys.argv) == 1:
        input_text = input("Input: ")
        figlet.setFont(font=fonts[randrange(len(fonts))])
        print(figlet.renderText(input_text))

    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f"  or sys.argv[0] == "--font") and sys.argv[2] in fonts:
            input_text = input("Input: ")   
            figlet.setFont(font=fonts[fonts.index(sys.argv[2])])
            print(figlet.renderText(input_text))

        else:
            raise ValueError
            sys.exit(0)

    else:
        raise ValueError
        sys.exit(0)

except ValueError:
    print("Invalid usage")



