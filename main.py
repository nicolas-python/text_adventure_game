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
    print("Dein Abenteuerer heißt:",name)
    print("Viel Erfolg, junger Abenteurer!")
    return name


def text_adventure_game(name):
    while True:
        print("Du bist in einem Wald",name)

        choice = input("Wo willst du hin nach Norden,Osten,Süden,Westen oder Baum klettern? ").lower()

        if choice == "süden":
            south(name)
        elif choice == "osten":
            east(name)
        elif choice == "norden":
            north(name)
        elif choice == "westen":
            west(name)
        elif choice == "baum":
            print("Du kletterst auf einen Baum und entdeckst eine Lichtung.")
            tree_climb(name)

#Richtung norden
def north(name):
    print("Du gehst nach Norden, der Wald wird dunkler.")

    choice2 = input("Willst du weitergehen? (ja/nein) ").lower()

    if choice2 == "ja":
        print(name, "hörst du eine Stimme rufen.")

        choice3 = input("Willst du zurückrufen oder umkehren? (zurückrufen/umkehren) ").lower()

        if choice3 == "zurückrufen":
            print("Du versuchst mit der Stimme zu reden.")

            choice4 = input("Willst du deinen wahren Namen sagen? (ja/nein) ").lower()

            if choice4 == "ja":
                print("Du sagst zögernd", name)
                print("Das Wesen wirkt genervt: 'Hier ist es gefährlich, du solltest umkehren.'")

                choice5 = input("Willst du auf den Rat hören? (ja/nein) ").lower()

                if choice5 == "ja":
                    print("Du kehrst um und landest wieder am Startpunkt.")
                    return text_adventure_game(name)

                elif choice5 == "nein":
                    print("Du gehst tiefer in den dunklen Wald hinein.")
                    print("Das seltsames Wesen steht hinter dir und lacht.")
                    print("Es verschlingt dich mit Haut und Haar.")
                    print("Das letze was man hört sind deine schreie und das kanacken deiner brechenden knochen und das lachen von dem Wesen.")
                    print("Das war das grausame Ende von", name)
                    return

            elif choice4 == "nein":
                print("Du lügst, das Wesen lacht.")
                print("Es verschlingt dich mit Haut und Haar.")
                print("Das letze was man hört sind deine schreie und das kanacken deiner brechenden knochen und das kichern von dem Wesen.")
                return

        elif choice3 == "umkehren":
            print("Du kehrst um und landest wieder am Startpunkt.")
            return text_adventure_game(name)

    elif choice2 == "nein":
        print("Du kehrst um und läufst zurück zum Start.")
        return text_adventure_game(name)

#Richtung Osten
def east(name):
        print("Du stehst vor einer Steinwand mit seltsamen Zeichen darauf.")
        print("Es sieht so aus, als ob ein seltsames Monster umherläuft.")
        print("Darunter steht in Blut geschrieben: 'Sag die Wahrheit.'")
        print("Du machst dir nicht wirklich Gedanken darum.")

        choice2 = input("Willst du weiter Richtung Osten laufen? (ja/nein) ").lower()

        if choice2 == "ja":
            print("Du läufst weiter Richtung Osten und findest eine Truhe.")
            choice3 = input("Willst du die Truhe öffnen? (ja/nein) ")

            if choice3 == "ja":
                print("Du öffnest die Truhe.")
                print("Es ist eine Mimik!")
                print("Die Mimik frisst dich qualvoll auf.")
                print("Der junge Abenteurer", name, "starb voller Reue wegen Gier.")
                return

            elif choice3 == "nein":
                print("Du ignorierst die Truhe und hörst Schreie.")
                return choice_scene4(name)

        elif choice2 == "nein":
            print("Du willst umkehren, doch du hörst Schreie aus Richtung Osten.")
            return choice_scene4(name)


