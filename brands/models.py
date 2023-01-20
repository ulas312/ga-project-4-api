from django.db import models

class Brand(models.Model): 
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand_name}"