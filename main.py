#text_adventure_game
class Game:
    def __init__(self):
        self.player_name = None

    #gegen falsche eingaben
    def wrong_input(self, prompt, options):
        while True:
            choice = input(prompt).lower()
            if choice in options:
                return choice
            else:
                print("Du kannst nur eine der Möglichkeiten eingeben! Bitte wähle erneut.")

    #menü
    def menu(self):
        choice = None
        while choice not in ["1","2","3"]:
            print(" 1 : Benenne deinen Abenteurer")
            print(" 2 : Spielen")
            print(" 3 : Beenden")
            choice = input("Wähle eine Option: ")
            print("Du hast gewählt:", choice)
            if choice not in ["1","2","3"]:

                print("Ungültige Option, bitte erneut zwischen 1,2,3 wählen.")
        return choice

    #namen machen
    def set_heroname(self):
        self.player_name = input("Name: ")
        print("Willkommen zu deinem Abenteuer", self.player_name)
        print("Viel Erfolg, junger Abenteurer!")

    #spielstart
    def start_game(self):
        while True:
            print("Du bist im Wald,", self.player_name)
            choice = self.wrong_input(
                "Wo willst du hin? (norden/osten/süden/westen/baum) ",["norden", "osten", "süden", "westen", "baum"]).lower()
            if choice == "norden":
                self.north()
            elif choice == "osten":
                self.east()
            elif choice == "süden":
                self.south()
            elif choice == "westen":
                self.west()
            elif choice == "baum":
                self.tree_climb()
            else:
                print("Ungültige Richtung!")

    #Game over Funktion
    def game_over(self, text="Du bist gestorben"):
        print("\n" + text)
        print("GAME OVER")
        self.end()

    #Ende Neustart
    def end(self):
        choice = self.wrong_input("Willst du neu anfangen? (ja/nein) ", ["ja", "nein"])
        if choice == "ja":
            self.set_heroname()
            self.start_game()
        else:
            print("Danke fürs Spielen")
            exit()

#verschiedene Szenen
#Richtung norden
    def north(self):
        print("Du gehst nach Norden, der Wald wird dunkler.")

        choice1 = self.wrong_input("Willst du weitergehen? (ja/nein) ", ["ja","nein"])

        if choice1 == "ja":
            print(self.player_name, "du hörst eine Stimme rufen.")

            choice2 = self.wrong_input("Willst du zurückrufen oder umkehren? (zurückrufen/umkehren) ", ["(zurückrufen","umkehren"])

            if choice2 == "zurückrufen":
                print("Du versuchst mit der Stimme zu reden.")

                choice3 = self.wrong_input("Willst du deinen wahren Namen sagen? (ja/nein) ", ["ja","nein"])

                if choice3 == "ja":
                    print("Du sagst zögernd", self.player_name)
                    print("Das Wesen wirkt genervt: 'Hier ist es gefährlich, du solltest umkehren.'")

                    choice4 = self.wrong_input("Willst du auf den Rat hören? (ja/nein) ", ["ja","nein"])

                    if choice4 == "ja":
                        print("Du kehrst um und landest wieder am Startpunkt.")
                        self.start_game()

                    elif choice4 == "nein":
                        print("Du gehst tiefer in den dunklen Wald hinein.")
                        print("Das seltsame Wesen steht hinter dir und lacht.")
                        print("Es verschlingt dich mit Haut und Haar.")
                        print("Das letzte, was man hört, sind deine Schreie und das Knacken deiner brechenden Knochen und das Lachen des Wesens.")
                        print("Das war das grausame Ende von", self.player_name)
                        self.game_over(f"{self.player_name} wurde von dem Wesen gefressen.")

                elif choice3 == "nein":
                    print("'Du lügst': sagt das Wesen und lacht.")
                    print("Es verschlingt dich mit Haut und Haar.")
                    print("Das letzte was man hört sind deine schreie und das Knacken deiner brechenden knochen und das kichern von dem Wesen.")
                    self.game_over(f"{self.player_name} wurde von dem Wesen gefressen.")

            elif choice2 == "umkehren":
                print("Du kehrst um und landest wieder am Startpunkt.")
                self.start_game()

        elif choice1 == "nein":
            print("Du kehrst um und läufst zurück zum Start.")
            self.start_game()

