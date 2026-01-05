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
    [420, 5, 2, 4],
    [340, 3, 1, 3],
    [275, 1, 6, 2],
    [125, 2, 7, 3]
])

weights = np.array([0.4, 0.3, 0.2, 0.1]) # Wagi kryteriów - suma równa się 1
criteria_types = np.array([1, -1, 1, -1]) # 1 - kryterium maksymalizowane, -1 - kryterium minimalizowane

normalized_matrix = minmax_normalization(decision_matrix) # normalizacja danych

topsis = TOPSIS()
topsis_scores = topsis(decision_matrix, weights, criteria_types)

# Metoda SPOTIS
bounds = np.array([[decision_matrix[:, 0].min(), decision_matrix[:,0].max()], # wartości min i max z 1 kolumny, poniżej tak samo dla pozostałych 
                  [decision_matrix[:, 1].min(), decision_matrix[:,1].max()],
                  [decision_matrix[:, 2].min(), decision_matrix[:,2].max()],
                  [decision_matrix[:, 3].min(), decision_matrix[:,3].max()]]
                  )

spotis = SPOTIS(bounds)
spotis_scores = spotis(decision_matrix, weights, criteria_types)
 
# Metoda VIKOR
vikor = VIKOR()
vikor_scores = vikor(decision_matrix, weights, criteria_types) 

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