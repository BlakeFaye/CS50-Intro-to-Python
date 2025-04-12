import sys
from PIL import Image, ImageOps


if len(sys.argv) != 3:
    print("Too many or too few command-line arguments")
    sys.exit(0)

user_input_file = sys.argv[1]
user_output_file = sys.argv[2]

if str(user_input_file).lower()[-4:] not in [".jpeg", ".jpg", ".png"] or str(user_output_file).lower()[-4:] not in [".jpeg", ".jpg", ".png"] :
    print("Not an image file")
    sys.exit(0) 

if str(user_input_file).lower()[-4:] != str(user_output_file).lower()[-4:] :
    print("The input does not have the same extension as the output")

try: 
    print(str(user_output_file).split(".")[1].upper())
    with Image.open(user_input_file) as im, Image.open("shirt.png") as ref :    
        #im = im.rotate(angle = 60)
        ImageOps.fit(im, ref.size)
        im.paste(ref, (0,0), ref)
        im.save(user_output_file, str(user_output_file).split(".")[1].upper())

except FileNotFoundError:
    print("No such file or directory")
    sys.exit(0) 
