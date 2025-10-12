# Kowalski Paweł, nr albumu 167013
# Zadanie 1: Tworzenie i łączenie list

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
"""

# Przykład użycia funkcji zip()
import random

random_list1 = [random.randint(1, 100) for _ in range(10)]
random_list2 = [random.randint(1, 100) for _ in range(9)]

zipped_list = list(zip(random_list1, random_list2))
print(f"Random list 1: {random_list1}")
print(f"Random list 2: {random_list2}")
print(f"Zipped list: {zipped_list}")