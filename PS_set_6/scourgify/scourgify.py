import sys
import csv


if len(sys.argv) != 3:
    print("Too many or too few command-line arguments")
    sys.exit(0)

user_input_file = sys.argv[1]
user_output_file = sys.argv[2]

if str(user_input_file)[-4:] != ".csv" or str(user_output_file)[-4:] != ".csv":
    print("Not a CSV file")
    sys.exit(0) 

try: 
    i = 0
    with open(user_input_file) as file, open(user_output_file, "w") as out:
        for line in file:
            #Gestion du header
            if i == 0:
                writer = csv.DictWriter(out, fieldnames=["first", "last", "house"])
                writer.writeheader()
                i += 1
                continue
            else:
                #Le strip marche pas, on fait un replace brut pour l'espace
                first, last, house = line.strip().replace('"', "").replace("\n", "").replace(" ", "").split(",")
                print(first, last, house)
                writer = csv.DictWriter(out, fieldnames=["first", "last", "house"])
                writer = writer.writerow({"first": first, "last": last, "house":house})
                continue

except FileNotFoundError:
    print("No such file or directory")
    sys.exit(0) 
