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


Treść zadania:
Zaprogramować szyfrowanie i odszyfrowywanie wiadomości przy użyciu szyfru Cezara i szyfru afinicznego.

Program o nazwie cezar powinien umożliwiać wywołanie z linijki rozkazowej z następującymi opcjami:

-c (szyfr Cezara),
-a (szyfr afiniczny)

oraz

-e (szyfrowanie),
-d (odszyfrowywanie),
-k (kryptoanaliza wyłącznie w oparciu o kryptogram),
-j (kryptoanaliza z tekstem jawnym)

Program będzie czytał dane z pewnych plików i zapisywał na inne, nazwy tych plików są z góry ustalone:

plain.txt: plik z tekstem jawnym,
crypto.txt: plik z tekstem zaszyfrowanym,
decrypt.txt: plik z tekstem odszyfrowanym,
key.txt: plik zawierający klucz, (jeden wiersz, w którym pierwsza liczba oznacza przesunięcie, druga współczynnik dla szyfru afinicznego, liczby oddzielone są spacją)
key-new.txt: plik z odzyskanym kluczem
extra.txt: plik zawierający pomocniczy tekst jawny w przypadku kryptoanalizy z tekstem jawnym i zaszyfrowanym.

Program szyfrujący czyta tekst jawny i klucz i zapisuje tekst zaszyfrowany. Jeśli klucz jest nieprawidłowy, zgłasza jedynie błąd.

Program odszyfrowujący czyta tekst zaszyfrowany i klucz i zapisuje tekst jawny. Jeśli klucz jest nieprawidłowy, zgłasza błąd. Dla szyfru afinicznego częścią zadania jest znalezienie odwrotności dla liczby a podanej jako część klucza – nie można zakładać, że program odszyfrowujący otrzymuje tę odwrotność.

Program łamiący szyfr bez pomocy tekstu jawnego czyta jedynie tekst zaszyfrowany i zapisuje jako tekst jawny wszystkie możliwe kandydatury (25 dla szyfru Cezara, 312 dla szyfru afinicznego).

Program łamiący szyfr z pomocą tekstu jawnego czyta tekst zaszyfrowany, tekst pomocniczy i zapisuje obliczony klucz i odszyfrowany tekst. Jeśli niemożliwe jest obliczenie klucza, zgłasza sygnał błędu. Dopuszczalna jest wersja, w której w sytuacji niemożności obliczenia klucza program jednak zwraca sensowne wartości, mianowicie możliwe klucze i możliwe teksty odszyfrowane. Mimo braku jednoznaczności jest znacząco mniej rozwiązań niż w analizie bez teksty jawnego.
