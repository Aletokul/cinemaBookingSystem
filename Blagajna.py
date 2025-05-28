def login(username, password):
    for blag in blagajna:
        if blag['username'] == username and blag['password'] == password:
            return True
    return False

#Otvaramo i citamo,
def ucitajBlagajnike():
    for line in open('blagajna.txt', 'r').readlines():
        if len(line) > 1:
            blag = str2blag(line)
            blagajna.append(blag)

def str2blag(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prezime, username, password = line.split('|')
    blag = {
        'ime': ime,
        'prezime': prezime,
        'username': username,
        'password': password
    }
    return blag

def blag2str(blag):
    return '|'.join([blag['ime'], blag['prezime'], blag['username'], blag['password']])

print(__name__)
blagajna = []
ucitajBlagajnike()






