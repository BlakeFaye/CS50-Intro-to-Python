from datetime import date
import inflect
import sys


def main():
    try:
        p = inflect.engine()
        birth = input ("Date of birth: ")
        diff = date.today() - (date.fromisoformat(birth))
        diff_mins = p.number_to_words(diff.days * 24 * 60, andword="")
        print(f"{diff_mins[:1].upper() + diff_mins[1:]} minutes")

    except:
        print("Invalid date")
        sys.exit(0)

if __name__ == "__main__":
    main()
