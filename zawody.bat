@echo off
:poczatek
cls
echo 1. Uruchom program
echo 2. Informacja o projekcie
echo 3. Backup
echo 4. Zakoncz program

Set/P opcja=[wybierz opcje]
if %opcja% EQU 1 ( goto start
) 
if %opcja% EQU 2 ( goto projekt
) 
if %opcja% EQU 3 (  goto backup
) 
if %opcja% EQU4 ( goto exit
)
:start
call Zawody.py
call raport.py
call raport.html

pause
goto poczatek

:projekt
echo Autor: Adam Paździerz
echo "Zawody sportowe"
echo Stworzony projekt jest odpowiedzialny za podanie (jesli istnieje taka mozliwosc) poprawej kolejnosci zajetych miejsc na podstawie relacji dziennikarzy.
echo W pliku wejsciowym, w pierwszej linijce podawana jest informacja o liczbie zawodnikow bioracych udzial "n", reprezentujacych "n" roznych krajow oraz miejsca, ktore oni zajeli.
echo Nastepne linijki pliku zapelniane sa wedlug schematu:
echo - jesli dziennikarz relacjonujacy byl pewny swojej decyzji, przed miejscem zawodnika podaje litere "T";
echo - jesli dziennikarz relacjonujacy nie byl pewnny swojej decyzji, przed prawdopodobnymi miejscami, jakie mogł zajac zawodnik podaje litere "N";
echo - relacje kazdego z dziennikarzy sa zapisywane w nowej linijce.

echo Przykladowy schemat:

echo 4 
echo N 2 3
echo T 3
echo N 2 1
echo T 4

echo W pliku wyjsciowym wyswietlana jest informacja, o zajetych miejscach przez zawodnikow. Moze byc ona wyswietlana na dwa sposoby:
echo - jesli na podstawie relacji dziennikarzy da sie okreslic jednoznacznie miejsca zajete przez zawodnikow, wtedy wyswietlany jest w pierwszej linijce komunikat "TAK", a nastepnie w kazdej kolejnej linijce miejsca zajete przez zawodnikow;
echo - jesli na podstawie relacji dziennikarzy nie da sie okreslic jednoznacznie miejsc zajetych przez zawodnikow, wtedy wyswietlany jest w pierszej linijce komunikat "NIE", a nastepnie w kolejne linii liczba mozliwych klasyfikacji.

echo Przykladowy plik wyjscia:

echo TAK
echo 2
echo 3
echo 1
echo 4

pause
goto poczatek

:backup
md backup%date%
xcopy *.* backup%date%\
goto poczatek

:exit
exit

echo on