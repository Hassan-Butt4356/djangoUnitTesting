from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from myapp.views import (
    ItemListView,
    itemDetail,
    CreateItem,
    UpdateItem,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ItemListView.as_view(),name='list' ),
    path('detail/<str:pk>/',itemDetail,name='detail' ),
    path('update/<str:pk>/',UpdateItem.as_view(),name='update' ),
    path('create/',CreateItem.as_view(),name='create' ),
    path('login/',LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
]
