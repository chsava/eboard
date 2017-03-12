from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Test

def index(request):
    numbers = Test.objects.order_by('number')
    #numlist = ["%d&nbsp;%s&nbsp;%s" % (n.number, n.english_name, n.spanish_name) for n in numbers]
    #output = "<br>".join(numlist)
    #return HttpResponse(output)
    template = loader.get_template('eboard/index.html')
    context = {
        'numbers_list': numbers,
    }
    return HttpResponse(template.render(context, request))
