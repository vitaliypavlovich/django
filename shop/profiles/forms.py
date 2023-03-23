from django import forms


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )

class RegisterProfileForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=18, required=False)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )