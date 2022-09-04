from django.urls import path
from business.views import stores_list, create_store, opinions_list, create_opinion, menu, about
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('stores_list/', stores_list, name='stores_list'),
    path('new_store/', create_store, name='new_store'), #ojooooooooo
    path('new_opinion/', create_opinion, name='new_opinion'), #ojooooooooo
    path('opinions_list/', opinions_list, name='opinions_list'),
    path('about/', about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)