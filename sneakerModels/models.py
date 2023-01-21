from django.db import models


class SneakerModels(models.Model):
    brand = models.ManyToManyField(
        'brands.Brand', related_name="models",  blank=True)
    model = models.CharField(max_length=100)    
    name = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    release_year = models.CharField(max_length=20)
    retail_price = models.CharField(max_length=20)
    cover_image = models.CharField(max_length=300)
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name="albums",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.name} - {self.colorway} - {self.size} - {self.release_year} - {self.retail_price}"