Witam w programie szyfr_cezara.
Program można uruchomić w IDE PyCharm lub w linii poleceń np.

C:\Users\Piotr\Documents\GitHub\techniki_projekt\Kryptografia>python szyfr_cezara.py

Program wyświetli następujące menu.

Witam w programie Szyfrowanie z Cezarem.
Wybierz jedną z poniższyc opcji:
'c':    szyfr Cezara
'a':    szyfr afiniczny
c
Po wybraniu rodzaju szyfru (afiniczny/cezar) wyświetli sie drugie menu w którym wybieramy rodzaj czynności.

Wybierz jedna z ponizszych opcji:
'e':    szyfrowanie
'd':    odszyfrowanie
'k':    kryptoanaliza wyłacznie w oparciu o kryptogram
'j':    kryptoanaliza z tekstem jawnym

W zależności od wybranej opcji program zapisze dane do jednego z poniższych plików:
decrypt.txt
crypto.txt
key-new.txt

W pliku key.txt zapisujemy litery z jakimi chcemy szyfrować dane.
W pliku plain.txt zapisujemy tekst do zaszyfrowania.
W pliku extra.txt zapisany jest tekst pomocniczy "alamakota".

Uwaga!
Jeśli chcemy przeprowadzić kryptoanalizę z użyciem szyfru Cezara lub afinicznego, w oparciu o kryptogram lub tekst jawny,
należy odpowiednio zaszyfrować dany tekst z odpowiednim szyfrem.
