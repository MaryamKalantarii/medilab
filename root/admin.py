from django.contrib import admin
from .models import Services,HealthService,Doctor,Skills
# Register your models here.



admin.site.register(Services)
admin.site.register(HealthService)
admin.site.register(Doctor)
admin.site.register(Skills)