# Exercitiu 1

| Termen | Definitie |
|---	|---	|
| (A) Adversar  	            | (3) O entitate (inclusiv un insider) care acționează rău intenționat pentru a compromite un sistem.  	|
| (B) Securitate  	            | (1) O condiție care rezultă din stabilirea și menținerea măsurilor de protecție care permit unei organizații/sistem să își îndeplinească misiunea sau funcțiile critice, în ciuda riscurilor reprezentate de amenințări.  	|
| (C) Risc  	                | (5) O măsură a gradului în care o entitate este amenințată de o eventuală circumstanță sau eveniment.   	|
| (D) Vulnerabilitate  	        | (2) Slăbiciune într-un sistem informațional, proceduri de securitate ale sistemului, controale interne sau implementare care ar fi putea fi exploatate sau declanșate de o sursă de amenințare.  	|
| (E) Securitatea cibernetică  	| (4) Capacitatea de a proteja / apăra spațiul cibernetic de atacuri cibernetice.	|



# Exercitiu 3
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



# Exercitiu 4
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


# Exercitiu 5
#### Considerați numele dumneavoastră, scris cu majuscule. Ce îi corespunde conform codificării Base64?

#### Se consideră codificarea Base64 dată de string-ul următor: U3VudCBzdHVkZW50IGxhIEZNSS4=. Ce îi corespunde?

