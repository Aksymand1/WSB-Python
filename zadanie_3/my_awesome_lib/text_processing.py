
"""Moduł text_processing.py zawierający narzędzia do przetwarzania tekstu."""

def licz_slowa(tekst: str) -> int:
    """Funkcja zwraca liczbę słów w podanym tekście."""
    return len(tekst.split())

def snake_to_camel(snake_str: str) -> str:
    """Funkcja konwertuje tekst z formatu snake_case na CamelCase."""
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


""" --------------------------------------------------------------------------------------------- """
""" ---------------- Przykładowe użycie funkcji z modułu text_processing.py ------------------ """

# print(licz_slowa("To jest przykładowy tekst."))
# print(snake_to_camel("przykladowy_tekst_do_konwersji"))