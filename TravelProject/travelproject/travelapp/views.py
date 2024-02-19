from django.shortcuts import render
from .models import Place, Men

def demo(request):
    obj = Place.objects.all()
    men = Men.objects.all()
    return render(request, "index.html", {'result':obj , 'men': men})


