from django.test import TestCase,Client
from django.urls import reverse
from myapp.views import (
    ItemListView,
    itemDetail,
    CreateItem,
)
from myapp.models import Item

class TestViews(TestCase):
    def setUp(self): 
        self.client=Client()

        self.list_url=reverse('list')
        
        self.item1=Item.objects.create(title='item1',price=1000,detail="This is for testdb")
        self.detail_url=reverse('detail',args=[self.item1.pk])

        self.update_url=reverse('update',args=[self.item1.pk])
        
        self.create_url=reverse('create')

    def test_list_view(self):
        response=self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'myapp/list.html')

    def test_detail_view(self):
        response=self.client.get(self.detail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'myapp/detail.html')
    
    def test_create_view(self):
        response=self.client.post(self.create_url,{
            'title':'item2',
            'price':2000,
            'detail':'This is detail for post request in testdb'
        })

        self.assertEquals(response.status_code,302)
        self.assertEquals(Item.objects.order_by('-pk').first().title,'item2')

    def test_update_view(self):
        response=self.client.post(self.update_url,{
            'title':'item3',
            'price':4000,
            'detail':"Updated Detail"
        })

        self.assertEquals(response.status_code,302)
        self.assertEquals(Item.objects.first().title,'item3')
        self.assertEquals(Item.objects.first().price,4000)
        self.assertEquals(Item.objects.first().detail,'Updated Detail')