from django.test import SimpleTestCase
from django.urls import reverse,resolve
from myapp.views import (
    ItemListView,
    itemDetail,
    CreateItem,
    UpdateItem,
)

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
class TestUrls(SimpleTestCase):

    def test_list_url(self):
        url=reverse('list')
        self.assertEquals(resolve(url).func.view_class,ItemListView)

    def test_detail_url(self):
        url=reverse('detail',args=[1])
        self.assertEquals(resolve(url).func,itemDetail)

    def test_create_url(self):
        url=reverse('create')
        self.assertEquals(resolve(url).func.view_class,CreateItem)

    def test_login_url(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func.view_class,LoginView)

    def test_logout_url(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func.view_class,LogoutView)

    def test_update_url(self):
        url=reverse('update',args=[1])
        self.assertEquals(resolve(url).func.view_class,UpdateItem)