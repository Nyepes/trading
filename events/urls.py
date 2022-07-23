from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = "home"),
    path('add_trade', views.add_trade, name='add_trade'),
    path('trade_log',views.trade_log,name='trade_log'),
    path('trade<trade_id>',views.trade, name='trade'),
    path('update_trade<trade_id>', views.edit_trade, name='update_trade'),
    path('delete_trade<trade_id>', views.delete_trade, name='delete_trade'),
]