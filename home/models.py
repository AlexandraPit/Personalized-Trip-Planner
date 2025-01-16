from django.db import models

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # City name, must be unique
    country = models.CharField(max_length=100, blank=True, null=True)  # Country name (optional)

    class Meta:
        db_table = 'city'  # Ensure this matches the table name in your database


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)  # Use ImageField to manage image uploads

    class Meta:
        db_table = 'images'

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    city = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city_id')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, db_column='image_id')

    class Meta:
        db_table = 'activity'  # Ensure this is correct
