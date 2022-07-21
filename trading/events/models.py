from django.db import models

class Trade(models.Model):
    date=models.DateField("Event Date", blank=True)
    time = models.TimeField("Time", blank=True)
    ticker=models.CharField("Ticker", max_length=10, null = True, blank=True)
    entry_price=models.DecimalField("Entry Price",decimal_places=2, max_digits=10, null = True, blank=True)
    stop_loss=models.DecimalField("Stop Loss",decimal_places=2, max_digits=10, null = True, blank=True)
    take_profit=models.DecimalField("Take Profit",decimal_places=2, max_digits=10, null = True, blank=True)
    shares=models.IntegerField("Number of Shares", null = True, blank=True)
    locate_fees=models.DecimalField("Locate Fees",decimal_places=2, max_digits=10, null=True,blank=True)
    exit_price=models.DecimalField("Exit Price",decimal_places=2, max_digits=10, null = True, blank=True)
    commission = models.DecimalField("Commission", decimal_places=2, max_digits=10, null = True, blank=True)
    wl = models.CharField("W/L",max_length=2, null = True, blank=True)
    profit = models.DecimalField("Profit", decimal_places=2, max_digits=10, null = True, blank=True)
    screenshot = models.ImageField("Screenshot", null=True,blank=True)
    comments=models.TextField("Comments", blank=True, null = True)



