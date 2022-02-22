from django.urls import path
from .views import (
    InvoiceListView,
    InvoiceFormView,
    SimpleTemplateView)

app_name = 'invoices'

urlpatterns = [
    path('', InvoiceListView.as_view(), name='main'),
    path('new/', InvoiceFormView.as_view(), name='create'),
    path('<pk>', SimpleTemplateView.as_view(), name='simple-template')
]
