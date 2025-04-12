import sys
from tabulate import tabulate
import csv

if len(sys.argv) != 2:
    print("Too many or too few command-line arguments")
    sys.exit(0)

user_file = sys.argv[1]

if str(user_file)[-4:] != ".csv":
    print("Not a CSV file")
    sys.exit(0) 

try: 
    with open(user_file) as file:
        reader = csv.DictReader(file)
        data = list(list(rec) for rec in csv.reader(file, delimiter=','))
        print(data)
        print(tabulate(data, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    print("No such file or directory")
    sys.exit(0) 
