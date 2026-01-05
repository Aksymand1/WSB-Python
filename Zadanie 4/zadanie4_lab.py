# Programowanie Zaawansowane, Laboratorium 4: Wprowadzenie do biblioteki pymcdm
# Celem jest przećwiczenie implementacji wybranych metod MCDM: TOPSIS, SPOTIS oraz opcjonalnie VIKOR czy PROMETHEE.
# https://github.com/Aksymand1/WSB-Python/tree/main/Zadanie%204
# Link do repozytorium GitHub.


import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.normalizations import minmax_normalization
import matplotlib.pyplot as plt


# Przykładowa macierz decyzyjna dla TOPSIS
decision_matrix = np.array([
    [300, 4, 2, 4],
    [200, 3, 1, 3],
    [150, 2, 3, 2],
    [100, 1, 4, 1]
])


weights = np.array([0.4, 0.3, 0.2, 0.1]) # Wagi kryteriów - suma równa się 1
criteria_types = np.array([1, -1, 1, -1]) # 1 - kryterium maksymalizowane, -1 - kryterium minimalizowane

normalized_matrix = minmax_normalization(decision_matrix) # normalizacja danych

topsis = TOPSIS()
topsis_scores = topsis(decision_matrix, weights, criteria_types)

# Przykładowa macierz decyzyjna dla SPOTIS
decision_matrix_spotis = np.array([
    [9000, 16],
    [8400, 15],
    [7200, 6],
    [6400, 5]
])

bounds = np.array([
    [6400, 9000], 
    [4, 19]        
])

weights_spotis = np.array([0.55, 0.45])
criteria_types_spotis = np.array([1, -1]) 

spotis = SPOTIS(bounds)

spotis_scores = spotis(
    decision_matrix_spotis,
    weights_spotis,
    criteria_types_spotis
)
 
# Metoda VIKOR
# Przykładowa macierz decyzyjna dla VIKOR
decision_matrix_vikor = np.array([
    [7, 9, 9, 8],
    [8, 7, 8, 9],
    [9, 6, 7, 6],
    [6, 8, 6, 7]
])
weights_vikor = np.array([0.15, 0.45, 0.15, 0.25])
criteria_types_vikor = np.array([1, 1, 1, -1])
vikor = VIKOR()
vikor_scores = vikor(
    decision_matrix_vikor,
    weights_vikor,
    criteria_types_vikor
) 

# Wyświetlenie wyników w formacie DataFrame
alternatives = ['A1', 'A2', 'A3', 'A4']
results_df = pd.DataFrame({
    'Alternatives': alternatives,
    'TOPSIS Score': topsis_scores, # Wyższa wartość oznacza lepszą alternatywę
    'SPOTIS Score': spotis_scores, # Niższa wartość oznacza lepszą alternatywę
    'VIKOR Score': vikor_scores # Tutaj także niższa wartość oznacza lepszą alternatywę
})
print("\nWyniki końcowe:")
print(results_df)

# Wizualizacja wyników
x = np.arange(len(alternatives))
width = 0.25
fig, ax = plt.subplots()
bars1 = ax.bar(x - width, results_df['TOPSIS Score'], width, label='TOPSIS')
bars2 = ax.bar(x, results_df['SPOTIS Score'], width, label='SPOTIS')
bars3 = ax.bar(x + width, results_df['VIKOR Score'], width, label='VIKOR')
ax.set_xlabel('Alternatywy')
ax.set_ylabel('Wyniki')
ax.set_title('Porównanie metod MCDM')
ax.set_xticks(x)
ax.set_xticklabels(alternatives)
ax.legend()
plt.show()
