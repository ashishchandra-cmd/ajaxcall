from django.contrib import admin
from testapp.models import Registation

class AdminRegistation(admin.ModelAdmin):
    list_display=['Name','Phone','Email','Password']

admin.site.register(Registation, AdminRegistation)    
