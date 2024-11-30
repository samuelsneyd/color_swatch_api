from django.urls import path
from .views import HealthCheck, ColorSwatchView, ColorSwatchBySpaceView

urlpatterns = [
    path('health/', HealthCheck.as_view(), name='health'),
    path('colors/', ColorSwatchView.as_view(), name='color-swatch'),
    path('colors/<str:color_space>', ColorSwatchBySpaceView.as_view(), name='color-swatch-by-space')
]
