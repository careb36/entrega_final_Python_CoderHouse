from django.shortcuts import render, redirect
from business.models import Stores, Opinions
from business.forms import Forms_stores, Forms_opinions

def menu(request):
        return render(request, 'business/menu.html', context={})


def create_store(request):
    
    if request.method == 'POST':
        form = Forms_stores(request.POST)

        if form.is_valid():
            Stores.objects.create(
                name = form.cleaned_data['name'],
                address = form.cleaned_data['address'],
                phone_number = form.cleaned_data['phone_number'],
                schedules = form.cleaned_data['schedules'],
            )
            
            return redirect(stores_list)

    elif request.method == 'GET':
        form = Forms_stores()
        context = {'form':form}
        return render(request, 'business/new_store.html', context=context)


def stores_list(request):
    stores = Stores.objects.all() #Trae todos
    context = {
        'stores':stores
    }
    return render(request, 'business/stores_list.html', context=context)


def create_opinion(request):
    
    if request.method == 'POST':
        form = Forms_opinions(request.POST)

        if form.is_valid():
            Opinions.objects.create(
                name = form.cleaned_data['name'],
                calification = form.cleaned_data['calification'],
                comment = form.cleaned_data['comment'],
            )
            
            return redirect(opinions_list)

    elif request.method == 'GET':
        form = Forms_opinions()
        context = {'form':form}
        return render(request, 'business/new_opinion.html', context=context)

def opinions_list(request):
    opinions = Opinions.objects.all() #Trae todos
    context = {
        'opinions':opinions
    }
    return render(request, 'business/opinions_list.html', context=context)


def about (request):
    return render(request, 'business/about.html', context={})
