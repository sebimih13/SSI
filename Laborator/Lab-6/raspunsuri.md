# Exercitiul 1

### Candidate 1:
- Afiseaza primul seed citit de la tastatura, dupa care genereaza doar 0
- Este predictibil, indiferent de primul seed pe care il primeste genereaza doar 2 valori unice
- Distributia numerelor nu este uniforma

```
#Candidate 1
try:
    while True:
        print(seed)
        seed=seed^seed
except KeyboardInterrupt:
    pass
```

### Candidate 2:
- overflow - nu mentine valorile intr-un interval
- converge catre infinit 
- Distributia numerelor nu este uniforma (multe numere nu vor aparea niciodata)
- Generarea numerelor este predictibila, este un sir strict crescator. Daca analizam putin numerele, putem sa intuim usor care este formula pentru generearea numerelor

```
#Candidate 2
try:
    while True:
        print(seed)
        seed=int(seed+seed/2)
except KeyboardInterrupt:
    pass
```

### Candidate 3:
- Mereu este generat acelasi numar, seed-ul initial citit de la tastatura impartiti la 4

```
#Candidate 3
print(seed>>2)
```



# Exercitiul 2

## Cerinta 1
```
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
```

**OUTPUT:** ``` S@VL$e8xVe ```  
**UTILIZRE:** Google Password Manager => sugereaza parole puternice pe care le gestioneaza el automat



## Cerinta 2
```
def generare_url():
    lungime = 32
    return secrets.token_urlsafe(lungime * 6 // 8) # nrbytes = (6 bits per Base64 char) // 8


print(generare_url())
```

**OUTPUT:** ``` l-vKwLW8nSL_nMcqGHM3KFPaqOScGF-z ```  
**UTILIZRE:** Poate fi folosita atunci cand dorim sa generam un identificator unic pentru o resura. Generare de tokens pentru inregistrare/autentificare, resetare parola



## Cerinta 3
```
def generare_token_hexazecimal():
    lungime = 32
    return secrets.token_hex(lungime // 2) # 1 hexadecimal = 4 bits = 1/2 bytes


print(generare_token_hexazecimal())
```

**OUTPUT:** ``` 95c9b7d559bee8b3d09bd9a66d34e239 ```  
**UTILIZRE:** Poate fi folosita atunci cand dorim sa generam un identificator unic pentru o resura. Generare de tokens pentru inregistrare/autentificare, resetare parola.



## Cerinta 4
```
def secvente_identice(secventa0, secventa1): # HMAC (Hash-based Message Authentication Code)
    return hmac.compare_digest(secventa0, secventa1)


print(secvente_identice('abc', 'abc'))
print(secvente_identice('abc', 'def'))

# alternativa -> comparat manual si facut secrets.randbelow
```

**OUTPUT:** 
``` 
True
False 
```  


## Cerinta 5
```
def generare_cheie_binara():
    lungime = 100
    token = secrets.token_bytes(lungime)
    return ' '.join(format(byte, '08b') for byte in token)
    

print(generare_cheie_binara())
```

**OUTPUT:** ``` 00111101 01101000 11100001 00110101 00101001 11100010 11001010 11010000 00011100 11011001 01110011 00101010 01001111 11100110 11010000 00011100 11100111 00011011 11100100 01010001 01100101 10001000 00011111 11101000 11111000 11011011 01010001 00011000 10001011 00101111 00110010 00011111 11100001 00011000 00011011 10101010 01101111 00011011 10110011 01000111 10110100 01001011 00101101 10110010 10010000 10010000 10000010 01110000 10000110 00000010 10000000 10101100 11111110 00010010 11111100 00011101 00011111 10001011 01111100 10101110 01110110 10001101 11010010 10110111 10001011 01111111 01010100 10010100 11011110 00001111 01011010 01101011 11000011 10101001 01101110 01101111 11110000 10011011 01001000 10101001 00001110 00111110 00110010 00000100 10111011 10001010 00111001 11110101 01110101 11011011 10100100 11001111 10110100 00010001 00111101 01110000 10010101 10001110 00101100 00011000 ```  



## Cerinta 6
```
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
```

**OUTPUT:** 
```
verificare: `parola_secreta` => True
verificare: `parola` =>  False 
```  
**UTILIZRE:** Pentru a salva parole criptate in baza de date, evitand astfel stocarea lor in text clar. In cazul unei spargeri a bazei de date, atacatorul nu va putea descifra parola reala.





# Exercitiul 3

### Pentru cod Java:
- CWE-335: Incorrect Usage of Seeds in Pseudo-Random Number Generator (PRNG)
https://cwe.mitre.org/data/definitions/335.html
- CWE-336: Same Seed in Pseudo-Random Number Generator (PRNG)
https://cwe.mitre.org/data/definitions/336.html

In codul de Java se va genera acelasi numar random pentru orice utilizator.
Astfel toti utilizatorii ce isi creeaza un cont vor avea exact acelasi ID, deoarece seed-ul la random este mereu acelasi.

### Pentru cod PHP:
- CWE-337: Predictable Seed in Pseudo-Random Number Generator (PRNG)
https://cwe.mitre.org/data/definitions/337.html

In codul de PHP, ID-ul sesiunii este direct legat de ID-ul utilizatorului (acesta fiind seed pentru generarea sesiunii). Astfel, daca se cunoaste ID-ul pentru user se poate deduce sesiunea, fiind un algoritm determinist.

- CWE-334: Small Space of Random Values
https://cwe.mitre.org/data/definitions/334.html

Daca spatial de valori random posibile este mic, atunci exista o vulnerabilitate ce poate fi exploatata printr-un brute-force.


### Atacul CAPEC
CAPEC CATEGORY: Abuse Existing Functionality
CAPEC-112: Brute Force   
https://capec.mitre.org/data/slices/333.html

"If the secret was chosen algorithmically, cryptanalysis can be applied to the algorithm to discover patterns in this algorithm. (This is true even if the secret is not used in cryptography.) Periodicity, the need for seed values, or weaknesses in the generator all can result in a significantly smaller secret space."



### Utilizari
Da, exista alte utilizari defectuoase ale PRNG explicate in alte CWE-uri:

- CWE-332: Insufficient Entropy in PRNG
"The lack of entropy available for, or used by, a Pseudo-Random Number Generator (PRNG) can be a stability and security threat." https://cwe.mitre.org/data/definitions/332.html

- CWE-338: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
https://cwe.mitre.org/data/definitions/338.html
- CVE-2024-45723
https://www.cve.org/CVERecord?id=CVE-2024-45723

Algoritmii de generare pseudo-random pot avea entropia slaba, iar distributia nu este astfel una suficient de uniforma. Sursa de randomness poate fi una predictibila, adaugand astfel o alta vulnerabilitate.
Poate fi atacat prin brute-force.





### Inregistrări CVE care se referă la vulnerabilități în legătură cu PRNG
Anul acesta au fost identificate 4 vulnerabilitati legate de PRNG (16.03.2025):  
https://www.cve.org/CVERecord/SearchResults?query=prng


