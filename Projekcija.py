def ucitajProjekcije():
    for line in open('projekcije.txt', 'r').readlines():
        if len(line) > 1:
            proje = str2proje(line)
            projekcije.append(proje)

def sacuvajProjekcije():
    file = open('projekcije.txt', 'w')
    for proje in projekcije:
        file.write(proje2str(proje))
        file.write('\n')
    file.close()

def str2proje(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prviTermin, drugiTermin, treciTermin = line.split('|')
    proje = {'ime': ime,
             'prviTermin': prviTermin,
             'drugiTermin': drugiTermin,
             'treciTermin': treciTermin}
    return proje

def proje2str(proje):
    return '|'.join([proje['ime'], proje['prviTermin'],
                     proje['drugiTermin'], proje['treciTermin']])

def formatHeader():
    return \
        "Ime            |Prvi termin    |Drugi termin   |Treći termin   \n" \
        "============================================================="

def formatProjekciju(proje):
    return "{0:^6}|{1:^15}|{2:^15}|{3:^15}".format(
        proje['ime'],
        proje['prviTermin'],
        proje['drugiTermin'],
        proje['treciTermin'])

def formatProjekcije(projeList):
    result = ""
    for proje in projeList:
        result += formatProjekciju(proje) + '\n'
    return result

def formatSveProjekcije():
    result = ''
    for proje in projekcije:
        result += "{0:15}|{1:^15}|{2:^15}|{3:^15}".format(
            proje['ime'],
            proje['prviTermin'],
            proje['drugiTermin'],
            proje['treciTermin']) + '\n'
    return result

def sortirajProjekcije(key):
    projekcije.sort(key = lambda x: x[key])



projekcije = []
ucitajProjekcije()

