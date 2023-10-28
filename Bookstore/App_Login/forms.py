from django.forms import ModelForm
from App_Login.models import User, Profile
from django.contrib.auth.forms import UserCreationForm


class profileform(ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)  # Note the comma to create a tuple


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
