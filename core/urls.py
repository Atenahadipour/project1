from django.contrib import admin
from django.urls import path
from predictor.views import predict_price, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/predict/', predict_price, name='predict_price_api'),
]