from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Drink
from .calculation import calculatePrice



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def orderDrink(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    cafe_list = Drink.objects.order_by("name")

    return render(
        request,
        'app/orderDrink.html',
        {
           'cafe_list': cafe_list,  
        }
    )

def createOrder(request):

    id = int(request.POST['drink'])
    drinkObject = Drink.objects.get(pk=id)
    quantity= int(request.POST['quantity'])

    price = calculatePrice(drinkObject,quantity)

    return render(
        request, 
        "app/createOrder.html", 
        {
            'result': price,
            'drink' :drinkObject,
            'quantity' : quantity
            }
        )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

