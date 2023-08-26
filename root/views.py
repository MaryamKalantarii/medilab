from django.shortcuts import render
from .models import Services,HealthService,Doctor

# Create your views here.

def home(request):
    services=Services.objects.filter(status=True)
    healthService=HealthService.objects.filter(status=True)
    doctor = Doctor.objects.filter(status=True)
    context={
        'service': services,
        'healthService':healthService,
        'doctor':doctor,
    }
    return render(request,"root/index.html",context=context)





