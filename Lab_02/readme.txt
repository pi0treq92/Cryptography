Zaprogramować szyfrowanie i odszyfrowywanie wiadomości przy użyciu szyfru Vigenere'a. Zakładamy, że tekst jawny jest ciągiem małych liter bez spacji, cyfr i znaków przestankowych. Taki tekst jawny trzeba przygotować z realnie dostępnego tekstu za pomocą odpowiedniego narzędzia.

Program o nazwie vigenere powinien umożliwiać wywołanie z linijki rozkazowej z następującymi opcjami:

-p (przygotowanie tekstu jawnego do szyfrowania),
-e (szyfrowanie),
-d (odszyfrowywanie),
-k (kryptoanaliza wyłącznie w oparciu o kryptogram)

Nazwy tych plików są identyczne jak w poprzednim zadaniu:

plain.txt: plik z tekstem jawnym,
crypto.txt: plik z tekstem zaszyfrowanym,
decrypt.txt: plik z tekstem odszyfrowanym,
key.txt: plik zawierający klucz,
orig.txt: oryginalny tekst, przed przygotowaniem do szyfrowania
key-crypto.txt: plik z kluczem znalezionym w wyniku kryptoanalizy
