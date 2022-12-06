from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from inventory.models import Product, Category

import json

  


class ProductTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        category1 = Category.objects.create(name="Category1", description="description1")
        product1 = Product.objects.create(name="Product1", price=15, brand="Brand1",description="description1",
        stock="5", slug="Slug1",displayrent="True")
        product1.category.add(category1)
       
    def test_list(self):

        #utwórz modele w bazie danych potrzebne do dalszych testów
       

        #print(Product.objects.all())
        
        # wysyłamy żądanie GET do adresu URL /api/v1/users
        response = self.client.get('/api/')

        # sprawdzamy, czy otrzymaliśmy odpowiedź 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #print(json.dumps(response.data, indent=2))
        # sprawdzamy, czy lista zwróconych użytkowników zawiera przynajmniej jeden element
        self.assertGreater(len(response.data), 0)


  

class LoginTests(TestCase):
    
    def test_login(self):
        # przygotowujemy dane do wysłania w żądaniu POST
        data = {
            'username': 'testuser',
            'password': 'testpas'
        }
        #wysyłamy żądanie POST rejestrujące nowego użytkownika
        response = self.client.post('/users/', data)      
       
        # sprawdzamy, czy otrzymaliśmy odpowiedź 201 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # wysyłamy żądanie POST logujące się na konto
        response = self.client.post('/auth/', data)
       

        # sprawdzamy, czy otrzymaliśmy odpowiedź 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # sprawdzamy, czy w odpowiedzi został zwrócony token 
        self.assertIn('token', response.data)



    def test_invalid_login(self):
        # przygotowujemy dane do wysłania w żądaniu POST
        data = {
            'username': 'testuser',
            'password': 'invalidpassword'
        }

        # wysyłamy żądanie POST do adresu URL /api/v1/login
        response = self.client.post('/auth/', data)

        # sprawdzamy, czy otrzymaliśmy odpowiedź 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    