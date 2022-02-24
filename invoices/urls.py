from django.urls import path

from invoices.models import Invoice
from .views import (
    InvoiceListView,
    InvoiceFormView,
    InvoiceUpdateView,
    AddPositionsFormView,
    CloseInvoiceView
)

app_name = 'invoices'

urlpatterns = [
    path('', InvoiceListView.as_view(), name='main'),
    path('new/', InvoiceFormView.as_view(), name='create'),
    # path('<pk>', SimpleTemplateView.as_view(), name='simple-template'),
    path('<pk>', AddPositionsFormView.as_view(), name='detail'),
    path('<pk>/close/', CloseInvoiceView.as_view(), name='close'),
    path('<pk>/update/', InvoiceUpdateView.as_view(), name='update')
]
