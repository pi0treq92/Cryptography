Zadania:

    Przygotować plik personal.txt ze swoimi danymi osobowymi. Obliczyć wszystkie funkcje skrótu na tym pliku, wyniki zapisać do pliku hash.txt w kolejności coraz dłuższych skrótów.

    Przygotować drugą wersje pliku z tymi samymi danymi osobowymi personal_.txt, różniącą się jedynie dodatkowym pustym wierszem na końcu. 
    Obliczyć wartość wszystkich funkcji skrótu dla obu wersji pliku połączonego z plikiem pdf wykładu hash.pdf (tzn. wykonać polecenia:

    cat hash.pdf personal.txt | md5sum >> hash.txt
    cat hash.pdf personal_.txt | md5sum >> hash.txt

    itd. dla obu wersji pliku z danymi osobowymi). Następnie sprawdzić liczbę bitów (nie bajtów) różnych w obu wynikach. 
    Należy się spodziewać, że w każdej parze ok. połowa bitów będzie różna. Przesłać jedynie plik diff.txt zawierający sześć par wyników
    dla każdej z funkcji skrótu i liczbę bitów różniących te wyniki.

    Przykładowy plik z wynikami: diff.txt.
