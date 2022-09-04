from django.urls import path
from products.views import List_products, Create_product, Update_product, Delete_product, \
    Search_product, Detail_product, list_delete_products, list_update_products

urlpatterns = [
    path('new_product/', Create_product.as_view(), name='Create_product'),
    path('products_list/', List_products.as_view(), name='List_products'),  
    path('delete_product/', list_delete_products.as_view(), name='List_Delete_product'),  
    path('delete_product/<int:pk>/', Delete_product.as_view(), name='Delete_product'),
    path('update_product/', list_update_products.as_view(), name='List_Update_product'), 
    path('update_product/<int:pk>/', Update_product.as_view(), name='update_product'),
    path('detail_products/<int:pk>/', Detail_product.as_view(), name='detail_product'),
    path('search_product/', Search_product.as_view(), name='search_product'),
]