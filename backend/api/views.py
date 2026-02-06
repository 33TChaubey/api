from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from backend.products.models import Product




def api_home(request):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    #mode data
    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)
