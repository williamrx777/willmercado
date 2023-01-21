from django.urls import path
from . import views
urlpatterns = [
    path('novo_produto', views.novo_produto, name='novo_produto'),
    path('seus_produtos', views.seus_produtos, name='seus_produtos'),
    path('remove_produto/<int:id>', views.remove_produto, name='remove_produto'),
]