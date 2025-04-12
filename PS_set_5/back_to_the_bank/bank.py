def main():
    greet = input("What's you greeting? ")
    print("$"+ str(value(greet)))

def value(greeting):
    if str(greeting[:5]).lower() == "hello":
        return 0
    elif str(greeting[:1]).lower() == "h":
        return 20
    else: 
        return 100

if __name__ == "__main__":
    main()