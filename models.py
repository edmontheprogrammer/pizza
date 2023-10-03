from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_zip_code = models.CharField(max_length=100)
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    comments = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.topping1 + ', ' + self.topping2
