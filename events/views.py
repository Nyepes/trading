from django.shortcuts import render, redirect
from events.models import Trade
from .forms import TradeForm
def home(request):
    return redirect('trade_log')

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
def edit_trade(request, trade_id):
    trade = Trade.objects.get(pk=trade_id)
    form = TradeForm(request.POST or None, instance=trade)
    submitted = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('trade_log')
    return render(request, 'events/update_trade.html', {'form':form,'trade':trade})
def trade_log(request):
    trades = Trade.objects.all().order_by('-date')
    return render(request, 'events/trade_log.html', {'all_trades':trades, 'index':range(0,len(trades))})

def trade(request,trade_id):
    trade = Trade.objects.get(pk=trade_id)
    return render(request,'events/detailed_trade.html', {'trade':trade})

def delete_trade(request, trade_id):
    trade = Trade.objects.get(pk=trade_id)
    trade.delete()
    return redirect('trade_log')

