from random import randint

def main():
    user_level = get_level()

    # On initialise le score
    score = 0

    for i in range(10):
        # On initialies les valeurs de a et b pour la 1ère itération + on met le nombre d'erreurs à 0
        bornes = generate_integer(user_level)
        fails = 0
        # Boucle While nécessaire pour try/except, pour qu'on incrémente le i uniquement si voulu (pas de ValueError renvoyée)
        while True:     
            try:
                answer = int(input(str(bornes[0]) + "+" + str(bornes[1]) + "? "))
                if answer == bornes[0] + bornes[1]: # Bonne réponse : On re randomise + on peut sortir du while true et ++ le i + on ++ le score
                    score = score + 1
                    break
                else: # Mauvaise réponse : EEE et on ++ le nombre de fails
                    print("EEE")
                    fails = fails +1
                    #DEBUG print("fails: " + str(fails))
                    if fails == 3: #3 fails, il faut print la bonne réponse, réinit les fails à 0 et passer à la prochaine itération de bornes
                        print("La bonne réponse était : " + str(bornes[0] + bornes[1]))
                        fails = 0
                        break
                    pass

            except ValueError:
                pass
    print("Score : " + str(score))


def get_level():
    # Choix du niveau, contrôle la bonne valeur
    while True:
        try:
            level = int(input("Choose a level: "))

            if level in [1,2,3]:
                return level
            else:
                continue
        
        except ValueError:
            continue


def generate_integer(level):
    a = randint(10**(level-1),(10**level)-1)
    b = randint(10**(level-1),(10**level)-1)
    return [a, b]

if __name__ == "__main__":
    main()

