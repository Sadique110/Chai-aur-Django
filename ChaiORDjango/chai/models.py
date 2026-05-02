from django.db import models
from django.utils import timezone


# Create your models here.
class ChaiVerities(models.Model):
    CHAI_TYPES = [
        ("Masala Chai", "Masala Chai"),
        ("Ginger Chai", "Ginger Chai"),
        ("Cardamom Chai", "Cardamom Chai"),
        ("Tulsi Chai", "Tulsi Chai"),
        ("Lemon Chai", "Lemon Chai"),
    ]
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=50, choices=CHAI_TYPES)

