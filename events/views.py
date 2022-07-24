from django.shortcuts import render, redirect
from events.models import Trade
from .forms import TradeForm
import decimal
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    return render(request,'events/home.html',{})

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
    p = Paginator(Trade.objects.all().order_by('-date'), 25)
    page = request.GET.get('page')
    trades_p = p.get_page(page)

    return render(request, 'events/trade_log.html', {'all_trades':trades, 'pagin':trades_p})

def trade(request,trade_id):
    trade = Trade.objects.get(pk=trade_id)
    return render(request,'events/detailed_trade.html', {'trade':trade})

def delete_trade(request, trade_id):
    trade = Trade.objects.get(pk=trade_id)
    trade.delete()
    messages.success(request,('Trade Deleted'))
    return redirect('trade_log')

def search_trade(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        strat = request.POST['strategy']
        if strat != 'Strategy':
            print(strat)
            trades = Trade.objects.filter(ticker__contains=searched).filter(trade_type__contains=strat)
        else:
            trades = Trade.objects.filter(ticker__contains=searched)
        pagin = Paginator(trades, 25)
        page = request.GET.get('page')
        trades_p = pagin.get_page(page)
        return render(request,'events/searched_trades.html',{'pagin': trades_p})
