from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'modules/index.html')

def moduleSpecs(request):
    return render(request, 'modules/moduleSpecs.html')

def moduleRequest(request):
    return render(request, 'modules/moduleRequest.html')

def about(request):
    return render(request, 'modules/about.html')

def contact(request):
    return render(request, 'modules/contact.html')