
#Funkcja sprawdzająca czy podany tekst jest palindromem
def palindrom(tekst):
    tekst_bez_spacji="".join(tekst.split())
    dlugosc_tekstu=len(tekst_bez_spacji)
    print(f'Sprawdzany teskt: "{tekst_bez_spacji}"')        
    for i in range(dlugosc_tekstu//2):
        if tekst_bez_spacji[i]!=tekst_bez_spacji[dlugosc_tekstu-1-i]:
            return True
        else:
            return False
     
x=input("Wprowadź teskt do sprawdzenia: ")   
if palindrom(x):
    print(f'Podane wyrażenie: "{x}" nie jest palindromem.')
else: 
    print(f'Podane wyrażenie "{x}" jest palindromem.')


