import unittest
from city_funtions import format_data

class CityTesCase(unittest.TestCase):

    def test_format_data(self):
        city_country = format_data('Madrid','España')
        self.assertEqual(city_country,'Madrid España')
    
    def test_format_data_title(self):
        city_country = format_data('madrid','españa')
        self.assertEqual(city_country,'Madrid España')
    
    def test_format_data_population(self):
        city_country = format_data('madrid','españa',46549045 )
        self.assertEqual(city_country,'Madrid España | 46549045')
    
unittest.main()