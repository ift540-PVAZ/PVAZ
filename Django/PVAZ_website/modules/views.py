from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from django.core import serializers
from .models import Solarpanel
from .models import *

# Create your views here.

def home(request):
    solarpanel = Solarpanel.objects.all()
    return render(request, 'modules/index.html',{ 'solarpanel':solarpanel})
    #return render(request, 'modules/index.html',{ 'performance':performance })
    #return render(request, 'modules/index.html')

def get_data(request, id):
    performance = Performanceparameters.objects.filter(modelid_id = id)
    maps = {}
    for item in performance:
        maps[item.testcondition] = {"performanceid":item.performanceid,"power":item.power, "voltage": item.voltage, "current":item.current,"temperaturecoefficient":item.temperaturecoefficient}
    return JsonResponse({"STC":maps["STC"], "PVUSA":maps["PVUSA"],"PVAZ":maps["PVAZ"]})

def moduleSpecs(request):
    solarpanel = Solarpanel.objects.all()
    return render(request, 'modules/moduleSpecs.html', { 'solarpanel':solarpanel})

def get_spec(request, id):
    specs = Designspecifications.objects.get( designspecificationid  = id)   
    return JsonResponse({"modelnumber": specs.modelnumber,"manufacturer": specs.manufacturer,"size": specs.size,"material": specs.material,"totalnoofcells": specs.totalnoofcells,"encapsulant": specs.encapsulant,"frontdesign": specs.frontdesign,"backdesign": specs.backdesign,"typemodeldesignation": specs.typemodeldesignation,"modelmanufacturingdate": specs.modelmanufacturingdate,"moduletotalarea": specs.moduletotalarea,"moduleweight": specs.moduleweight,"individualcellarea": specs.individualcellarea})

def moduleRequest(request):
    return render(request, 'modules/moduleRequest.html')

def about(request):
    return render(request, 'modules/about.html')

def contact(request):
    return render(request, 'modules/contact.html')