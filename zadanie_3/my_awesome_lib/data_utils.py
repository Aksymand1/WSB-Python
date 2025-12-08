
"""Moduł data_utils.py zawierający narzędzia do przetwarzania danych."""

import random

def usun_duplikaty(data: list) -> list:
    """ Funkcja usuwa duplikaty z listy. Zachowuje kolejność elementów."""
    return list(dict.fromkeys(data))

class ListProcessor:
    """ Klasa zawierająca metody do przetwarzania list zawierających liczby całkowite. """
    def __init__(self):
        self.data = []
        
    def losuj_n(self) -> int:
        """Losuje i zwraca liczbę całkowitą z zakresu 10-100, która będzie rozmiarem listy do wygenerowania."""
        return random.randint(10, 100)
    
    def generuj_liste(self, n: int) -> list:
        """Generuje listę n losowych liczb całkowitych z zakresu 1-49."""
        self.data = [random.randint(1, 50) for _ in range(n)] # Wypełnia listę wartościami od 1 do 49
        return self.data
        
    def zamien(self, x: int) -> int:
        """Zamienia wszystkie liczby parzyste na 0, a nieparzyste na ich wartość przeciwną."""
        if x % 2 == 0:
            return 0
        return -x
        
    def mapuj(self) -> list:
        """Mapuje funkcję zamien na wszystkie elementy listy i odwraca kolejność listy."""
        self.data = list(map(self.zamien, self.data))[::-1]
        return self.data
    

""" --------------------------------------------------------------------------------------------- """    
""" ---------------- Przykładowe użycie funkcji i klasy z modułu data_utils.py ------------------ """    
    
# print(usun_duplikaty([1, 2, 2, 3, 4, 4, 5]))  # Przykładowe użycie funkcji usun_duplikaty
    
testowa_lista = ListProcessor()
n = testowa_lista.losuj_n()
print(f"Wylosowana liczba n: {n}")
testowa_lista.generuj_liste(n)
print(f"Wygenerowana lista: {testowa_lista.data}")
print()
print(f"Lista po przetworzeniu: {testowa_lista.mapuj()}")