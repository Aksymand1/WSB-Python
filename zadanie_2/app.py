import re

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
        
print('\n' + '='* 60 + '\n')

#Funkcja sprawdzająca poprawność adresu email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
emails = ["example.com", "user@domain", "prawidlowy.email@domain.com",
          "@domain.com", "mail@user@domena.com", "email-test.com", "email-test@test.domain.com"]
for email in emails:
    if validate_email(email):
        print(f'Podany adres email: "{email}" jest poprawny.')
    else:
        print(f'Podany adres email: "{email}" jest niepoprawny.')


print('\n' + '='* 60 + '\n')

#Funkcja obliczająca objętość kuli na podstawie promienia
class Sphere:
    def __init__(self, radius):
        self.radius = radius
           
    def sphere_volume(radius):
        pi = 3.14159
        volume = (4/3) * pi * (radius ** 3)
        return volume

radii = [3, 5.5, 10, 0.25, 7.8]
for radius in radii:
    volume = Sphere.sphere_volume(radius)
    print(f'Objętość kuli o promieniu {radius} wynosi: {volume:.4f}')


