from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator   
from django.db.models import Q

# from django.contrib import admin
from .models import Ekko, Comment


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):   
            context = super().get_context_data(**kwargs)
            context["ekkos"] = Ekko.objects.all()
            name = self.request.GET.get('name')

            if name != None:
                context["ekkos"] = Ekko.objects.filter(Q(source__icontains=name) | Q(ekko__icontains=name))
            else:
                context["ekkos"] = Ekko.objects.all()
                context['header'] = "Home"
            return context

class About(TemplateView):
    template_name = "about.html"

class SignIn(TemplateView):
    template_name = "sign_in.html"

@method_decorator(login_required, name='dispatch')
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

class EkkoDetail(DetailView):
    model = Ekko
    template_name = "ekko_detail.html"
  

class EkkoUpdate(UpdateView):
    model = Ekko
    fields = ['user', 'ekko', 'source', 'verified_ekko']
    template_name = "ekko_update.html"
    # success_url = "/ekkos/"
    def get_success_url(self):
        return reverse('ekko_detail', kwargs={'pk': self.object.pk})

class EkkoDelete(DeleteView):
    model = Ekko
    template_name = "ekko_delete.html"
    success_url = "/ekkos/"
    # def get_success_url(self):
    #     return reverse('ekko_delete', kwargs={'pk': self.object.pk})

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("ekko_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class CommentCreate(View):

    def post(self, request, pk):
        user = self.request.user
        comment = request.POST.get("comment")
        ekko = Ekko.objects.get(pk=pk)
        Comment.objects.create(user=user, comment=comment, ekko=ekko)
        return redirect('ekko_detail', pk=pk)

