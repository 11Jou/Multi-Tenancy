from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Item

class YourAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        login_url = reverse('login') 
        response = self.client.post(login_url, {'username': 'testuser', 'password': 'testpassword'})
        print(response.content)
        self.assertEqual(response.status_code, 200)  

    def test_retrive_items(self):
        self.client.login(username='testuser', password='testpassword')
        get_item = reverse('items_api')  
        response = self.client.get(get_item)
        self.assertEqual(response.status_code, 200)  

