
"""Moduł math_tools.py zawierający przykładowe narzędzia matematyczne."""

def suma_cyfr_liczby(number: int) -> int:
    """Funkcja zwraca sumę cyfr podanej liczby całkowitej."""
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum    


def srednia(liczby: list) -> float:
    """Funkcja zwraca średnią arytmetyczną z listy liczb."""
    if not liczby:
        raise ValueError("Lista nie może być pusta.")
    return sum(liczby) / len(liczby)


def silnia(n: int) -> int:
    """Funkcja zwraca silnię liczby n."""
    if n < 0:
        raise ValueError("N nie może być ujemne.")
    if n <= 1:
        return 1
    return n * silnia(n - 1)


def fibonacci(n: int) -> int:
    """Funkcja zwraca pierwszą znalezioną liczbę Fibonacciego zawierającą n cyfr oraz jej indeks."""
    a, b = 0, 1
    i = 1
    while len(str(b)) < n:
        a, b = b, a + b
        i += 1
    return i, b

