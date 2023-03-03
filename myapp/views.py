from django.shortcuts import render,get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Item
from .forms import ItemCreateForm
from django.urls import reverse_lazy

class ItemListView(ListView):
    model=Item
    template_name='myapp/list.html'
    queryset=Item.objects.all()


def itemDetail(request,pk):
    item=get_object_or_404(Item,id=pk)
    return render(request,'myapp/detail.html',{'object':item})

class CreateItem(CreateView):
    model=Item
    form_class=ItemCreateForm
    template_name='myapp/create.html'
    success_url=reverse_lazy('list')

class UpdateItem(UpdateView):
    model=Item
    template_name='myapp/update.html'
    form_class=ItemCreateForm
    success_url=reverse_lazy('list')