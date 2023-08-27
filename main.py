a, b, menu = 0, 0, -1

#można się zastanowić jak wykonać program, by działał do momentu, gdy użytkownik wybierze odpowiednią opcję menu
#innymi słowy - program będzie w stałej pętli
print("Prosty kalkulator\nMenu programu:\n1. Dodawanie\n2.Odejmowanie") #tutaj trzeba dopisać kolejne opcje menu
#bądź dokonać tego w nowym print
menu = int(input("Wybrana opcja: "))
if (menu > 0 and menu < 3): #tutaj trzeba dostosować warunek do nowych elementów menu
    a = float(input("Podaj wartość a: "))
    b = float(input("Podaj wartość b: "))
    match(menu):
        case 1:
            print("Suma wartości", a, "i", b, "wynosi", a+b)
        case 2:
            print("Różnica wartości", a, "i", b, "wynosi", a-b)
        #tutaj nalezy dodac kolejne operacje arytmetyczne (+,-,*,/,//,**,%)
        #trzeba pamiętać o wyjątkach!
else:
    print("Wybrano opcję spoza menu")

print("Program się zakończył")