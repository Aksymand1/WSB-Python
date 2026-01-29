# Programowanie Zaawansowane, Laboratorium 5: Poszukiwanie bibliotek o określonej funkcjonalności
# Celem jest zapoznanie się z wybranymi bibliotekami Pythona oraz przedstawienie działania wybranych funkcjonalności.
# https://github.com/Aksymand1/WSB-Python/tree/main/Zadanie%205
# Link do repozytorium GitHub.

"""Proste przykłady Web Scraping w Pythonie"""
import requests
from bs4 import BeautifulSoup
import os

# -------------------- Testowanie na lokalnym pliku HTML --------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(BASE_DIR, "index.html")

with open(html_path, "r", encoding="utf-8") as f: # otwieranie pliku HTML
    document = BeautifulSoup(f, "html.parser")

print(document.prettify())
title = document.title.string # pobranie tytułu strony
print(f"Tytuł strony: {title}")
title = "Nowa strona HTML" # Modyfikacja tytułu
print(f"Nowy tytuł: {title}")

p_tags = document.find_all("p") # Znajdowanie wszystkich tagów <p>
for i, p in enumerate(p_tags, start = 1): # Wyświetlenie zawartości każego tagu <p>
    print(f"Tag <p> {i}: {p.string}")    


# -------------------- Testy na zewnętrznej stronie www --------------------------

print("\n--- Testy na zewnętrznej stronie www ---\n")

url = "https://www.azlyrics.com/"

result = requests.get(url)
status_code = result.status_code
print(f"Status odpowiedzi: {status_code}") # Sprawdzenie statusu odpowiedzi

if status_code == 200:
    naglowki = result.headers
    print(f"\nZawartość nagłówków odpowiedzi HTTP:")
    for header, value in naglowki.items():
        print(f"{header}: {value}")

    document = BeautifulSoup(result.text, "html.parser")
    
    tytul_strony = document.title.string
    print(f"\nTytuł strony: {tytul_strony}")
    
    dane = document.find_all("div", class_= lambda value: value and "hotsongs" in value)
    
    piosenki = dane[0].find_all("a")
    for i, piosenka in enumerate(piosenki, start = 1):
        print(f"Piosenka nr {i}: {piosenka.string}")