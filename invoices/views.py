from email import message
from django.urls import (
    reverse_lazy,
    reverse)
from profiles.models import Profile
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    FormView,
    TemplateView,
    DetailView,
    UpdateView,
    RedirectView,
    DeleteView
)
from .models import Invoice
from positions.models import Position
from .forms import InvoiceForm
from positions.forms import PositionForm
from django.contrib import messages
from .mixins import InvoiceNotClosedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = "invoices/main.html"  # default invoice_list.html
    paginate_by = 3
    context_object_name = "qs"

    def get_queryset(self):
        # profile = Profile.objects.get(user=self.request.user)
        profile = get_object_or_404(Profile, user=self.request.user)
        # qs = Invoice.objects.filter(profile=profile).order_by('-created')

        # return qs

        return super().get_queryset().filter(profile=profile).order_by('-created')


class InvoiceFormView(LoginRequiredMixin, FormView):
    form_class = InvoiceForm
    template_name = 'invoices/create.html'
    # success_url = reverse_lazy('invoices:main')
    i_instance = None

    def get_success_url(self):
        return reverse('invoices:detail', kwargs={'pk': self.i_instance.pk})

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)


class SimpleTemplateView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'invoices/simple_template.html'


# class SimpleTemplateView(TemplateView):
#     template_name = 'invoices/simple_template.html'

class AddPositionsFormView(LoginRequiredMixin, FormView):
    form_class = PositionForm
    template_name = "invoices/detail.html"

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        invoice_pk = self.kwargs.get('pk')
        invoice_object = Invoice.objects.get(pk=invoice_pk)
        instance = form.save(commit=False)
        instance.invoice = invoice_object
        form.save()
        messages.info(
            self.request, f'Successfully added position - {instance.title}')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice_object = Invoice.objects.get(pk=self.kwargs.get('pk'))
        qs = invoice_object.positions
        context['object'] = invoice_object
        context['qs'] = qs
        return context


class InvoiceUpdateView(LoginRequiredMixin, InvoiceNotClosedMixin, UpdateView):
    model = Invoice
    template_name = 'invoices/update.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('invoices:main')

    def form_valid(self, form):
        instance = form.save()
        messages.info(
            self.request, f'Successfuly updated invoice - {instance.number}')
        return super().form_valid(form)


class CloseInvoiceView(LoginRequiredMixin, RedirectView):

    pattern_name = "invoices:detail"

    print('hello')

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Invoice.objects.get(pk=pk)
        obj.closed = True
        obj.save()
        print(obj)
        return super().get_redirect_url(*args, **kwargs)


class InvoicePositionDeleteView(LoginRequiredMixin, InvoiceNotClosedMixin, DeleteView):
    model = Position
    template_name = 'invoices/position_confirm_delete.html'

    # /<pk>/delete/<position_pk>/
    def get_object(self):
        pk = self.kwargs.get('position_pk')
        object = Position.objects.get(pk=pk)
        return object

    def get_success_url(self):
        messages.info(self.request, f'Delete Position - {self.object.title}')
        return reverse('invoices:detail', kwargs={'pk': self.object.invoice.id})
