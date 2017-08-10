from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Order
from .forms import OrderForm

@login_required
def homepage(request):
    context = {}
    return render(request, 'example/homepage.html', context)


@login_required
def orders_list(request):
    orders = Order.objects.order_by('pk')
    context = {'orders': orders}
    return render(request, 'example/orders_list.html', context)


@login_required
def edit_order(request, pk=None):
    if request.method == "POST":
        if pk:
            order = Order.objects.get(pk=pk)
            form = OrderForm(request.POST, instance=order)
        else:
            form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('orders_list'))
    else:
        order = None
        if pk is None:
            form = OrderForm()
        else:
            order = get_object_or_404(Order, pk=pk)
            form = OrderForm(instance=order)
        context = {'order': order, 'form': form}
        return render(request, 'example/edit_order.html', context)
