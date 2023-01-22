from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /salons/1/
    path('<int:salon_id>/', views.detail, name='detail')
]
