from django.db import models

# Create your models here.


class myown(models.Model):
    U_id = models.BigAutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Desc = models.CharField(max_length=200)
    Date = models.DateTimeField(auto_now_add=True)
