from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

    genders = (("1","Male"),
               ("2","Female"), 
                )

    email = forms.EmailField(required=True)

    gender = forms.TypedChoiceField(choices = genders, 
                                    required=False,
                                    widget = forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username','email','gender','password1','password2']