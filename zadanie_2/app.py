
#Funkcja sprawdzająca czy podany tekst jest palindromem
def palindrom(tekst):
    tekst_bez_spacji = "".join(tekst.split()).lower()
    dlugosc_tekstu=len(tekst_bez_spacji)    
    for i in range(dlugosc_tekstu//2):
        if tekst_bez_spacji[i]!=tekst_bez_spacji[dlugosc_tekstu-1-i]:
            return False
    return True

palindromy = ["Kajak", "Wół utył i ma miły tułów", "A to kanapa pana Kota",
              "Ala ma kota", "Kobyła ma mały bok", "nie jestem palindromem"]

for tekst in palindromy:
    if palindrom(tekst):
        print(f'Podane wyrażenie: "{tekst}" jest palindromem.')
    else: 
        print(f'Podane wyrażenie: "{tekst}" nie jest palindromem.')
        
