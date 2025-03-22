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
- nu cicleaza
- converge catre infinit 
- Distributia numerelor este uniforma (multe numere nu vor aparea niciodata)
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

TODO



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


