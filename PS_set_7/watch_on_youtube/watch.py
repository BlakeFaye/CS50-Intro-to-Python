import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/(.+?)"'
    match = re.search(pattern, s, re.IGNORECASE)
    if match:
        print("https://youtu.be/", match.group(1))
        return "OK"
    else:
        return "None"

if __name__ == "__main__":
    main()
