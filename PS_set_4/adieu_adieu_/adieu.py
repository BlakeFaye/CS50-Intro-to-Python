#py -m  pip install inflect
#Test ajout commentaire pour commit
import inflect

p = inflect.engine()

names = []

while True:
    user_name = input("Name: ")
    if user_name != "":
        names.append(user_name)
    
    else:
        print("Adieu, adieu, to", p.join(names))
        break
