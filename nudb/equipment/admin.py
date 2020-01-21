from django.contrib import admin
from .models import AlarmType, Manufacturer, Equipment, Service, Block, Laboratory, Node, Notification

# Register your models here.
admin.site.register(AlarmType)
admin.site.register(Manufacturer)
admin.site.register(Equipment)
admin.site.register(Service)
admin.site.register(Block)
admin.site.register(Laboratory)
admin.site.register(Node)
admin.site.register(Notification)
