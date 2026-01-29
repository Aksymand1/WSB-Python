# Programowanie Zaawansowane, Laboratorium 5: Poszukiwanie bibliotek o określonej funkcjonalności
# Celem jest zapoznanie się z wybranymi bibliotekami Pythona oraz przedstawienie działania wybranych funkcjonalności.
# https://github.com/Aksymand1/WSB-Python/tree/main/Zadanie%205
# Link do repozytorium GitHub.

"""Przykłady Web Scraping w Pythonie"""
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

url = "https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/pamieci-ram/pamiec-ram-goodram-irdm-32gb-2x16gb-ddr5-6000mt-s-cl30"

result = requests.get(url)
print(f"Status odpowiedzi: {result.status_code}") # Sprawdzenie statusu odpowiedzi