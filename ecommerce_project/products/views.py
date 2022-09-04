from urllib import request
from django.views.generic import ListView, DetailView, CreateView, DeleteView, \
    UpdateView, DetailView, TemplateView

from .models import Products
from .forms import Forms_products
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


'''
CREATE PRODUCTS VIEW
'''
class Create_product(CreateView):
    form_class = Forms_products
    template_name = 'products/new_product.html'
    success_url = '/products/products_list/'

'''
LIST PRODUCTS VIEW
'''
class List_products(ListView):
    model = Products
    template_name = 'products/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['products'].order_by('name')
        return context


'''
DELETE PRODUCTS VIEW
'''
class Delete_product(DeleteView):
    model = Products
    success_url = '/products/products_list/' 
    
    def delete (self, request, pk):
        if request.user.is_authenticathed and request.user.is_superuser:

            product = self.get_object(pk)
            print("producto", product)
            product.delete()
            return HttpResponseRedirect('/products/products_list/')
        
        return redirect('login')

class list_delete_products(ListView):
    model = Products
    template_name = 'products/delete_products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['products'].order_by('name')
        context ['is_delete'] = True
        return context


'''
UPDATE PRODUCTS VIEW
'''
class Update_product(UpdateView):
    
        model = Products
        fields = '__all__'
        success_url = '/products/products_list/'
        template_name = 'products/update_product.html'


class list_update_products(ListView):
    model = Products
    template_name = 'products/update_products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['products'] = context['products'].order_by('name')
        context ['is_update'] = True
        return context


class Detail_product(DetailView):
    model = Products
    template_name = 'products/detail_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['products']
        return context


'''
SEARCH PRODUCTS VIEW
'''
class Search_product(TemplateView):
    model = Products
    template_name = 'products/search_product.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('search', '')
        print("query",query)
        self.products = Products.objects.filter(name__icontains=query)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.products
        return context





