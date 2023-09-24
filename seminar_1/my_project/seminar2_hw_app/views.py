from django.shortcuts import render

from .models import Client, Order, Product
from random import randint
from django.views.generic import TemplateView, DetailView


class AllOrderViews(TemplateView):
    template_name = 'seminar2_hw_app/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Client.objects.get(pk=self.kwargs['id_customer'])
        orders = Order.objects.filter(customer=customer).all()
        context['orders'] = orders
        return context


class DetailOrder(DetailView):
    model = Order
    template_name = 'seminar3_app/detail_order.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

