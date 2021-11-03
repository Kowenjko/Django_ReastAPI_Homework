from django.test import TestCase
from rest_framework.test import APITestCase,RequestsClient

class API_Testing(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        
    def test_post_address(self):        
        test_data={
            'apartamenst': 236,
            'city': 'Рівне',     
            'country': 'Україна',
            'house_num': 25,            
            'street': 'Боровое (Заречненский р-н), Рівненська обл. Пункт приема - выдачи ',           
            'zip_code': 2525252    }
        response = self.client.post('http://127.0.0.1:8000/address/',data=test_data)
        print(response.json(),response.status_codes)
        self.assertEqual(response.status_code,201)

    def test_get_address(self): 
        response = self.client.get('http://127.0.0.1:8000/address/')
        print(response.json(),response.status_codes)
        self.assertEqual(response.status_code,200)


