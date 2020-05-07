from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Wishlist(models.Model):
	owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, default=None)
	