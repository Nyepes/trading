import decimal
import math
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initial_equity = models.DecimalField("Initial Equity",decimal_places=2, max_digits=10, blank=True, null=True,default=decimal.Decimal(0.0))
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Trade(models.Model):
    page_user=models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    equity = decimal.Decimal(2000.00) #TODO change to user
    date=models.DateField("Event Date", blank=True)
    time = models.TimeField("Time", blank=True)
    ticker=models.CharField("Ticker", max_length=10, null = True, blank=True)
    entry_price=models.DecimalField("Entry Price",decimal_places=2, max_digits=10, null = True, blank=True)
    stop_loss=models.DecimalField("Stop Loss",decimal_places=2, max_digits=10, null = True, blank=True)
    locate_fees=models.DecimalField("Locate Fees",decimal_places=2, max_digits=10, null=True,blank=True)
    exit_price=models.DecimalField("Exit Price",decimal_places=2, max_digits=10, null = True, blank=True)
    commission = models.DecimalField("Commission", decimal_places=2, max_digits=10, null = True, blank=True)
    trade_type = models.CharField("Trade Type",max_length=30, null = True, blank=True)
    screenshot = models.ImageField("Screenshot", null=True,blank=True)
    comments=models.TextField("Comments", blank=True, null = True)

    @property
    def num_shares(self):
        if self.entry_price-self.stop_loss !=  0:
            return math.floor((float(self.equity)*0.015)/abs((float(self.entry_price)-float(self.stop_loss))))
        else: 
            return 0
    @property
    def take_profit(self):
        return round((abs((float(self.entry_price)-float(self.stop_loss))*2+float(self.entry_price))),2)
    @property
    def profit(self):
        if self.trade_type == 'Channel Trading':
            return (self.exit_price-self.entry_price)*self.num_shares - self.locate_fees - self.commission
        elif self.trade_type == 'Short Into Resistance':
            return -1*(self.exit_price-self.entry_price)*self.num_shares - self.locate_fees - self.commission
    @property
    def wl(self):
        if self.trade_type == "Short":
            if self.profit > 0:
                return "Loss"
            elif self.profit == 0:
                return "Neutral"
            else:
                return "Win"
        else:
            if self.profit < 0:
                return "Loss"
            elif self.profit == 0:
                return "Neutral"
            else:
                return "Win"