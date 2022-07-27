from django import forms
from django.forms import ModelForm
from .models import Trade, Profile
from django.utils.timezone import now
from datetime import date, datetime,timezone

class TradeForm(ModelForm):
    class Meta:
        today = date.today()
        # now = datetime.now().
        # today.date().
        model = Trade
        # fields = (
        #     "date","time","ticker","entry_price","stop_loss",
        #     "take_profit","shares","locate_fees","exit_price",
        #     "commission","wl","profit","screenshot","comments")
        fields = (
            "date","time","ticker","entry_price","stop_loss",
            "locate_fees","exit_price","commission","trade_type",
            "screenshot","comments")

        labels = {
            "date": 'Date',
            "time": 'Time',
            "ticker": 'Ticker',
            "entry_price": 'Entry Price',
            "stop_loss": 'Stop Loss',
            # "take_profit": '',
            # "shares": '',
            "locate_fees": 'Locate Fees',
            "exit_price": 'Exit Price',
            "commission": 'Commission',
            "trade_types": 'Strategy',
            #"profit": '',
            "screenshot": 'Screenshot',
            "comments": ''
        }
        widgets = {
            "date": forms.DateInput(attrs={'class':'form-control','required': 'True','type':'date'}),
            "time": forms.TimeInput(attrs={'class':'form-control','required': 'True','type':'time'}),
            "ticker": forms.TextInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Ticker'}),
            "entry_price": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Entry Price'}),
            "stop_loss": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Stop Loss'}),
            # "take_profit": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Take Profit'}),
            # "shares": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Number of Shares'}),
            "locate_fees": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Locate Fees'}),
            "exit_price": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Exit Price'}),
            "commission": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Commission'}),
            "trade_type": forms.Select(attrs={'class':'form-control','required': 'True', 'placeholder':'Type of Trade'}, choices=[("Channel Trading","Channel Trading"),("Short Into Resistance","Short Into Resistance")]),
            #"profit": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Profit'}),
            "screenshot": forms.FileInput(attrs={'class':'form-control'}),
            "comments": forms.Textarea(attrs={'class':'form-control','required': 'True', 'placeholder':'Comments'})
        }