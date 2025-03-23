
import secrets
import time
import string
import hmac
import bcrypt

# EX_1
def generare_parola():
    lungime = 10
    caractereSpeciale = '.!$@'

    parola = []
    parola += [secrets.choice(string.ascii_lowercase)]
    parola += [secrets.choice(string.ascii_uppercase)]
    parola += [secrets.choice(string.digits)]
    parola += [secrets.choice(caractereSpeciale)]

    parola += [secrets.choice(
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        caractereSpeciale
    ) for _ in range(lungime - 4)]

    return ''.join(secrets.SystemRandom().sample(parola, len(parola)))


print(generare_parola())



# EX_2
def generare_url():
    lungime = 32
    return secrets.token_urlsafe(lungime * 6 // 8) # nrbytes = (6 bits per Base64 char) // 8


print(generare_url())



# EX_3
def generare_token_hexazecimal():
    lungime = 32
    return secrets.token_hex(lungime // 2) # 1 hexadecimal = 4 bits = 1/2 bytes


print(generare_token_hexazecimal())



# EX_4
def secvente_identice(secventa0, secventa1): # HMAC (Hash-based Message Authentication Code)
    return hmac.compare_digest(secventa0, secventa1)


print(secvente_identice('abc', 'abc'))
print(secvente_identice('abc', 'def'))

# alternativa -> comparat manual si facut secrets.randbelow



# EX_5
def generare_cheie_binara():
    lungime = 100
    token = secrets.token_bytes(lungime)
    return ' '.join(format(byte, '08b') for byte in token)
    

print(generare_cheie_binara())



# EX_6
def criptare_parola(parola):
    salt = bcrypt.gensalt()
    hashed_parola = bcrypt.hashpw(parola.encode(), salt)
    return hashed_parola

def verificare_parola(parola_plaintext, parola_criptata):
    return bcrypt.checkpw(parola_plaintext.encode(), parola_criptata)

parola = "parola_secreta"
parola_criptata = criptare_parola(parola)

print("verificare: `parola_secreta` =>", verificare_parola("parola_secreta", parola_criptata))  # True
print("verificare: `parola` => ", verificare_parola("parola", parola_criptata))  # False

