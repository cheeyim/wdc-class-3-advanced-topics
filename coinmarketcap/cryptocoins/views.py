from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from braces.views import FormValidMessageMixin

from cryptocoins.models import Cryptocurrency
from cryptocoins.forms import CryptocurrencyForm


# def index(request):
#     coins = Cryptocurrency.objects.all().order_by('rank')
#     return render(request, 'index.html', {
#         'coins': coins
#     })
class IndexPageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coins = Cryptocurrency.objects.all().order_by('rank')
        context['coins'] = coins
        favorite_coins = []
        if self.request.user.is_authenticated:
            favorite_coins = self.request.user.profile.favorite_coins.all()
        context['favorite_coins'] = favorite_coins
        return context
#
# @login_required
# def create_new_cryptocurrency(request):
#     form = CryptocurrencyForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     return render(request, 'create.html', {
#         'form': form
#     })


class CreateCryptoView(LoginRequiredMixin, FormValidMessageMixin, CreateView):
    template_name = 'create.html'
    form_class = CryptocurrencyForm
    success_url = '/'

    def get_form_valid_message(self):
        return "Crypto {} created!".format(self.object.name)


@login_required
def favorite(request):
    profile = request.user.profile
    coin_id = request.POST['coinId']
    coin = Cryptocurrency.objects.get(id=coin_id)

    if profile.favorite_coins.filter(id=coin_id).exists():
        profile.favorite_coins.remove(coin)
    else:
        profile.favorite_coins.add(coin)

    return HttpResponse("Good!")
