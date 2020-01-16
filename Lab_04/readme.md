W zadaniu, należy zaprojektować "szyfrowanie" obrazu graficznego. Obraz powinien być czarno-biały i mieć rozmiar rzędu kilkuset pikseli
w pionie i w poziomie. Obraz taki należy podzielić na małe bloki, np. 3x4 piksele,
w ten sposób każdy blok grafiki zostaje potraktowany jako blok szyfru blokowego. Np. 12-bitowy, jak w programie miniDES.
Cały obraz należy potraktować jako ciąg małych bloków, np. przeglądanych kolejnymi wierszami. 
A jeśli nie jest dostępna implementacja szyfru blokowego, można przyjąć dowolne przekształcenie. 
Nie jest konieczne odszyfrowywanie kryptogramu, jest istotne, by te same bloki były identycznie szyfrowane. 
Np. można zastosować jakąkolwiek funkcję skrótu, np md5sum czy sha1sum, odpowiednio dostosowaną do przekształcania małych bloków. 

Program powinien wczytać plik graficzny i wyprodukować dwa pliki graficzne: kryptogram zaszyfrowany w trybie ECB oraz kryptogram
zaszyfrowany w trybie CBC. Należy pamiętać, że obrazek powinien być maksymalnie nieskomplikowany, 
np. jakiś znak firmowy albo powiększona do dużych rozmiarów czcionka. Przykłady: obrazek jest przekształcany w trybie ECB 
oraz CBC i drugi obrazek, ECB i CBC.

Program block powinien czytać pliki: graficzny plain.bmp i opcjonalnie tekstowy key.txt z kluczem i powinien zapisywać dwa pliki graficzne
"zaszyfrowanego" obrazu ecb_crypto.bmp oraz cbc_crypto.bmp. W rozwiązaniu należy przesłać program w wersji źródłowej i skompilowanej
jak również testowy plik graficzny i ew. plik z kluczem.
