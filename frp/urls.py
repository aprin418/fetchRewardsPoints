from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payers/', views.payers, name='payers'),
    path('payer/create/', views.PayerCreate.as_view(), name='payer_create'),
    path('payer/<int:pk>/update/', views.PayerUpdate.as_view(), name='Payer_update'),
]