#Richtung Osten
    def east(self):
        print("Du stehst vor einer Steinwand mit seltsamen Zeichen darauf.")
        print("Es sieht so aus, als ob ein seltsames Monster umherläuft.")
        print("Darunter steht in Blut geschrieben: 'Sag die Wahrheit.'")
        print("Du machst dir nicht wirklich Gedanken darum.")

        choice1 = self.wrong_input("Willst du weiter Richtung Osten laufen? (ja/nein) ", ["ja","nein"])

        if choice1 == "ja":
            print("Du läufst weiter Richtung Osten und findest eine Truhe.")

            choice2 = self.wrong_input("Willst du die Truhe öffnen? (ja/nein) ", ["ja","nein"])

            if choice2 == "ja":
                print("Du öffnest die Truhe.")
                print("Es ist eine Mimik!")
                print("Die Mimik frisst dich qualvoll auf.")
                print("Der junge Abenteurer", self.player_name, "starb voller Reue wegen Gier.")
                self.game_over(f"{self.player_name} wurde von einer Mimik gefressen.")

            elif choice2 == "nein":
                print("Du ignorierst die Truhe und hörst Schreie.")
                self.choice_scene4()

        elif choice1 == "nein":
            print("Du willst umkehren, doch du hörst Schreie aus Richtung Osten.")
            self.choice_scene4()


#Richtung Süden
    def south(self):
        print("Du hörst komische Geräusche.")

        choice1 =self.wrong_input("Willst du in das Gebüsch zu den Geräuschen gehen? (ja/nein) ", ["ja","nein"])

        if choice1 == "ja":
            print("Du gehst zögerlich zum Gebüsch.")
            print("Du atmest erleichtert auf, es ist nur ein kleines Kätzchen.")

            choice2 = self.wrong_input("Willst du das Kätzchen streicheln (ja/nein) ", ["ja","nein"])

            if choice2 == "ja":
                print("Du streckst deine Hand aus um das Kätzchen zu streicheln.")
                print("Plötzlich beißt das Kätzchen zu und rennt weg.")
                print("Hinter dir steht ein Goblin und schlägt dir mit der Keule auf den Kopf.")
                print("Du stirbst einen langsamen erniedrigend Tod.")
                print("Ein Abenteurer sollte immer achtsam sein",self.player_name)
                self.game_over(f"{self.player_name}Wurde von Goblin erschlagen.")

            elif choice2 == "nein":
                print("Du bemerkst eine Bewegung hinter dir.")
                print("Es ist ein Goblin.")
                print("Du erschlägst ihn.")
                print("Du läufst in die Richtung wo er herkam.")
                self.choice_scene5()

        elif choice1 == "nein":
            print("Du drehst dich von dem gebüsch weg und läufst zögerlich weiter.")
            self.choice_scene5()

