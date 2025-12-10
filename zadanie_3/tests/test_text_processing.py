from ..my_awesome_lib.text_processing import licz_slowa, snake_to_camel
import unittest

class TestLiczSlowa(unittest.TestCase):
    def test_pusty_ciag(self):
        self.assertEqual(licz_slowa(""), 0)

    def test_pojedyncze_slowo(self):
        self.assertEqual(licz_slowa("Hello"), 1)

    def test_wiele_slow(self):
        self.assertEqual(licz_slowa("To jest przykładowy tekst."), 4)

    def test_interpunkcja(self):
        self.assertEqual(licz_slowa("Cześć, jak się masz?"), 4)
        
    def test_nowe_linie(self):
        self.assertEqual(licz_slowa("To jest\nprzykładowy tekst."), 4)
        
    def test_wiele_spacji(self):
        self.assertEqual(licz_slowa("To   jest    przykładowy   tekst."), 4)
        
    def test_tylko_spacje(self):
        self.assertEqual(licz_slowa("     "), 0)
        
    def test_split(self):
        with self.assertRaises(AttributeError):
            licz_slowa(None)
            licz_slowa(123)
            licz_slowa([])
            licz_slowa({})
            licz_slowa(4.55)


class TestSnakeToCamel(unittest.TestCase):
    def test_pusty_ciag(self):
        self.assertEqual(snake_to_camel(""), "")

    def test_jedno_slowo(self):
        self.assertEqual(snake_to_camel("hello"), "Hello")

    def test_wiele_slow(self):
        self.assertEqual(snake_to_camel("Ala_ma_kota_kot_ma_Alę"), "AlaMaKotaKotMaAlę")

    def test_podkreslniki_na_pocz_i_koncu(self):
        self.assertEqual(snake_to_camel("_Tesktdo_testu_"), "TesktdoTestu")

    def test_wiele_podkreslnikow(self):
        self.assertEqual(snake_to_camel("_To____zdanie_zawiera__wiele_podkreślników____"), "ToZdanieZawieraWielePodkreślników")

    def test_brak_podkreslnikow(self):
        self.assertEqual(snake_to_camel("przykladowytekst"), "Przykladowytekst")
        
    def test_inne_znaki(self):
        self.assertNotEqual(snake_to_camel("przykladowy-tekst_do.konwersji!"), "PrzykladowyTekstDoKonwersji!")
        
    
    def test_split(self):
        with self.assertRaises(AttributeError):
            snake_to_camel(None)
            snake_to_camel(123)
            snake_to_camel([])
            snake_to_camel({})
            snake_to_camel(4.55)

    def test_types(self):
        self.assertIsInstance(snake_to_camel("przykladowy_tekst"), str)
        self.assertIsInstance(snake_to_camel(""), str)
        self.assertNotIsInstance(snake_to_camel("przykladowy_tekst"), int)
        self.assertNotIsInstance(snake_to_camel(""), list)
        
        
        
if __name__ == '__main__':
    unittest.main()