from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm
# Create your views here.

#FBV
def home_view(request):
    context = {}
    if request.user.is_authenticated:
        #ดึงโปรไฟล์
        context['profile'] = Profile.objects.filter(user=request.user).first()
    return render(request, 'accounts/home.html', context)

#CBV 
class Registerview(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("register")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response
    
    
class Loginview(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    
class LogoutView(LogoutView):
    next_page = 'home'
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy("home")
    
    def get_object(self):
        return self.request.user.profile