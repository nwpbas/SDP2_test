from django.shortcuts import render
from django.http import HttpResponse
from .models import Multiplication
# Create your views here.

def index(request):
    context = {}
    if "number" in request.GET:
        if request.GET['number'] != '':

            if not Multiplication.objects.filter(number=int(request.GET['number'])):
                obj = Multiplication(number=int(request.GET['number']))
                obj.save()
                context['count'] = Multiplication.objects.filter(number=int(request.GET['number'])).count
            else:
                obj = Multiplication.objects.get(number=int(request.GET['number']))
                obj.count += 1
                obj.save()
            context['multipliction_obj'] = obj
            result = [int(request.GET['number'])*i for i in range(1,13)]
            context['result'] = result
    return render(request, "multiplication/index.html",context)

def stat(request):
    context = {'stat_list': Multiplication.objects.all().order_by('number')}
    return render(request, "multiplication/statistics_multiplication.html",context)
    
    