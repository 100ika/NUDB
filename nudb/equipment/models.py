from django.db import models
from datetime import date

# Create your models here.


class AlarmType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField("trouble")

    class Meta:
        verbose_name = ("Alarm Type")
        verbose_name_plural = ("Alarm Types")

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=50)
    country = models.CharField("Country", max_length=50)
    email = models.EmailField("Email", max_length=254)
    site = models.URLField("Site", max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    id = models.AutoField('Equipment type', primary_key=True)
    name = models.CharField("Type of equipment",
                            max_length=150, default='Refrigirator')

    class Meta:
        verbose_name = "Equipment Type"
        verbose_name_plural = "Equipment Types"

    def __str__(self):
        return self.name

  #  def get_absolute_url(self):
  #      return reverse("EquipmentType_detail", kwargs={"pk": self.pk})


class ResponsiblePerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=150)
    position = models.CharField("Position", max_length=150)
    email = models.EmailField("Email", max_length=254)
    office = models.CharField("Office", max_length=6)
    phone = models.CharField("Phone", max_length=16)
    work_phone = models.CharField("Work phone", max_length=8)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Responsible Person"
        verbose_name_plural = "Responsible Persons"

    def __str__(self):
        return self.name

   # def get_absolute_url(self):
   #     return reverse("ResponsiblePerson_detail", kwargs={"pk": self.pk})


class TechnicalContact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=150)
    position = models.CharField("Position", max_length=150)
    email = models.EmailField("Email", max_length=254)
    office = models.CharField("Office", max_length=6)
    phone = models.CharField("Phone", max_length=16)
    work_phone = models.CharField("Work phone", max_length=8)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Technical Contact"
        verbose_name_plural = "Technical Contacts"

    def __str__(self):
        return self.name

 #   def get_absolute_url(self):
  #      return reverse("TechnicalContact_detail", kwargs={"pk": self.pk})


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_equipment = models.ManyToManyField(
        EquipmentType, verbose_name="Type of equipment")
    name = models.CharField("Model", max_length=50)
    description = models.TextField("Description")
    serial_number = models.CharField(
        "Serial number", max_length=100, unique=True)
    manufacturer = models.ForeignKey(
        Manufacturer, verbose_name="Manufacturer", on_delete=models.CASCADE
    )
    manual = models.FileField("Manual", upload_to='manual/')
    inventory_number = models.CharField(
        "Inventory number", max_length=20, unique=True)
    photo = models.ImageField("Photo", null=True, blank=True)
    """service = models.ForeignKey(
        Service, verbose_name="Service", on_delete=models.CASCADE
        )"""
    responsible_person = models.ManyToManyField(
        ResponsiblePerson, verbose_name="Responsible Person")
    technical_contact = models.ManyToManyField(
        TechnicalContact, verbose_name="Technical Contact")
    slug = models.SlugField("url", max_length=150, unique=True)

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    equipment = models.ForeignKey(
        Equipment, verbose_name="equipment", on_delete=models.CASCADE)
    last_service = models.DateField("last service", default=date.today)
    next_service = models.DateField(
        'Next service', null=False, help_text="Please use following format: <em>YYYY-MM-DD</em>.")
    spares = models.CharField("Spares", max_length=150)
    what_is_done = models.TextField("What is done")
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.equipment


class Block(models.Model):
    id = models.AutoField(primary_key=True)
    block = models.CharField("Block", max_length=3)

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"

    def __str__(self):
        return self.block


class Laboratory(models.Model):
    id = models.AutoField(primary_key=True)
    block = models.ManyToManyField(Block, verbose_name="Block")
    floor = models.CharField("Floor", max_length=2)
    room = models.CharField("Room", max_length=6)  # primary_key = True,
    department = models.CharField(
        'Departament', max_length=64, null=True, blank=True)
    room_type = models.CharField(max_length=32, null=True, blank=True)
    gases = models.CharField(null=True, blank=True,
                             max_length=64, default='None')

    class Meta:
        verbose_name = "Laboratory"
        verbose_name_plural = "Laboratories"

    def __unicode__(self):  # unicode?
        return f"{self.block} - {self.room}"


class Node(models.Model):
    id = models.AutoField(primary_key=True)
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
        "Date of installation", default=date.today
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
    id = models.AutoField(primary_key=True)
    node = models.ForeignKey(
        Node, verbose_name="Node", on_delete=models.CASCADE
    )
    time = models.DateTimeField('Time', auto_now=True)
    type = models.ManyToManyField(
        AlarmType, verbose_name="Type")
    checked = models.BooleanField("Checked", default=False)
    mailWasSent = models.BooleanField("Inform", default=False)

    class Meta:
        verbose_name = ("Notification")
        verbose_name_plural = ("Notifications")

    def __str__(self):
        return self.node
