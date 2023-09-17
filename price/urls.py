from django.urls import path
from . import views

urlpatterns = [
    path('update/',views.UpdatePrices.as_view(),name='update_price')
]
