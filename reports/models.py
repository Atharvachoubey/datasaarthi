from django.db import models
from django.contrib.auth.models import User



class Report(models.Model):

    # 🔹 User entered unique ID
    custom_id = models.CharField(max_length=50, unique=True)

    # 🔹 Basic Details
    house_no = models.CharField(max_length=50)
    address = models.TextField()
    village = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)

    # 🔹 Type (PVR options)
    TYPE_CHOICES = [
        ('PVR01', 'PVR01'),
        ('PVR02', 'PVR02'),
        ('PVR03', 'PVR03'),
        ('PVR04', 'PVR04'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    # 🔹 Sub Type (only for PVR03 → Flat / House)
    SUB_TYPE_CHOICES = [
        ('Flat', 'Flat'),
        ('House', 'House'),
    ]
    sub_type = models.CharField(max_length=10, choices=SUB_TYPE_CHOICES, blank=True, null=True)

    # 🔹 LIC Agent
    lic_agent_name = models.CharField(max_length=100)

    # 🔹 Estimate Status
    ESTIMATE_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]
    estimate_status = models.CharField(max_length=10, choices=ESTIMATE_STATUS_CHOICES)

    # 🔹 Client Mobile
    client_mobile = models.CharField(max_length=15)

    # 🔹 File Status
    FILE_STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Not Submitted', 'Not Submitted'),
    ]
    file_status = models.CharField(max_length=15, choices=FILE_STATUS_CHOICES)

    # 🔹 Date
    date = models.DateField()

    def __str__(self):
        return f"{self.custom_id} - {self.client_name}"
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