# Richtung Westen
    def west(self):
        print("Du siehst eine Lichtung.")
        print("In dieser Lichtung findest du viele Fußspuren sowie Klauenabdrücke.")
        print("Inmitten der Lichtung ist ein blutverschmierter Stein. Es sieht aus wie ein Opferaltar.")

        choice1 = self.wrong_input("Willst du dich ihm nähern oder die lichtung verlassen ? (nähern/verlassen).", ["nähern","verlassen"])

        if choice1 == "nähern":
            print("Du näherst dich dem Opferaltar.")
            print("Du hörst eine Stimme hinter dir,sie kichert.")
            print("Eine Stimme flüstert: 'Was tust du hier?'")

            choice2 = self.wrong_input("Du überlegst solltest du die Wahrheit sagen oder Lügen ? (wahrheit/lüge) ", ["wahrheit","lüge"])

            if choice2 == "wahrheit":
                print("Du fragst: 'Wer ist da?'")
                print("Du sagst: 'Ich habe mich verlaufen.'")
                print("Aus dem dunkeln tritt eine seltsames Wesen vor.")
                print("Es stellt sich vor als Ältester und erklärt das es hier gefährlich sei.")

                choice3 = self.wrong_input("Willst du es auf den altar ansprechen ? (ja/nein) ", ["ja","nein"])

                if choice3 == "ja":
                    print("Du sprichst das Wesen das sich Ältester nennt auf den Blutigenaltar an.")
                    print("Das Wesen kichert nur und sagt das das Opfer für den Gott Cyric er wird hier angebetet.")
                    print("Du überlegst ob es sich um einen Kult handeln könnte.")
                    print("Du frägst nach ob es sich dabei um menschliche opfer handelt.")
                    print("Der älteste sagt nur lachend :'mal so mal so auf jeden fall sind es immer Lügner.'")

                    choice4 = self.wrong_input("Du kriegst es langsam mit der Angst zu tun willst du gehen ? (ja/nein) ", ["ja","nein"])

                    if choice4 == "ja":
                        print("Du verabschiedest dich und probierst so schnell wie möglich wegzurennen.")
                        print("Zu deiner verwunderung rennt er dir nicht hinterher sondern steht nur da und lacht.")
                        print("Du rennst den ganzen weg zurück und stehst wieder am anfang.")
                        self.start_game()

                    elif choice4 == "nein":
                        print("Trotz deiner Angst bleibst du.")
                        print("Du frägst langsam nach wer genau der Älteste ist und wer dieser Gott Cyric sein soll von dem du noch nie gehört hast")
                        print("Der Älteste erklärt das er Anführer eines gewissen Stammes ist der die Gnade von Cyric bekommen hat das ist der grund warum er aussieht wie er aussieht.")
                        print("Er erklärt des weiteren das solange man ehrlich ist keine Probleme bekommt.")
                        print("Wie genau die Opferung doch aussieht behält er für sich.")
                        print("Er fragt dich ob du beitreten möchtest ?")

                        choice5 = self.wrong_input("Willst du beitreten oder ablehnen ? (ja/nein) ", ["ja","nein"])

                        if choice5 == "ja":
                            print("Du sagst zu da es dich interessiert.")
                            print("Ein unfassbarer schmerz fährt durch dich,dein Körper verändert sich.")
                            print("Der Älteste lacht während du dich qualvoll zusammenrollst und schreist.")
                            print("als alles vorbei ist erklärt der Älteste dir das du von nun an schwache menschen und Lügner jagen und fressen sollst.")
                            print("Als du dein Äußeres betrachtest fällt dir auf das du dich in ein Monster verwandelt hast.")
                            print("es fühlt sich auch so an als hättest du dich innerlich verändert.")
                            print("du bist nun zufriedener ,erfüllter ,hungriger nach fleisch")
                            print("Nun bist du kein Abenteurer mehr", self.player_name ,"von nun an bist du ein Mitglied der Gefolgschaft von Cyric!")
                            print("Du lebst von nun an dein leben als seltsames Wesen! Und streifst durch die Wälder")
                            self.game_over(f"{self.player_name} lebt von nun an als seltsames Wesen")

                        elif choice5 == "nein":
                            print("Du lehnst ab sagt der Älteste sichtlich genervt.")
                            print("Er kommt immer näher auf dich zu.")

                            choice6 = self.wrong_input("Wegrennen oder nicht fragst du dich (wegrennen/bleiben) ")

                            if choice6 == "wegrennen":
                                print("Du rennst so schnell du kannst.")
                                print("nach einiger zeit bleibst du stehen und kuckst dich verwirrt um.")
                                print("Du hast den Wald leben verlassen.")
                                print("Ein stein fällt dir vom Herzen.")
                                print("Du entschließt dich von nun an dich vom Wald fernzuhalten und keine auftrage dort anzunehmen.")
                                print("Kaum zurück in der Gilde erzählst du allen was du erlebt hast doch du wirst nur ausgelacht.")
                                print("Das ist deine schockierende Geschichte ",self.player_name, "Ob du dir das eingebildet hast oder nicht.")
                                self.game_over(f"{self.player_name} hat fürs leben einen schock erlitten nichtmal{self.player_name} weis noch was war ist")

                            elif choice6 == "bleiben":
                                print("Du entschließt dich zu bleiben und abzuwarten.")
                                print("Noch bevor du reagieren kannst kommen aus den dunkel schatten der umgebung"  
                                      " weitere gestalten die dem Ältesten ähneln")
                                print("Sie kommen immer näher als du dein schwert in panik ziehen willst")
                                print("fangen die gestalten zu lachen an über deine schwäche.")
                                print("Der Älteste erklärt dir das das als Kriegshandlung gewertet wird und lacht.")
                                print("Sie stehen mittlerweile direkt um dich herum und zerren dich auf den Opferaltar.")
                                print("sie fangen an dich zu zerreißen und zu fressen.")
                                self.game_over(f"{self.player_name} wurde von den Anhängern zerreißen und gefressen")

                elif choice3 == "nein":
                    print("Du bedankst dich für die warnung und gehst zurück richtung startpunkt.")
                    print("Das wesen ruft dir noch genervt nach etwas nach aber das verstehst du nicht mehr.")
                    self.start_game()

            elif choice2 == "lüge":
                print("'Du lügst, sagt das Wesen und lacht.")
                print("Es verschlingt dich mit Haut und Haar.")
                print("Das letzte was man hört sind deine schreie und das kanaken deiner brechenden Knochen und das kichern von dem Wesen.")
                self.game_over(f"{self.player_name} wurde von dem seltsamen Wesen gefressen")

        elif choice1 == "verlassen":
            print("Du gehst zum Start punkt zurück.")
            self.start_game()


