
""" 
Funkcja zip() zwraca obiekt zip, który jest iteratorem krotek, gdzie pierwszy element z każdego przekazanego iteratora jest parowany razem,
a następnie drugi element z każdego przekazanego iteratora jest parowany razem itd. Jeżeli przekazane iteratory mają różne długości,
to lista z mniejszą ilością elementów decyduje o długości nowego iteratora.
https://www.w3schools.com/python/ref_func_zip.asp

Funkcja enumerate() dodaje licznik do iterowalnego obiektu i zwraca go jako obiekt enumerate.
https://www.w3schools.com/python/ref_func_enumerate.asp#gsc.tab=0

Funkcja sorted() zwraca posortowaną listę z podanego iterowalnego obiektu. Można posortować rosnąco lub malejąco.
Stringi są sortowane alfabetycznie, liczby numerycznie. Nie można sortować list zawierających różne typy danych.
https://www.w3schools.com/python/ref_func_sorted.asp

Moduł random zawiera funkcje do generowania liczb losowych. 
Dla liczb całkowitych istnieje jednolity wybór z zakresu.
Dla sekwencji istnieje jednolity wybór losowego elementu, funkcja do generowania losowej permutacji listy w miejscu
i funkcja do losowego próbkowania bez zastępowania.
https://docs.python.org/3/library/random.html

ZeroDivisionError - wyjątek zgłaszany, gdy dokonywane jest dzielenie jakiejś liczby przez 0.
https://docs.python.org/3/library/exceptions.html#ZeroDivisionError

Link do github: https://github.com/Aksymand1/WSB-Python/tree/main/zadanie_1
Zadanie przesłane 12 października 2025r.
29.10.2025 dodano link do github
"""

# Przykład użycia funkcji zip() i wykorzystanie modułu random do wygenerowania dwóch list o różnych długościach
import random

random_list1 = [random.randint(1, 100) for _ in range(10)]
random_list2 = [random.randint(1, 100) for _ in range(9)]

zipped_list = list(zip(random_list1, random_list2))
print(f"Random list 1: {random_list1}")
print(f"Random list 2: {random_list2}")
print(f"Zipped list: {zipped_list}") # długość listy z mniejszą ilością elementów decyduje o długości nowej listy


a1, a2, a3, a4, a5 = [float(x) for x in input("Podaj 5 wartości oddzielonych spacjami: ").split()]

try:
    if a5 == 0:
        raise ZeroDivisionError('Nie można dzielić przez 0!')
    result = (((a1 + a2) * a3) - a4) / a5
    print(f"Wynik działania jest równy: {result:.3f}")
except ZeroDivisionError as e:
    print(e)

