from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from products.models import Product




def api_home(request):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    #mode data
    if model_data:
        data = model_to_dict(model_data)
    return JsonResponse(data)
