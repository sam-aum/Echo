from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# from django.contrib import admin
from .models import Ekko


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class SignIn(TemplateView):
    template_name = "sign_in.html"

class EkkoList(TemplateView):
    template_name = "ekko_list.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["ekkos"] = Ekko.objects.all()

        name = self.request.GET.get('name')
    #     print(name)
        if name != None:
            context['ekkos'] = Ekko.objects.filter(source__icontains=name, user=self.request.user)
            context['header'] = f"Results for: {name}"
    #         context['artists'] = Artist.objects.filter(name__icontains=name, user=self.request.user)
    #         
        else:
            context['ekkos'] = Ekko.objects.all()
    #         context['artists'] = Artist.objects.filter(user=self.request.user)
            context['header'] = "Your Ekkos"

        
    #     # query the database - Model.objects.query_method()
        return context 