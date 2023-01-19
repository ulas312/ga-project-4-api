from django.db import models

class Brand(models.Model): 
    sneaker_brand = models.CharField(max_length=50)
    sneaker_model = models.CharField(max_length=50)
    sneaker_name = models.CharField(max_length=100)
    sneaker_colorway = models.CharField(max_length=100)
    sneaker_size = models.CharField(max_length=20)
    release_year = models.CharField(max_length=20)
    retail_price = models.CharField(max_length=20)
    cover_image = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.sneaker_brand} - {self.sneaker_model} - {self.sneaker_name} - {self.sneaker_colorway} - {self.sneaker_size} - {self.release_year} - {self.retail_price}"