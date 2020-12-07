from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from orders.models import Order
import uuid


@login_required
def confirmation(request):
    exist_oder_for_the_user = Order.objects.filter(user__username=request.user.username).exists()

    if not exist_oder_for_the_user:
        return redirect('order')

    data = Order.objects.get(user__username=request.user.username)
    return render(request, 'order/confirmation.html', {'order': data})


@login_required
def order(request):
    exist_oder_for_the_user = Order.objects.filter(user__username=request.user.username).exists()

    if exist_oder_for_the_user:
        return redirect('confirmation')

    if request.method == 'POST':
        code = str(uuid.uuid4())
        description = request.POST['description']
        Order.objects.create(user=request.user, code=code, description=description)
        return redirect('confirmation')

    return render(request, 'order/form.html')