#Richtung Süden
def south(name):
        print("Du hörst komische Geräusche.")

        choice1 = input("Willst du in das gebüsch zu den geräuschen gehen ? (ja/nein) ").lower()

        if choice1 == "ja":
            print("Du gehst zögerlich zum gebüsch.")
            print("Du atmest erleichtert auf es ist nur ein kleines Kätzchen.")

            choice2=input("Willst du das Kätzchen streicheln (ja/nein) ").lower()

            if choice2 == "ja":
                print("Du streckst deine Hand aus um das Kätzchen zu streicheln.")
                print("Plötzlich beist das Kätzchen zu und rennt weg.")
                print("Hinter dir steht ein Goblin und schlagt dir mit der Keule auf den Kopf.")
                print("Du stirbst einen langsamen ernidrigenden Tod.")
                print("Ein Abenteuerer sollte immer achtsam sein",name)
                return

            elif choice2 == "nein":
                print("Du bemerkst eine Bewegung hinter dir.")
                print("Es ist ein Goblin.")
                print("Du erschlägst ihn.")
                print("Du leufst in die Richtung wo er herkam.")
                return choice_scene5(name)

        elif choice1 == "nein":
            print("Du drehst dich von dem gebüsch weg und leufst zögerlich weiter.")
            return choice_scene5(name)

# Richtung Westen
def west(name):
    print("Du siehst eine Lichtung.")
    print("In dieser lichtung findest du viele Fußspuren sowie klauen abdrücke.")
    print("inmitten der lichtung ist ein Blutverschmirter stein es sieht aus wie ein Opferaltar.")

    choice1 = input("Willst du dich ihm nähern oder die lichtung verlassen ? (nähern/verlassen).").lower()

    if choice1 == "nähern":
        print("Du näherst dich dem Opferaltar.")
        print("Du hörst eine stimme hinter dir,sie kichert.")
        print("Was tust du hier.")

        choice2 = input("Du überlegst solltest du die Wahrheit sagen oder Lügen ? (wahrheit/lüge ").lower()

        if choice2 == "wahrheit":
            print("Du frägst wer da redet und sagst du hättest dich verlaufen.")
            print("Aus dem dunkeln tritt eine seltsames wesen vor.")
            print("Es stellt sich vor als Ältester und erklärt das es hier gefährlich sei.")

            choice3 = input("Willst du es auf den altar ansprechen ? (ja/nein) ").lower()

            if choice3 == "ja":
                print("Du sprichst das Wesen das sich Ältester nennt auf den Blutigenaltar an.")
                print("Das wensen kichert nur und sagt das das Opfer für den Gott Cyric er wird hier angebetet.")
                print("Du überlegst ob es sich um einen Kult handeln könnte.")
                print("Du frägst nach ob es sich dabei um menschliche opfer handelt.")
                print("Der älteste sagt nur lachend mal so mal so aufjedenfall sind es immer Lügner.")

                choice4 = input("Du kiegst es langsam mit der Angst zu tun willst du gehen ? (ja/nein) ").lower()

                if choice4 == "ja":
                    print("Du verabschiedest dich und probierst so schnell wie möglich wegzurennen.")
                    print("Zu deiner verwunderung rennt er dir nicht hinterher sondern steht nur da und lacht.")
                    print("Du rennst den ganzen weg zurück und stehst wieder am anfang.")
                    return text_adventure_game(name)

                elif choice4 == "nein":
                    print("Trozdeiner Angst bleibst du.")
                    print("Du frägst langsam nach wer genau der Älteste ist und wer dieser Gott Cyric sein soll von dem du noch nie gehört has.t")
                    print("Der Älteste erklärt das er anführer eines gewissen stammes ist der die gnade von Cyric bekommen hat das is der grund warum er aussieht wie er aussieht.")
                    print("Er erklärt desweiteren das solange man erhlich ist keine probleme bekommt.")
                    print("Wie genau die Opferung doch aussieht behält er für sich.")
                    print("Er fragt dich ob du beitreten möchtest ?")

                    choice5 = input("Willst du beitreten oder ablenen ? (ja/nein) ").lower()

                    if choice5 == "ja":
                        print("Du sagst zu da es dich interessiert.")
                        print("Ein unfassbarer schmerz fährt durch dich,dein Körper verändert sich.")
                        print("Der Älteste lacht während du dich quallvoll zusammenrollst und schreist.")
                        print("als alles vorbei ist erklärt der Äöteste dir das du von nun an schwache menschen und Lügner jagen und fressen sollst.")
                        print("Als du dein Ausseres betrachtest fällt dir auf das du dich in ein Monster verwandelt hast.")
                        print("es fühlt sich auch so an als hättest du dich innerlich verändert.")
                        print("Nun bist du kein Abenteuerer mehr", name ,"von nun an bist du ein mitglied der gefolgschaft von Cyric!")
                        print("Du lebst von nun an dein leben als seltsames Wesen!")
                        return

                    elif choice5 == "nein":
                        print("Du lehnst ab sagt der Älteste sichtlich genervt.")
                        print("Er kommt immer näher auf dich zu.")
                        choice6 = input("Wegrennen oder nicht fragst du dich (wegrennen/bleiben) ")

                        if choice6 == "wegrennen":
                            print("Du rennst so schnell du kannst.")
                            print("nach einiger zeit bleibst du stehen und kuckst dich verwirrt um.")
                            print("Du hast den Wald leben verlassen.")
                            print("Ein stein fällt dir vom Herzen.")
                            print("Du entschließt dich von nun an dich vom Wald vernzuhalten und keine auftrage dort anzunehmen.")
                            print("Kaum zurück in der Gilde erzählst du allen was du erlebt hast doch du wirst nur ausgelacht.")
                            print("Das ist deine schockirende geschichte ",name, "Ob du dir das eingebildet hast oder nicht wer weiß.")

                        elif choice6 == "bleiben":
                            print("Du entschlißt dich zu bleiben und abzuwarten.")
                            print("Noch bevor du reagieren kannst kommen aus den dunkel schatten der umgebung"  
                                  " weitere gestalten die dem Ältesten ahneln")
                            print("Sie kommen immer naher als du dein schwert in panik ziehen willst")
                            print("fangen die gestalten zu lachen an über deine schwäche.")
                            print("Der Älteste erklärt dir das das als Kriegshandlung gewertet wird und lacht.")
                            print("Sie stehen mitlerweile direkt um dich herum und zereen dich auf den Opferaltar.")
                            print("sie fangen an dich zu zereisen und zu fressen.")
                            return

            elif choice3 == "nein":
                print("Du bedankst dich für die warnung und gehst zurück richtung startpunkt.")
                print("Das wesen ruft dir noch genervt nach etwas nach aber das verstehst du nichtmehr.")
                return text_adventure_game(name)

        elif choice2 == "lüge":
            print("Du lügst, das Wesen lacht.")
            print("Es verschlingt dich mit Haut und Haar.")
            print("Das letze was man hört sind deine schreie und das kanacken deiner brechenden knochen und das kichern von dem Wesen.")
            return

    elif choice1 == "verlassen":
        print("Du gehst zum Start punkt zurück.")
        return text_adventure_game(name)


