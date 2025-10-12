# Kowalski Paweł, nr albumu 167013
# Zadanie 1: Tworzenie i łączenie list


import random

random_list1 = [random.randint(1, 100) for _ in range(10)]
random_list2 = [random.randint(1, 100) for _ in range(10)]

zipped_list = list(zip(random_list1, random_list2))

print(f"Zipped list: {zipped_list}")