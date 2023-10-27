from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:category_id>/',views.UpdatePrices.as_view(),name='update-price'),
    path('current-price/',views.CurrentPrice.as_view(),name='get-current-prices')
]
