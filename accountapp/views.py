from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User #django에서 기본적으로 제공하는 User 모델
    form_class = UserCreationForm #django에서 기본 제공
    success_url = reverse_lazy('accountapp:hello_world') #reverse는 함수형에서 reverse_lazy는 class형에서 사용
    template_name = 'accountapp/create.html'