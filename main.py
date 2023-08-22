import classes


def docstring():
    """
    Οι κλάσεις που έχουν υλοποιηθεί είναι οι εξής:
        -class Player
        -class Computer
        -class Human
        -class SakClass
        -class Statistics

        Σχετικά με την κληρονομηκότητα ως κλάση γονέας έχω υλοποιείσει την κλάση Player και την κληρονομούν οι κλάσεις
        Human Και Computer. Οι μέθοδοι που χρησιμοποιούν οι κλάσεις που κληρονομούν αφορούν το score ,δηλαδή τους
        πόντους τόσο του παίχτη όσο και του υπολογιστή και την λέξη που επιλέγει να παίζει ο υπολογιστής και ο
        άνθρωπος. Τα παραπάνω αποτελούν κοινα χαρακτηριστικά και για αυτό χρησιμοποιήθηκε η κληρονομικότητα. Οι
        μέθοδοι που έχουν χρησιμοποιηθεί είναι:set_score , get_score, set_word,get_word  και αποτελούν setters και
        getters  για την αποθήκευση και την επικοινωνία της κλάσεις με το υπόλοιπο πρόγραμμα.

        Το πρόγραμμα οργανώνεται με την χρήση λεξικών τα οποία αρχικοποιούνται και επεξεργάζονται καθ' ολη την διάρκεια
        της εκτέλεσης του προγράμματος στην κλάση SakClass. Στην συγκεκριμένη κλάση έχουμε υλοποιέισει το λεξικό words το
        οποίο περιέχει όλες τις λέξεις το αρχειου greek7, λεξικό letters που περιέχει ένα κλειδί (το γράμμα) και στο
        δεύτερο σκέλος μία λίστα με την ποσότητα του γραμματος και την βαθμολογία του κάθε γράμματος.
        Σχετικά με τις μεθόδους της συγκεκριμένης κλάσης αναφέρονται οι πιο σημαντικές:
            -give_letters δέχεται ως όρισμα τα εναπομείναντα γράμματα letters και επιστρέφει τα γράμματα που δόθηκαν και
                κάποια επιπλέον διαφορετικά μέχτι να φτάσουν την ποσότητα 7
            -check_letters δέχεται ως όρσιματα μία λέξη και τα γράμματα που αναφέραμε παραπάνω. Στην συνέχει ελέγχει αν
                ολα τα γράμματα της λέξης υπαρχουν στην συνέχεια τα αφαιρεί και επιστρέφει True αν η λέξη μπορεί να
                σχηματιστεί με τα δοθέντα γράμματα αλλιώς False.
            -word_search δέχεται ως όρισμα μία λέξη και ελέγχει στο αρχείο αν η δοθέντα λέξη υπάρχει. Αν υπάρχει
                επιστρέφει True αλλίως επιστρέφει False.
            -count_points υπολογίζει τους πόντους μίας λέξης
            -find_max_points δέχεται μία λίστα με όλες τις πιθανές λέξεις απο 7 συγκεκριμένα γράμματα και βρίσκει αυτη
                με την μεγαλύτερη αξίας σε πόντους και την επιστρέφει

        Ο αλγόριθος που υλοποιήθηκε για την περίπτωση του υπολογιστή είναι ο Smart Teach. Συγκεκριμένα υλοποιήθηκε στην
        κλάση Computer  και στην μέθοδο smart επιστρέφοντας μία λίστα με τις πιθανές λέξεις.Σχετικά με την επιλογή της
        λέξης η μέθοδος που επιλέγει την λέξη με τους περισσότερους πόντους είναι η find_max_points Που τις λειτουργίες
        της τις αναλύσαμε παραπάνω. Για την επιλογη των δύο καλύτερων λέξεων με τα γράμματα του παίχτη χρησιμοποιήσαμε
        την find_max_2_points που επιστρέφει τις 2 λέξεις με τους περισσότερους πόντους και τις εμφανίζει με σχετικό
        μήνυμα

        Το κύριο μέρος του προγράμματος υλοποιείται με την βοήθεια της μεθόδους game όπου εκεί γίνονται οι κινήσεις και
        απο τον πάιχτη και απο τον υπολογιστή.Τα στατιστικά επίσης των παιχτών αποθηκεύονται σε ένα αρχείο και όταν τους
        ζητηθεί εμφανίζονται σε αριθμημένη κατάταξη απο το μεγαλύτερο στο μικρότερο σκορ.Οι παίχτες που αποθηκεύονται
        είναι αυτοί που έχουν επιλέξει τον τερματισμό του παιχνιδιού.
    """


def game(stats):
    sak = classes.SakClass()
    player1 = classes.Human()

    computer = classes.Computer()
    player1.set_name()
    computer_points = 0
    while not stats.unique_username(player1.get_name()):
        player1.set_name()
    turn = True  # true when is PLAYER'S turn false when its COMPUTER'S turn
    player1.set_letters(sak.give_letters(player1.get_letters()))
    while player1.get_word() != 'Q':
        if turn:
            print(str(player1.get_letters()) + " γράμματα παίχτη")
            player1.set_word()

            while not sak.is_greek(player1.get_word()) and player1.get_word() != 'Q':
                print("Παρακαλώ εισάγετε ελληνική λέξη:")
                player1.set_word()

            tmp_comp = computer.smart(sak.get_words(), player1.get_letters())

            if sak.check_letters(player1.get_word(), player1.get_letters()):
                if sak.word_search(player1.get_word()):
                    player1.set_score(sak.count_points(player1.get_word()))
                    word_max1, word_max2 = sak.find_max_2_points(tmp_comp)
                    print("Οι λέξεις που ο υπολογιστής βρήκε και έχουν την καλύτερη βαθμολογία είναι:" + str(
                        word_max1) + "  " + str(word_max2))
            player1.set_letters(sak.give_letters(player1.get_letters()))
            turn = False
        else:
            computer.set_letters(sak.give_letters(computer.get_letters()))
            print(str(computer.get_letters()) + " γράμματα υπολογιστή")
            tmp1 = computer.smart(sak.get_words(), computer.get_letters())
            max_word, max = sak.find_max_points(tmp1)
            sak.check_letters(max_word, computer.get_letters())
            sak.give_letters(computer.get_letters())
            print("Ο υπολογιστής επέλεξε την λέξη " + max_word + " η οποία παίρνει " + str(max) + " πόντους.")
            computer_points += max
            turn = True
        print("compputer " + str(computer_points) + " human " + str(player1.get_score()))
        print("")
    stats.add_element(player1.get_name(), player1.get_score())


def menu():
    print("***** SCRABBLE *****")
    print("1:Παιχνίδι")
    print("2:Ρυθμίσεις")
    print("3:Στατιστικα παιχτων")
    print("q:Εξοδος")


def main():
    stats = classes.Statistics()
    action = "random"
    while action != 'q':
        menu()
        action = input("Επιλέξτε μία απο τις παραπάνω επιλογές:")
        while action != '1' and action != '2' and action != '3' and action != 'q':
            if action == '4':
                print("Για έξοδο δοκιμάστε να πληκτρολογίσετε q.")
            action = input("Εισάγετε έγκυρη είσοδο:")
        if action == '1':
            game(stats)
        else:
            if action == '2':
                print("Το παιχνίδι έχει δημιουργηθεί ώστε ο αλγόριθμος του υπολογιστή να παίζει με SMART TEACH.")
                print("")
            else:
                if action == '3':
                    stats.print_stats()
                else:
                    print("Τέλος παιχνιδιού")

    #

    #

    # stats.add_element(player1.get_name(), player1.get_score())
    # stats.print_stats()


main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
