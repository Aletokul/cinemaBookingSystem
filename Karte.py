import matplotlib.pyplot as plt

def ceneZlatni():
    fajl = open("karteZlatni.txt", "r")
    f = int(fajl.read())
    print("Slobodno je ", f, "mesta.")
    cena = 450
    print("Cena karte za odabrani film iznosi 450 dinara.")
    kupi = eval(input("Unesite broj karata: "))
    suma = 0
    if kupi in range(f + 1):
        cena *= kupi
        suma += kupi
        fajl = open('prodateZlatni.txt', 'a')
        fajl.write(str(suma))
        fajl.write("\n")
        print("Vas racun iznosi: ",cena ,"dinara")
        f = f - kupi
        fajl = open("karteZlatni.txt", "w")
        f = fajl.write(str(f))
        
    else:
        print("Uneli ste vise karata nego sto je dostupno.")
        
    
def ceneKnives():
    fajl = open("karteKnives.txt", "r")
    f = int(fajl.read())
    print("Slobodno je ", f, "mesta.")
    cena = 500
    print("Cena karte za odabrani film iznosi 500 dinara.")
    kupi = eval(input("Unesite broj karata: "))
    suma = 0
    if kupi in range(f + 1):
        cena *= kupi
        suma += kupi
        fajl = open('prodateKnives.txt', 'a')
        fajl.write(str(suma))
        fajl.write("\n")
        print("Vas racun iznosi: ",cena ,"dinara")
        f = f - kupi
        fajl = open("karteKnives.txt", "w")
        f = fajl.write(str(f))
        
    else:
        print("Uneli ste vise karata nego sto je dostupno.")
        
        
def ceneWrong():
    fajl = open("karteWrong.txt", "r")
    f = int(fajl.read())
    print("Slobodno je ", f, "mesta.")
    cena = 400
    print("Cena karte za odabrani film iznosi 400 dinara.")
    kupi = eval(input("Unesite broj karata: "))
    suma = 0
    if kupi in range(f + 1):
        cena *= kupi
        suma += kupi
        fajl = open('prodateWrong.txt', 'a')
        fajl.write(str(suma))
        fajl.write("\n")
        print("Vas racun iznosi: ",cena ,"dinara")
        f = f - kupi
        fajl = open("karteWrong.txt", "w")
        f = fajl.write(str(f))
        
    else:
        print("Uneli ste vise karata nego sto je dostupno.")
        
        
def ceneScream():
    fajl = open("karteScream.txt", "r")
    f = int(fajl.read())
    print("Slobodno je ", f, "mesta.")
    cena = 500
    print("Cena karte za odabrani film iznosi 500 dinara.")
    kupi = eval(input("Unesite broj karata: "))
    suma = 0
    if kupi in range(f + 1):
        cena *= kupi
        suma += kupi
        fajl = open('prodateScream.txt', 'a')
        fajl.write(str(suma))
        fajl.write("\n")
        print("Vas racun iznosi: ",cena ,"dinara")
        f = f - kupi
        fajl = open("karteScream.txt", "w")
        f = fajl.write(str(f))
        
    else:
        print("Uneli ste vise karata nego sto je dostupno.")
        
        
def ceneAjfel():
    fajl = open("karteAjfel.txt", "r")
    f = int(fajl.read())
    print("Slobodno je ", f, "mesta.")
    cena = 450
    print("Cena karte za odabrani film iznosi 450 dinara.")
    kupi = eval(input("Unesite broj karata: "))
    suma = 0
    if kupi in range(f + 1):
        cena *= kupi
        suma += kupi
        fajl = open("prodateAjfel.txt", "a")
        fajl.write(str(suma))
        fajl.write("\n")
        print("Vas racun iznosi: ",cena ,"dinara")
        f = f - kupi
        fajl = open("karteAjfel.txt", "w")
        f = fajl.write(str(f))
        
    else:
        print("Uneli ste vise karata nego sto je dostupno.")

def ukupnaCena():
    ukupnoZ = 0

    with open('prodateZlatni.txt', 'r') as ulaz, open('karte.txt', 'w') as izlaz:
        for line in ulaz:
            try:
                broj = int(line)
                ukupnoZ += broj
                izlaz.write(line)
            except ValueError:
                print('{} Nije broj!'.format(line))
    
    print('Broj prodatih karata za film Zlatni decko: {}'.format(ukupnoZ))
    
    ukupnoK = 0

    with open('prodateKnives.txt', 'r') as ulaz, open('karte.txt', 'w') as izlaz:
        for line in ulaz:
            try:
                broj =int(line)
                ukupnoK += broj
                izlaz.write(line)
            except ValueError:
                print('{} Nije broj!'.format(line))
    
    print('Broj prodatih karata za film Knives out: {}'.format(ukupnoK))
    
    ukupnoW = 0

    with open('prodateWrong.txt', 'r') as ulaz, open('karte.txt', 'w') as izlaz:
        for line in ulaz:
            try:
                broj = int(line)
                ukupnoW += broj
                izlaz.write(line)
            except ValueError:
                print('{} Nije broj!'.format(line))
    
    print('Broj prodatih karata za film Wrong turn: {}'.format(ukupnoW))
    
    ukupnoS = 0

    with open('prodateScream.txt', 'r') as ulaz, open('karte.txt', 'w') as izlaz:
        for line in ulaz:
            try:
                broj = int(line)
                ukupnoS += broj
                izlaz.write(line)
            except ValueError:
                print('{} Nije broj!'.format(line))
    
    print('Broj prodatih karata za film Scream: {}'.format(ukupnoS))
    
    ukupnoA = 0

    with open('prodateAjfel.txt', 'r') as ulaz, open('karte.txt', 'w') as izlaz:
        for line in ulaz:
            try:
                broj = int(line)
                ukupnoA += broj
                izlaz.write(line)
            except ValueError:
                print('{} Nije broj!'.format(line))
    
    print('Broj prodatih karata za film Ajfel: {}'.format(ukupnoA))
    
    ukupno = ukupnoZ+ukupnoK+ukupnoW+ukupnoS+ukupnoA
    print("Ukupan broj karata: ", ukupno)
    fajl = open("karte.txt", "w")
    fajl.write(str(ukupno))
    
    x = ["Ukupno", "Zlatni decko", "Knives out", "Wrong turn", "Scream", "Ajfel"]
    y = [ukupno, ukupnoZ, ukupnoK, ukupnoW, ukupnoS, ukupnoA]
    
    plt.bar(x, y)
    plt.title("Karte")
    plt.xticks(rotation = 90)
    plt.xlabel("Ukupan broj prodatih karata po filmu")
    plt.ylabel("Ukupan broj karata")
    plt.show()
    
    
    


    
    
    