import decimal
import math
from django.db import models
from .models import Trade
from django.contrib.auth.models import User

class PageUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    initial_equity = models.DecimalField("Initial Equity",decimal_places=2, max_digits=10, blank=True)
    user_trades=models.ForeignKey(Trade, blank = True, null= False,on_delete=models.CASCADE)