from django.shortcuts import render, redirect
from events.models import Trade
from .forms import TradeForm
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    print(request.user.profile.win_p[0])
    return render(request,'events/home.html',{})

def add_trade(request):
    submitted = False
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.page_user = request.user.profile
            trade.equity_at_time = request.user.profile.total_equity
            trade.save()
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
    p = Paginator(Trade.objects.filter(page_user__exact=request.user.profile).order_by('-date'), 25)
    page = request.GET.get('page')
    trades_p = p.get_page(page)

    return render(request, 'events/trade_log.html', {'pagin':trades_p})

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
        trades = Trade.objects.filter(page_user=request.user.profile)
        if strat != 'Strategy':
            print(strat)
            trades = trades.filter(ticker__contains=searched).filter(trade_type__contains=strat)
        else:
            trades = trades.filter(ticker__contains=searched)
        pagin = Paginator(trades, 25)
        page = request.GET.get('page')
        trades_p = pagin.get_page(page)
        return render(request,'events/searched_trades.html',{'pagin': trades_p})
