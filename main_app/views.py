from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
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
        # context["ekkos"] = Ekko.objects.all()
        name = self.request.GET.get('name')
  
        if name != None:
            context['ekkos'] = Ekko.objects.filter(source__icontains=name, user=self.request.user)
            context['header'] = f"Results for: {name}"
    
      
        else:
            # context['ekkos'] = Ekko.objects.all()
            context['ekkos'] = Ekko.objects.filter(user=self.request.user)
            context['header'] = "Your Ekkos"

        
    #     # query the database - Model.objects.query_method()
        return context 

class EkkoCreate(CreateView):
    model = Ekko
    fields = ['user', 'ekko', 'source', 'verified_ekko']
    template_name = "ekko_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EkkoCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('ekko_list')

# class EkkoDetail(DetailView):
#     model = Ekko
#     template_name = "ekko_detail.html"
    # this is can used for comments

class EkkoUpdate(UpdateView):
    model = Ekko
    fields = ['user', 'ekko', 'source', 'verified_ekko']
    template_name = "ekko_update.html"
    success_url = "/ekkos/"
    # def get_success_url(self):
    #     return reverse('artist_detail', kwargs={'pk': self.object.pk})

class EkkoDelete(DeleteView):
    model = Ekko
    template_name = "ekko_delete.html"
    success_url = "/ekkos/"
    # def get_success_url(self):
    #     return reverse('ekko_delete', kwargs={'pk': self.object.pk})