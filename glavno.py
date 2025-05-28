import Repertoar 
import Projekcija
from Naziv import prikaziNaziv
from Karte import ceneAjfel, ceneWrong,ceneKnives,ceneScream,ceneZlatni, ukupnaCena
import Blagajna

def main():
    print()
    print("Dobrodošli u Bioskop!")
    print("=====================")
    print()
    
    komanda = '0'
    while komanda !='X':
        komanda = menu()

        if komanda == '1':
            prikaziFilm()
          
        elif komanda == '2':
            prikaziProjekcije()
           
        elif komanda == '3':
            NazivFilma()
                
        #Odabir filma unosenjem njegovog naziva
        elif komanda == '4':
             odgovor = input("Pretrazite film: ")
             if odgovor == "Zlatni decko":
                 ceneZlatni()
             elif odgovor == "Knives out":
                 ceneKnives()
             elif odgovor == "Wrong turn":
                 ceneWrong()
             elif odgovor == "Scream":
                 ceneScream()
             elif odgovor == "Ajfel":
                 ceneAjfel()
             else:
                 print("Uneti film ne postoji.")
                 
        elif komanda == '5':
            if login():
                print("  K - Broj prodatih karata")
                print("  X - Izlaz!")
            else:
                print("Netacni podaci")
        elif komanda == 'K':
            ukupnaCena()
    print("Dovidjenja!")
            
#Meni pomocu kojeg ucitavamo odabrane komande
def menu():
    printMeni()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', 'K', 'X'):
        print("Izabrali ste nepostojeću opciju! \n")
        printMeni()
        command = input(">> ")
    return command.upper()

# Meni
def printMeni():
    print( "\nOdaberite opciju: ")
    print( "  1 - Repertoar filmova")
    print( "  2 - Projekcije filmova")
    print( "  3 - Dostupni filmovi")
    print( "  4 - Kupite kartu")
    print( "  5 - Blagajna")
    print( "  X - Izlaz!")

#Prikaz repertoara filmova
def prikaziFilm():
    print("1. Repertoar filmova: ")
    print()
    print(Repertoar.formatHeader())
    print(Repertoar.formatAllFilms()[:-1])
    print("="*15 + "=" + "="*15 + "=" + "="*15)
    
def NazivFilma():
    print("---Dostupni filmovi---")
    print("="*22)
    prikaziNaziv()
    print("="*22)
#Prikaz projekcije filmova        
def prikaziProjekcije():
    print("2. Prikazivanje vremena projekcije: ")
    print()
    print(Projekcija.formatHeader())
    print(Projekcija.formatSveProjekcije()[:-1])
    print("="*15 + "=" + "="*15 + "=" + "="*15 + '=' + "="*13)

#Login za blagajnika    
def login():
    print("\nBlagajna")
    print("=========")
    print("Molimo Vas ulogujte se: ")
    username = input("Korisnicko ime: ")
    password = input("Lozinka: ")
    return Blagajna.login(username, password)
    
main()





















