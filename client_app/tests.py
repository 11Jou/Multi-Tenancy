from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from app.models import Client 

class YourAppTestCase(TenantTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.tenant = Client(schema_name='public', name='Test Tenant')
        cls.tenant.save()

    def setUp(self):
        self.client = TenantClient(self.tenant)
        self.client.login(username='testuser', password='testpassword')

    def test_login(self):
        login_url = reverse('login') 
        response = self.client.post(login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    def test_retrieve_items(self):
        get_item_url = reverse('items_api')
        response = self.client.get(get_item_url)
        self.assertEqual(response.status_code, 200)
