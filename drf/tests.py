from django.test import TestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from inventory.models import Product, Category
import json
  
class JopekTests(TestCase):
    #utwórz modele w bazie danych potrzebne do dalszych testów
    @classmethod
    def setUpTestData(cls):
        category1 = Category.objects.create(name="Category1", description="description1")
        product1 = Product.objects.create(name="Product1", price=15, brand="Brand1",description="description1",
        stock="5", slug="Slug1",displayrent="True")
        product1.category.add(category1)
        username = "admin"
        password = "admin"        
        User.objects.create_user(username=username, password=password)
        

    def test_product_url(self):
       
       #print(Product.objects.all())
        
        # wysyłamy żądanie GET do adresu URL /api/v1/users
        response = self.client.get('/api/?category=Category1&active=True&name=prod')

        # sprawdzamy, czy otrzymaliśmy odpowiedź 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # sprawdzamy, czy lista zwróconych użytkowników zawiera przynajmniej jeden element
        self.assertGreater(len(response.data), 3)
        # sprawdzamy, czy nazwa pierwszego produktu na liście jest "Product1"   
        self.assertEqual(response.data["results"][0]["name"], "Product1")

    def test_product_slug(self):
        response = self.client.get('/api/Slug1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_invalid_product_slug(self):
        response = self.client.get('/api/invalid/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_login_register_invalid_register(self):
        # przygotowujemy dane do wysłania w żądaniu POST
        data = {
            'username': 'testuser',
            'password': 'testpas'
        }
        #wysyłamy żądanie POST rejestrujące nowego użytkownika
        response = self.client.post('/users/', data)      
       
        # sprawdzamy, czy otrzymaliśmy odpowiedź 201 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #wysyłamy żądanie POST rejestrujące takiego samego użytkownika
        response = self.client.post('/users/', data)      
       
        # sprawdzamy, czy otrzymaliśmy odpowiedź 400 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

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

    def test_post_comment(self):
        # przygotowujemy dane do wysłania w żądaniu POST
        data = {
            'product': 1,
            'body': 'testbody'
        }
       

        user = User.objects.get(username='admin')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('/comments/', data=data)
       
        # sprawdzamy, czy otrzymaliśmy odpowiedź 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment(self):
       
        response = self.client.get('/comments/')
       
        # sprawdzamy, czy otrzymaliśmy odpowiedź 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_post_rent(self):
        # przygotowujemy dane do wysłania w żądaniu POST
        data = {
            'product': 1,
           
        }       

        user = User.objects.get(username='admin')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('/rentproduct/', data=data)
       
        # sprawdzamy, czy otrzymaliśmy odpowiedź 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rent(self):
       
        response = self.client.get('/rentready/')
       
        # sprawdzamy, czy otrzymaliśmy odpowiedź 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_order(self):
        # przygotowujemy dane do wysłania w żądaniu POST
        data = {
            "price":1,
            "city":"Wrocław",
            "street":"Bajeczna 15/20",
            "zipcode":"50-000"
            }

        user = User.objects.get(username='admin')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('/order/', data=data)
       
        # sprawdzamy, czy otrzymaliśmy odpowiedź 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data2 = {
            "order":1,
            "product":1,
            "quantity":1
            }

        response = client.post('/orderproduct/', data=data2)
        # sprawdzamy, czy otrzymaliśmy odpowiedź 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)