#auf einen Baum klettern
def tree_climb(name):
    print("Du kletterst auf einen Baum und siehst Folgendes:")
    print("Eine Steinwand im Osten.")
    print("Eine Lichtung im Westen.")
    print("Mehr Wald im Norden.")
    print("Du kletterst wieder herunter.")
    return text_adventure_game(name)



def  choice_scene4(name):
        choice4 = input("Willst du den Schreien entgegenlaufen oder umdrehen? (entgegen/umdrehen) ").lower()

        if choice4 == "entgegen":
            print("Du rennst den Schreien entgegen.")
            print("Einige Kreaturen greifen eine Händler Karvana an!")

            choice5 = input("Willst du helfen gehen und die Monster bekämpfen? (ja/nein) ").lower()

            if choice5 == "ja":
                print("Du kämpfst gegen die Monster.")
                print("Du besiegst sie, bist aber verwundet.")
                print("Die Händler bieten dir an, dich als Dank in das nächste Dorf zu bringen.")
                choice6 = input("Willst du annehmen? (ja/nein) ")

                if choice6 == "ja":
                    print("Du bedankst dich und sagst zu.")
                    print("Sie bringen dich in das nächste Dorf.")
                    print("Dort wirst du verpflegt und überlebst.")
                    print("Das war das erste große Abenteuer der Legende", name)
                    return

                elif choice6 == "nein":
                    print("Aus Eitelkeit lehnst du ab.")
                    print("Du hast dich während des Kampfes verletzt.")
                    print("Die Verletzung ist ernster als erwartet.")
                    print("Kaum sind die Händler weg, kippst du aufgrund des Blutverlustes um.")
                    print("Du stirbst dumm aber edel, der Abenteurer", name,
                          "gestorben an deinen Verletzungen, immerhin hatest du noch etwas Gutes getan troz deiner Eitelkeit.")
                    return

            elif choice5 == "nein":
                print("Du kriegst es mit der Angst zu tun und rennst weg.")
                print("Du rennst einem seltsamen Wesen in die Arme.")
                print("Es fragt dich, warum du wegrennst, anstatt deinem Gleichgesinnten zu helfen.")

                choice7 = input("Lügst du aus Scham oder sagst du die Wahrheit? (wahrheit/lüge) ").lower()

                if choice7 == "wahrheit":
                    print("Das Wesen lacht und sagt, es erwartet sowieso nichts von Menschen.")
                    print("Das Wesen geht.")
                    print("Du überlebst, aber die Reue, nicht geholfen zu haben, treibt dich in den Wahnsinn.")
                    return

                elif choice7 == "lüge":
                    print("Das Wesen lacht.")
                    print("Bevor du noch fragen kannst, warum es lacht, dreht es sich schon um.")
                    print("Das letzte, was du siehst, ist ein großes Maul voller spitzer Zähne.")
                    print("Es verschlingt dich mit Haut und Haar.")
                    print("Man hört deine Schreie und das Knirschen deiner brechenden Knochen durch den ganzen Wald.")
                    return

