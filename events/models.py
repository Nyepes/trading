from datetime import datetime
import decimal
import math
from time import pthread_getcpuclockid, time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initial_equity = models.DecimalField("Initial Equity", blank=True,null=True,max_digits=10,decimal_places=2,default=decimal.Decimal(0.00))

    @property
    def total_equity(self):
        trades = Trade.objects.filter(page_user=self)
        total_profit= 0
        for trade in trades:
            total_profit += trade.profit
        return self.initial_equity+total_profit

    @property 
    def win_p(self):
        trades = Trade.objects.filter(page_user=self)
        w=0
        n=0
        l=0
        for trade in trades:
            if trade.wl == 'Win':
                w+=1
            elif trade.wl =='Neutral':
                n+=1
            else:
                l+=1
        total_amount=trades.count()
        if total_amount ==0:
            return (0,0,0)
        return (round(w/total_amount*100,2),round(n/total_amount*100,2),round(l/total_amount*100,2))
    @property 
    def risk_reward_ratio(self):
        trades = Trade.objects.filter(page_user=self)
        sum = 0
        for trade in trades:
            if trade.wl=='Win':
                sum += trade.risk_reward
        a =trades.count()
        if a == 0:
            return 0
        return round(sum/trades.count(),2)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Trade(models.Model):
    page_user=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    equity_at_time = models.DecimalField("Equity at Time",decimal_places=2, max_digits=10, null = True, blank=True)
    date=models.DateField("Event Date", blank=True,default=timezone.now)
    time = models.TimeField("Time", blank=True, default=datetime.today().time())
    ticker=models.CharField("Ticker", max_length=10, null = True, blank=True)
    entry_price=models.DecimalField("Entry Price",decimal_places=2, max_digits=10, null = True, blank=True)
    stop_loss=models.DecimalField("Stop Loss",decimal_places=2, max_digits=10, null = True, blank=True)
    locate_fees=models.DecimalField("Locate Fees",decimal_places=2, max_digits=10, null=True,blank=True, default=0)
    exit_price=models.DecimalField("Exit Price",decimal_places=2, max_digits=10, null = True, blank=True)
    commission = models.DecimalField("Commission", decimal_places=2, max_digits=10, null = True, blank=True, default=0)
    trade_type = models.CharField("Trade Type",max_length=30, null = True, blank=True)
    screenshot = models.ImageField("Screenshot", null=True,blank=True)
    comments=models.TextField("Comments", blank=True, null = True)
    num_shares = models.PositiveIntegerField ("Number of Shares", max_length=10, default=0,null = True, blank=True)
    take_profit = models.DecimalField("Commission", decimal_places=2, max_digits=10,default=0,null = True, blank=True)

    @property
    def profit(self):
        if self.trade_type == 'Channel Trading':
            return (self.exit_price-self.entry_price)*self.num_shares - self.locate_fees - self.commission
        elif self.trade_type == 'Short Into Resistance':
            return -1*(self.exit_price-self.entry_price)*self.num_shares - self.locate_fees - self.commission
        return 0
    @property
    def wl(self):
        if self.profit < 0:
            return "Loss"
        elif self.profit == 0:
            return "Neutral"
        else:
            return "Win"
    @property
    def risk_reward(self):
        if self.take_profit != self.entry_price:
            return (float(self.entry_price)-float(self.stop_loss))/(float(self.take_profit)-float(self.entry_price))
        return 0