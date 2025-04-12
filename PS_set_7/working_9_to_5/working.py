import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([1-9]|1[0-2]):?([0-5][0-9])? ([ap]m) to ([1-9]|1[0-2]):?([0-5][0-9])? ([ap]m)$"
    match = re.match(pattern, s, re.IGNORECASE)
    if match:
        detail_tuple = match.groups() 
        print(detail_tuple)
        for i in detail_tuple:
            if i is None:
                print (i, "aaaaaaaaaaaaaa")
                detail_tuple[index(i)] = "00"

        if str(detail_tuple[2]).lower() == "am" and str(detail_tuple[5]).lower() == "pm":
            print(f"{detail_tuple[0]}:{detail_tuple[1]} to {detail_tuple[3]}:{detail_tuple[4]}")
            return "OK"
        elif str(detail_tuple[2]).lower() == "pm" and str(detail_tuple[5]).lower() == "am":
            print(f"{detail_tuple[3]}:{detail_tuple[4]} to {detail_tuple[0]}:{detail_tuple[1]}") 
        else:
            raise ValueError()
    
    else:
        return "None"

if __name__ == "__main__":
    main()
