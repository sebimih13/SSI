# Exercitiul 1

| Termen | Definitie |
|---	|---	|
| (A) Adversar  	            | (3) O entitate (inclusiv un insider) care acționează rău intenționat pentru a compromite un sistem.  	|
| (B) Securitate  	            | (1) O condiție care rezultă din stabilirea și menținerea măsurilor de protecție care permit unei organizații/sistem să își îndeplinească misiunea sau funcțiile critice, în ciuda riscurilor reprezentate de amenințări.  	|
| (C) Risc  	                | (5) O măsură a gradului în care o entitate este amenințată de o eventuală circumstanță sau eveniment.   	|
| (D) Vulnerabilitate  	        | (2) Slăbiciune într-un sistem informațional, proceduri de securitate ale sistemului, controale interne sau implementare care ar fi putea fi exploatate sau declanșate de o sursă de amenințare.  	|
| (E) Securitatea cibernetică  	| (4) Capacitatea de a proteja / apăra spațiul cibernetic de atacuri cibernetice.	|



# Exercitiul 3
#### Considerați ziua în care v-ați născut la care adăugați valoarea 10. Transformați în binar această valoare. Faceți transformarea inversă.

zi = 13  
13 + 10 = 23  

Transformare din baza 10 in baza 2:  
23          => 1  
23 / 2 = 11 => 1  
11 / 2 = 5  => 1  
5 /  2 = 2  => 0  
2 /  2 = 1  => 1  
1 /  2 = 0  => 0  
=> binar = 10111

Transforamre din baza 2 in baza 10:  
10111 => 2^0 + 2^1 + 2^2 + 2^4 = 1 + 2 + 4 + 16 = 23  



#### Considerați un număr hexazecimal oarecare de 4 cifre. Transformați în binar această valoare. Faceți transformarea inversă.

Transformare din baza 16 in baza 2:  
hexadecimal = 0x1234  
0x1234 = 4 * 16^0 + 3 * 16^1 + 2 * 16^3 + 1 * 16^3  
- 4 * 16^0 = 0100
- 3 * 16^1 = 0011
- 2 * 16^3 = 0010
- 1 * 16^3 = 0001

=> binar = 0001 0010 0011 0100



Transformare din baza 2 in baza 16:  
binar = 0001 0010 0011 0100  
- 0100 => 4
- 0011 => 3
- 0010 => 2
- 0001 => 1

=> hexadecimal = 0x1234



# Exercitiul 4
#### Considerați prenumele dumneavoastră, scris cu majuscule. Ce îi corespunde conform codificării ASCII?

prenume = SEBASTIAN-STEFAN  
S = 83  
E = 69  
B = 66  
A = 65  
T = 84  
I = 73  
N = 78  
\- = 45  
F = 70  

=> codificare ASCII = 83 69 66 65 83 84 73 65 78 45 83 84 69 70 65 78


#### Se consideră codificarea ASCII 66 82 65 86 79. Ce cuvânt îi corespunde?
66 = B  
82 = R  
65 = A  
86 = V  
79 = O  

=> string = BRAVO


# Exercitiul 5

- convertim caracterele in format ASCII
- convertim numarul in binar
- impartim in bucati de cate 6 biti
- in functie de numar alegem maparea din Base64 = A-Za-z0-9+/=

#### Considerați numele dumneavoastră, scris cu majuscule. Ce îi corespunde conform codificării Base64?

nume = MIHALACHE  
Transformare in Base64 = TUlIQUxBQ0hF  

#### Se consideră codificarea Base64 dată de string-ul următor: U3VudCBzdHVkZW50IGxhIEZNSS4=. Ce îi corespunde?

Base64 = U3VudCBzdHVkZW50IGxhIEZNSS4=  
Transformare in string ASCII = Sunt student la FMI.


# Exercitiul 6
#### malware, virus, dropper, downloader, trojan, spyware, riskware, ransomware, adware, worm, obfuscare

- malware = Orice tip de software malițios creat pentru a afecta negativ un sistem  
- virus = Un tip de malware care se atașează la fișiere legitime și se răspândește prin execuția acestora  
- dropper = Un program malițios care nu conține direct malware, dar îl descarcă și îl instalează pe dispozitivul infectat  
- downloader = Similar cu un dropper, dar funcționează prin descărcarea malware-ului de pe internet după ce a fost executat
- trojan = Un program care pare legitim, dar conține funcționalități ascunse și malițioase
- spyware = Malware conceput pentru a spiona activitatea utilizatorului și a colecta informații fără permisiune
- riskware = Software potențial periculos care poate fi folosit abuziv
- ransomware = Malware care blochează accesul la fișiere sau sistem și cere o răscumpărare pentru deblocare
- adware = Software care afișează reclame intruzive, de obicei fără consimțământul utilizatorului
- worm = Un tip de malware care se răspândește automat prin rețele, fără a necesita intervenția utilizatorului
- obfuscare = Tehnică folosită pentru a ascunde codul sursă sau scopul unui malware, îngreunând detectarea acestuia


