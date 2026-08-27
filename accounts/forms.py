from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","email", "password1", "password2")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #เรียก init เดิม ของ super class
        for field in self.fields.values(): #ใข้ css
            field.widget.attrs.update({"class" : "form-control"})
            
            
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #เรียก init เดิม ของ super class
        for field in self.fields.values(): #ใข้ css
            field.widget.attrs.update({"class" : "form-control"})
                
                