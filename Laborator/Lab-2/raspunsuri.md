# Exercitiul 1

| Termen | Definitie |
|---	|---	|
| (A) Criptologie | (4) Știința care se ocupă de criptanaliză și criptografie. |
| (B) Criptografie | (2) Disciplina care studiază principiile, mijloacele și metodele de transformare a datelor pentru a ascunde conținutul lor semantic, a preveni utilizarea lor neautorizată sau a preveni modificarea lor nedetectată. |
| (C) Criptanaliză | (5) Încercarea de a înfrânge protecția criptografice fără o cunoaștere inițială a cheii utilizate în furnizarea protecției. |
| (D) Confdențialitate | (1) Asigurarea că informațiile nu sunt dezvăluite entităților neautorizate. |
| (E) Integritate | (6) Protejarea împotriva modificării sau distrugerii necorespunzătoare a informațiilor |
| (F) Disponibilitate | (3) Asigurarea accesului și utilizării informațiilor în timp util și fiabil. |

# Exercitiul 2

1. Salariile angajaților nu trebuie făcute publice. **=> CONFIDENTIALITATE**
2. Biroul casierie trebuie să aibă acces la salariile angajaților (pentru a realiza plățile). **=> DISPONIBILITATE**
3. Un angajat nu își poate modifica singur suma primită ca salariu pe luna în curs. **=> INTEGRITATE**
4. Un angajat nu ar trebui să afle cât câștiga un coleg fără acordul acestuia (ex. să îi spună direct). **=> CONFIDENTIALITATE**
5. Biroul casierie trebuie să aibă certitudinea că suma pe care o înmânează angajatului de plată este cea corectă.  **=> INTEGRITATE**  

Primitive criptografice pentru **confidentialitate**:
- algoritmi de criptare: RSA

Primitive criptografice pentru **integritate**:
- semnaturi digitale
- funcții hash criptografice: SHA-256
- MAC = Message authentication code

# Exercitiul 3

Adversar Probabilistic Polinomial în Timp (PPT)

1. Un adversar care are la dispoziție un timp infinit pentru criptanaliza unui sistem este un adversar PPT. **=> FALS**
2. Un adversar PPT are dreptul de a „ghici” cheia. **=> ADEVARAT**
3. Un adversar PPT are la dispoziție algoritmi exponențiali în timp. **=> FALS**

# Exercitiul 4

1. f(n) = 2 **=>ne-neglijabilă**
2. f(n) = 1/2000 **=>ne-neglijabilă**
3. f(n) = 1/n^2000 **=>neglijabilă**
4. f(n) = 1/2^n **=>neglijabilă**
5. f(n) = f1(n) + f2(n), unde f1(n) și f2(n) sunt neglijabile **=>neglijabilă**
6. f(n) = f1(n) + f2(n), unde f1(n) este neglijabilă și f2(n) este ne-neglijabilă **=>ne-neglijabilă**

# Exercitiul 5

Dați câteva argumente pentru care preferăm să utilizăm securitatea computațională în practică. De ce nu avem ca scop securitatea perfectă (i.e., indiferent de resursele adversarului un sistem să nu poată fi spart)? Discuție.

- Securitatea perfecta necesita foarte multe resurse, necesita schimbul și stocarea unor volume uriașe de chei
- Scaderea performantei
- Scaderea scalabilitatii

# Exercitiul 6

Se consideră un sistem criptografic care folosește o cheie de criptare pe 512 biți.   

• Câte chei posibile distincte există?  
$$ 2^{512} $$

• Cât timp îi va lua unui adversar găsirea cheii corecte (cazul cel mai nefavorabil) dacă are la dispoziție un calculator care testează $2^{30}$ chei pe secundă?
$$TimpulMaxim=\frac{2^{512}}{2^{30}} = 2^{482} secunde$$

• Considerați că este un atac eficient?  
Nu este eficient pentru ca necesita foarte mult timp