#auf einen Baum klettern
    def tree_climb(self):
        print("Du kletterst auf einen Baum und siehst Folgendes:")
        print("Eine Steinwand im Osten.")
        print("Eine Lichtung im Westen.")
        print("Mehr Wald im Norden.")

        choice1 = self.wrong_input("Willst du Herunterklettern ? (runterklettern/bleiben) ", ["runterklettern","bleiben"])

        if choice1 == "runterklettern":
            print("Du kletterst wieder herunter.")
            self.start_game()

        elif choice1 == "bleiben":
            print("Du bleibst auf dem Baum")
            self.tree_climb()



    def  choice_scene4(self):
        print("Du hörst Schreie aus der Ferne.")
        choice1 = self.wrong_input("Willst du den Schreien entgegenlaufen oder umdrehen? (entgegen/umdrehen) ", ["entgegen","umdrehen"])

        if choice1 == "entgegen":
            print("Du rennst den Schreien entgegen.")
            print("Einige Kreaturen greifen eine Händler Karawane an!")

            choice2 = self.wrong_input("Willst du helfen gehen und die Monster bekämpfen? (ja/nein) ", ["ja","nein"])

            if choice2 == "ja":
                print("Du kämpfst gegen die Monster.")
                print("Du besiegst sie, bist aber verwundet.")
                print("Die Händler bieten dir an, dich als Dank in das nächste Dorf zu bringen.")

                choice3 = self.wrong_input("Willst du annehmen? (ja/nein) ", ["ja","nein"])

                if choice3 == "ja":
                    print("Du bedankst dich und sagst zu.")
                    print("Sie bringen dich in das nächste Dorf.")
                    print("Dort wirst du verpflegt und überlebst.")
                    print("Das war das erste große Abenteuer der Legende", self.player_name)
                    self.game_over(f"{self.player_name}wird noch auf viele Abenteuer gehen")

                elif choice3 == "nein":
                    print("Aus Eitelkeit lehnst du ab.")
                    print("Du hattest dich während des Kampfes verletzt.")
                    print("Die Verletzung ist ernster als erwartet.")
                    print("Kaum sind die Händler weg, kippst du aufgrund des Blutverlustes um.")
                    print("Du stirbst dumm aber edel, der Abenteurer", self.player_name,
                          "gestorben an deinen Verletzungen, immerhin hatest du noch etwas Gutes getan trotz deiner Eitelkeit.")
                    self.game_over(f"{self.player_name} starb")

            elif choice2 == "nein":
                print("Du kriegst es mit der Angst zu tun und rennst weg.")
                print("Du rennst einem seltsamen Wesen in die Arme.")
                print("Es fragt dich, warum du wegrennst, anstatt deinem Gleichgesinnten zu helfen.")

                choice4 = self.wrong_input("Lügst du aus Scham oder sagst du die Wahrheit? (wahrheit/lüge) ", ["wahrheit","lüge"])

                if choice4 == "wahrheit":
                    print("Das Wesen lacht und sagt, es erwartet sowieso nichts von Menschen.")
                    print("Das Wesen geht.")
                    print("Du überlebst, aber die Reue, nicht geholfen zu haben, treibt dich in den Wahnsinn.")
                    self.game_over(f"{self.player_name} verfällt dem Wahnsinn")

                elif choice4 == "lüge":
                    print("Das Wesen lacht.")
                    print("Bevor du noch fragen kannst, warum es lacht, dreht es sich schon um.")
                    print("Das letzte, was du siehst, ist ein großes Maul voller spitzer Zähne.")
                    print("Es verschlingt dich mit Haut und Haar.")
                    print("Man hört deine Schreie und das Knirschen deiner brechenden Knochen durch den ganzen Wald.")
                    self.game_over(f"{self.player_name} wurde von einem seltsamen Wesen gefressen ")

        elif choice1 == "umdrehen":
            print("Du entscheidest dich umzudrehen und kehrst vorsichtig zum Startpunkt zurück.")
            self.start_game()

    def choice_scene5(self):
        print("Du siehst ein Goblin Dorf")
        print("Du wirst überrascht und gesehen einer der Goblins fängt an zu schreien")

        choice1 = self.wrong_input("Du überlegst Wegrennen oder Kämpfen (wegrennen/kämpfen) ", ["wegrennen","kämpfen"])

        if choice1 == "wegrennen":
            print("Du hast dich für wegrennen entscheiden")
            print("Du rennst so schnell du kannst")
            print("Aber die Goblins haben scheinbar Wölfe gezähmt")
            print("Ein Pfeil durchbohrt dein Bein,du fällst zu Boden")
            print("Die Goblins holen dich ein")

            choice2 = self.wrong_input("willst du weiter wegrennen oder kämpfen (wegrennen/kämpfen)", ["wegrennen","kämpfen"])

            if choice2 == "wegrennen":
                print("Du probierst aufzustehen und schaffst es")
                print("Du probierst weg zu humpeln doch wirst von einem zweiter Pfeil durchbohrt und fällst zu boden")
                print("Während du blutend am Boden liegst hörst du die Goblins lachen")
                print("Sie lachen dich aus wie du verzweifelst probierst wegzukommen und stechen immer häufiger in deinen Rücken")
                print("Du stirbst qualvoll  durch die ganzen Einstiche in deinem Rücken")
                print("So endet dein Weg mutiger Abenteurer",self.player_name)
                self.game_over(f"{self.player_name} ist qualvoll verblutet")

            elif choice2 == "kämpfen":
                print("Du ziehst dein Schwert und erschlägst so viele wie du kannst.")
                print("Du hast alle die dich verfolgten getötet aber wurdest verletzt.")
                print("Du wirst ohnmächtig.")
                print("Als du aufwachst realisierst du das du nicht mehr im Wald bist.")
                print("Eine Abenteuergruppe hat dich scheinbar gefunden und in die Stadt gebracht.")
                print("Du bedankst dich")

                choice3 = self.wrong_input("Willst du uns nicht beitreten? Frägt die Gruppe dich (annehmen/ablehnen) ", ["annehmen","ablehnen"])

                if choice3 == "annehmen":
                    print("Du trittst der Gruppe bei")
                    print("Ihr geht auf viele gemeinsame Abenteuer")
                    print("So begann die geschichte der berühmten Abenteuergruppe von",self.player_name)
                    self.game_over(f"{self.player_name} ging mit seinen neuen Kameraden noch auf viele Reisen")

                elif choice3 == "ablehnen":
                    print("Du lehnst ab mit der begründung das du als Abenteurer aufhören willst")
                    print("Das Goblindorf hat dir ein Trauma verpasst")
                    print("Das war das erste und letzte Abenteuer von",self.player_name)
                    print(self.player_name,"ist mittlerweile ein Glücklicher Bürger der stadt und hilft aus wo er kann")
                    self.game_over(f"{self.player_name} lebte glücklich bis ans ende seiner tage in der Stadt")

        elif choice1 == "kämpfen":
            print("Du kämpfst und schwingst dein Schwert")
            print("Doch es sind zu viele du bist am Ende deiner Kraft")
            print("Ihre überzahl überwältigt  dich")
            print("Du gehst in den ganzen grünen Körpern unter")
            print("Die letzten worte von dir sind nur:'wie konnte das passieren?'")
            self.game_over(f"Das ist das ende des Abenteuers{self.player_name}")

#menü ausgabe was passieren soll
game = Game()

while True:
    choice = game.menu()

    match choice:
        case "1":
            game.set_heroname()
        case "2":
            if game.player_name is None:
                print("Bitte Namen wählen")
            else:
                game.start_game()
        case "3":
            break