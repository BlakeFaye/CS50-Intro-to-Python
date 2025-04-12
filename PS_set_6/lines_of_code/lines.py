import sys

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(0)

user_file = sys.argv[1]

if str(user_file)[-3:] != ".py":
    print("Not a Python file")
    sys.exit(0) 


number_of_lines = 0

try:
    with open(user_file) as file:
        contents = file.readlines()
        for line in contents:        
            if str(line).strip() == "":
                continue

            elif str(line).strip()[0] == "#":
                continue       

            else:
                number_of_lines = number_of_lines + 1
            
        print(number_of_lines)

except FileNotFoundError:
    print("No such file or directory")
    sys.exit(0) 
