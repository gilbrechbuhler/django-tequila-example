from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User)
    quantity = models.PositiveIntegerField(default=1)
    text = models.TextField()
