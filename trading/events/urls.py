from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = "home"),
    path('add_trade', views.add_trade, name='add_trade')
]