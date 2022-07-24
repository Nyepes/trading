import decimal
import math
from django.db import models

class Trade(models.Model):
    equity = decimal.Decimal(2000.00) #TODO
    date=models.DateField("Event Date", blank=True)
    time = models.TimeField("Time", blank=True)
    ticker=models.CharField("Ticker", max_length=10, null = True, blank=True)
    entry_price=models.DecimalField("Entry Price",decimal_places=2, max_digits=10, null = True, blank=True)
    stop_loss=models.DecimalField("Stop Loss",decimal_places=2, max_digits=10, null = True, blank=True)
    #take_profit=models.DecimalField("Take Profit",decimal_places=2, max_digits=10, null = True, blank=True)
    #shares=models.IntegerField("Number of Shares", null = True, blank=True)
    locate_fees=models.DecimalField("Locate Fees",decimal_places=2, max_digits=10, null=True,blank=True)
    exit_price=models.DecimalField("Exit Price",decimal_places=2, max_digits=10, null = True, blank=True)
    commission = models.DecimalField("Commission", decimal_places=2, max_digits=10, null = True, blank=True)
    trade_type = models.CharField("Trade Type",max_length=30, null = True, blank=True)
    #profit = models.DecimalField("Profit", decimal_places=2, max_digits=10, null = True, blank=True)
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
        return 10 #TODO
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
