from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from apps.usuario.forms import RegistroForm, Formulariologin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

 
  
class ReistrarUsuario(CreateView):
    model = User
    template_name = "registration/registrar_Users.html"
    form_class = RegistroForm
    success_url = reverse_lazy('analisis:home')

# class Loginview(FormView):
#     template_name = "login .html"
#     form_class = Formulariologin
#     success_url = reverse_lazy('usuario:home')
#     print("estoy en el loginnnnn.........................................")

#     @method_decorator(csrf_protect,name='dispatch')
#     @method_decorator(never_cache,name='dispatch')
#     def dispatch(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.get_success_url())     
#         else:
#             return super(Loginview,self).dispatch(request, *args, **kwargs)
    
#     def form_valid(self,form):
#         login(self.request, form.get_user())
#         return super(Loginview,self).form_valid(form)




def resetpass(request):
    return render(request,'resetpass.html')

#     #Estamos utilizando el método refresh_from_db () para manejar el problema del sincronismo,
#     #básicamente recargando la base de datos después de la señal, 
#     #por lo que mediante este método se cargará nuestra instancia de perfil.


# def registerview(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.first_name = form.cleaned_data.get('first_name')
#             user.profile.last_name = form.cleaned_data.get('last_name')
#             user.profile.email = form.cleaned_data.get('email')
#             user.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             print("entro al registrar usuario")
#             return redirect('home.html')
#     else:
#         form = SignUpForm()   
#     return render(request,'registrar_Users.html',{'form':form})


