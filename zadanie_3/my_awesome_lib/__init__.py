""" my_awesome_lib - kolekcja przydatnych narzędzi i funkcji - Laboratorium 3"""

from data_utils import usun_duplikaty, ListProcessor
from math_tools import suma_cyfr_liczby, srednia, silnia, fibonacci
from text_processing import licz_slowa, snake_to_camel

print("my_awesome_lib załadowana pomyślnie.")

__version__ = "1.0"
__author__ = "Paweł Kowalski"
__nr_albumu__ = "167013"
__all__ = [
    "usun_duplikaty",
    "ListProcessor",
    "suma_cyfr_liczby",
    "srednia",
    "silnia",
    "fibonacci",
    "licz_slowa",
    "snake_to_camel",
]