from django.db import models
from datetime import date

# Create your models here.

class AlarmType(models.Model):
    name = models.TextField("trouble")
    
    class Meta:
        verbose_name = ("AlarmType")
        verbose_name_plural = ("AlarmTypes")

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField("Name", max_length=50)
    country = models.CharField("Country", max_length=50)
    email = models.EmailField("", max_length=254)
    site = models.URLField('Site', max_length=32,null=True,blank=True)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField("Model", max_length=50)
    serial_number = models.CharField("Serial number", max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer, verbose_name="Manufacturer", on_delete=models.CASCADE
        )
    manual = models.FileField("Manual", upload_to='manual/')
    inventory_number = models.CharField("Inventory number", max_length=20)
    photo = models.ImageField("Photo", null=True, blank=True)
    """service = models.ForeignKey(
        Service, verbose_name="Service", on_delete=models.CASCADE
        )"""

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"

    def __str__(self):
        return self.name


class Service(models.Model):
    equipment = models.ForeignKey(Equipment, verbose_name="equipment", on_delete=models.CASCADE)
    last_service = models.DateField("last service", default=date.today)
    #next_service = 
    spares = models.CharField("Spares", max_length=150)
    what_is_done = models.TextField("What is done")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.equipment


class Block(models.Model):
    block = models.CharField("Block", max_length=3)
    
    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"

    def __str__(self):
        return self.block


class Laboratory(models.Model):
    block = models.ManyToManyField(Block, verbose_name="Block")
    floor = models.CharField("Floor", max_length=2)
    room = models.CharField("Room", primary_key = True, max_length=6)
    department = models.CharField('Departament', max_length=64, null=True, blank=True)
    room_type = models.CharField(max_length=32, null=True, blank=True)
    gases = models.CharField(null=True, blank=True, max_length=64)

    
    class Meta:
        verbose_name = "Laboratory"
        verbose_name_plural = "Laboratories"

    def __unicode__(self): #unicode?
        return f"{self.block} - {self.room}"


class Node(models.Model):

    name = models.CharField('name', max_length=50, unique=True)
    equipment = models.ForeignKey(
        Equipment, verbose_name="Equipment", on_delete=models.CASCADE
        )
    lab = models.ManyToManyField(Laboratory, verbose_name="Laboratory")
    temp1 = models.FloatField("Temp-1")
    temp2 = models.FloatField("Temp-2")
    temp3 = models.FloatField("Temp-3")
    leak1 = models.BooleanField("Leak-1", default=False)
    leak2 = models.BooleanField("Leak-2", default=False)
    leak3 = models.BooleanField("Leak-3", default=False)
    date_of_installation = models.DateField(
        "Date of installation", default = date.today
        )
    date_of_last_service = models.DateField(
        "Date of last service", default=date.today
        )
    #date_of_next_service = models.DateField("Date of next service", default=date.today)
    inventory_number = models.CharField("Inventory nimber", max_length=20)

    class Meta:
        verbose_name = "Node"
        verbose_name_plural = "Nodes"

    def __str__(self):
        return self.name


class Notification(models.Model):
    node = models.ForeignKey(
        Node, verbose_name="Node", on_delete=models.CASCADE
        )
   # time = 
    type = models.ManyToManyField(
        AlarmType, verbose_name="Type")
    checked = models.BooleanField("Checked", default=False)
    mailWasSent = models.BooleanField("Inform", default=False)

    class Meta:
        verbose_name = ("Notification")
        verbose_name_plural = ("Notifications")

    def __str__(self):
        return self.node



