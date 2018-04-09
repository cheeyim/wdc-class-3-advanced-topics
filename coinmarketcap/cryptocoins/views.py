from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cryptocoins.models import Cryptocurrency
from cryptocoins.forms import CryptocurrencyForm


def index(request):
    coins = Cryptocurrency.objects.all().order_by('rank')
    return render(request, 'index.html', {
        'coins': coins
    })


@login_required
def create_new_cryptocurrency(request):
    form = CryptocurrencyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', {
        'form': form
    })
