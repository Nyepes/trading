from django import forms
from django.forms import ModelForm
from .models import Trade
from datetime import date, datetime,timezone

class TradeForm(ModelForm):
    class Meta:
        today = date.today()
        # now = datetime.now().
        # today.date().
        model = Trade
        fields = (
            "date","time","ticker","entry_price","stop_loss",
            "take_profit","shares","locate_fees","exit_price",
            "commission","wl","profit","screenshot","comments")

        labels = {
            "date": 'Date',
            "time": 'Time',
            "ticker": '',
            "entry_price": '',
            "stop_loss": '',
            "take_profit": '',
            "shares": '',
            "locate_fees": '',
            "exit_price": '',
            "commission": '',
            "wl": '',
            "profit": '',
            "screenshot": 'Screenshot',
            "comments": ''
        }
        widgets = {
            "date": forms.DateInput(attrs={'class':'form-control','required': 'True','type':'date'}),
            "time": forms.TimeInput(attrs={'class':'form-control','required': 'True','type':'time','min':'08:00', 'max':'03:00'}),
            "ticker": forms.TextInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Ticker'}),
            "entry_price": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Entry Price'}),
            "stop_loss": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Stop Loss'}),
            "take_profit": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Take Profit'}),
            "shares": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Number of Shares'}),
            "locate_fees": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Locate Fees'}),
            "exit_price": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Exit Price'}),
            "commission": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Commission'}),
            "wl": forms.TextInput(attrs={'class':'form-control','required': 'True', 'placeholder':'W/L'}),
            "profit": forms.NumberInput(attrs={'class':'form-control','required': 'True', 'placeholder':'Profit'}),
            "screenshot": forms.FileInput(attrs={'class':'form-control'}),
            "comments": forms.Textarea(attrs={'class':'form-control','required': 'True', 'placeholder':'Comments'})
        }