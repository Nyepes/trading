from django.shortcuts import render, redirect
from events.models import Trade
from .forms import TradeForm
def home(request):
    return render(request, 'events/home.html', {})

def add_trade(request):
    #form = TradeForm(request.POST)
    submitted = False
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form = TradeForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_trade.html', {'form':form})
