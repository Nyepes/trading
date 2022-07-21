from django.shortcuts import render, redirect
from events.models import Trade
from .forms import TradeForm
def home(request):
    return render(request, 'events/home.html', {})

def add_trade(request):
    submitted = False
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('trade_log')
    else:
        form = TradeForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_trade.html', {'form':form})

def trade_log(request):
    trades = Trade.objects.all()
    return render(request, 'events/trade_log.html', {'all_trades':trades})

def trade(request,trade_id):
    trade = Trade.objects.get(pk=trade_id)
    return render(request,'events/detailed_trade.html', {'trade':trade})