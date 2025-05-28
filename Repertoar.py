def ucitajRepertoar():
    for line in open('filmovi.txt', 'r').readlines():
        if len(line) > 1:
            film = str2film(line)
            filmovi.append(film)

def str2film(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, zanr, trajanje = line.split("|")
    film = {'ime': ime,
            'zanr': zanr,
            'trajanje': trajanje}
    return film

def film2str(film):
    return '|'.join([film['ime'], film['zanr'],
                     film['trajanje']])

def formatHeader():
    return \
        "Ime            |Žanr           |Trajanje filma     \n" \
        "==============================================="

def formatFilmovi(film):
    return "{0:6}|{1:15}|{2:10}".format(
        film['ime'],
        film['zanr'],
        film['trajanje'])

def formatAllFilms():
    result = ''
    for film in filmovi:
        result += "{0:15}|{1:^15}|{2:^10}".format(
            film['ime'],
            film['zanr'],
            film['trajanje']) + '\n'
    return result

def sortirajFilmove(key):
    filmovi.sort(key = lambda x: x[key])
    
print(__name__)
filmovi = []
ucitajRepertoar()