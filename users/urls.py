from django.urls import path
from .views import user_list, borne_list, ombriere_list, home
from . import views

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('products/', views.products_view, name='products'),
    path('', home, name='home'),
]
