from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView

# Create your views here.
def home(request):
    return render(request, 'coffeeApp/index.html')

def catalog(request):
    return render(request, 'coffeeApp/catalog.html')

def gallery(request):
    return render(request, 'coffeeApp/gallery.html')

class CustomLoginView(LoginView):
    template_name = 'coffeeApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'coffeeApp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)