def choice_scene5(name):
    print("Du siehst ein Goblin Dorf")
    print("Du wirst überascht und gesehen einer der Goblins fängt an zu schreien")

    choice5 = input("Du überlegst Wegrennen oder Kämpfen (wegrennen/kämpfen) ").lower()

    if choice5 == "wegrennen":
        print("Du hast dich für wegrennen entscheiden")
        print("Du rennst so schnell du kannst")
        print("Aber die Goblins haben scheinbar Wölfe gezähmt")
        print("Ein Pfeil durchbohrt dein Bein,du fällst zu Boden")
        print("Die Goblins holen dich ein")

        choice6=input("willst du weiter wegrennen oder kämpfen (wegrennen/kämpfen)").lower()

        if choice6 == "wegrennen":
            print("Du probierst aufzustehen und schaffst es")
            print("Du probierst weg zu humpeln doch wirst von einem 2 pfeil durchbohrt und fällst zu boden")
            print("Während du blutend am Boden liegst hörst du die Goblins lachen")
            print("Sie lachen dich aus wie du verzweifelst probierst wegzukommen und stechen immer heufiger in deinen Rücken")
            print("Du stierbst Quallvoll durch die ganzen einstiche in deinem Rücken")
            print("So endet dein Weg mutiger Abendteuerer",name)
            return

        elif choice6 == "kampfen":
            print("Du ziehst dein Schwert und erschlägst so viele wie du kannst.")
            print("Du hast alle die dich verfolgten getötet aber wurdest verletzt.")
            print("Du wirst unmächtig.")
            print("Als du aufwachst realisirst du das du nicht mehr im Wald bist.")
            print("Eine Abenteuergruppe hat dich schienbar gefunden und in die staat gebracht.")
            print("Du bedankst dich")

            choice7=input("Willst du uns nicht beitreten? Frägt die Gruppe dich (annehmen/ablenen) ").lower()

            if choice7 == "annehmen":
                print("Du trittst der Gruppe bei")
                print("Ihr geht auf viele gemeinse abenteuer")
                print("So begann die geschichte der berühmten Abenteuergruppe von",name)

            elif choice7 == "ablenen":
                print("Du lehnst ab mit der begründung das du als Abenteurer aufhören willst")
                print("Das Goblindorf hat dir ein Trauma verpasst")
                print("Das war das erste und letze Abendteuer von",name)
                print(name,"ist mitlerweile ein Glücklicher Bürger der statt und hilft aus wo er kann")
                return

    elif choice5 == "kämpfen":
        print("Du kampfst und schwingst dein Schwert")
        print("Doch es sind zu viele du bist am ende deiner Kraft")
        print("Ihre überzahl überweltigt dich")
        print("Du gehst in den ganzen grünen Körpfern unter")
        print("Die letzen worte von dir sind nur wie konnte das passieren")
        print("Das is das ende des Abenteuers",name)
        return


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










