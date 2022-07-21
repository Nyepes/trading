from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = "home"),
    path('add_trade', views.add_trade, name='add_trade'),
    path('trade_log',views.trade_log,name='trade_log'),
    path('trade<trade_id>',views.trade, name='trade')
]