from django.shortcuts import render
from django.views.generic.base import View

from .models import Equipment
# Create your views here.

class EquipmentView(View):
    def get(self, request):
        equipment = Equipment.objects.all()
        return render(request, "equipment/equipment_list.html", {"equipment_list":equipment})

#class  


"""def index(request):#создаем свою функцию
    context = {}#с помощью словаря можем передать модель и форму в шаблон HTML
    return render(request, 'equipment/index.html', context)"""
