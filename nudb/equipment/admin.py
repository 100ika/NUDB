from django import forms
from django.contrib import admin
from .models import AlarmType, Manufacturer, Equipment, EquipmentType, ResponsiblePerson, TechnicalContact, Service, Block, Laboratory, Node, Notification

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class EquipmentAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Equipment
        fields = '__all__'


#admin.site.register(Equipment, EquipmentAdmin)


@admin.register(AlarmType)
class AlarmTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "site")
    list_display_links = ("name",)
    list_filter = ("name", "country",)
    search_fields = ("name", "country",)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "name", "description", "manufacturer", "manual",)
    list_filter = ("name", "manufacturer",)
    search_fields = (
        "name", "type_of_equipment", "manufacturer", "responsible_person"
    )
    list_display_links = ("name", )
    form = EquipmentAdminForm


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


# admin.site.register(EquipmentType)
admin.site.register(ResponsiblePerson)
admin.site.register(TechnicalContact)
admin.site.register(Service)
admin.site.register(Block)
admin.site.register(Laboratory)
admin.site.register(Node)
admin.site.register(Notification)
