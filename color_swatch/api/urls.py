from django.urls import path
from .views import HealthCheck, ColorSwatchView

urlpatterns = [
    path('health/', HealthCheck.as_view(), name='health'),
    path('colors/', ColorSwatchView.as_view(), name='color-swatch'),
]
