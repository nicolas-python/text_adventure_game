#text_adventure_game
player_name = None


def menu():

    choice = None

    while choice not in ["1","2", "3"]:
        print(" 1 : Benenne deinen Abenteurer")
        print(" 2 : Spielen ")
        print(" 3 : Beenden")

        choice = input("Wähle eine Option:")
        print("Du hast gewählt:", choice)

        if choice not in ["1" ,"2" ,"3" ]:
            print("Ungültige Option, bitte erneut zwischen 1,2,3 wählen.")

    return choice


def Hero_name():
    global player_name

    name = input("Wie soll dein Abenteurer heißen? : ")
    print("Willkommen zu deinem Abenteuer", name)
    print("Dein Abenteuere heißt:",name)
    print("Viel Erfolg, junger Abenteurer!")
    return name


def text_adventure_game(name):


    print("Du bist in einem Wald.", name)
    print("Wo willst du hin")







while True:
    choice = menu()

    match choice:
        case "1":
            player_name = Hero_name()
        case "2":
            if player_name is None:
                print("Bitte Namen Wählen")
            else:
                text_adventure_game(player_name)
        case "3":
            break










