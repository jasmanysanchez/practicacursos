from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email', 'password', 'password2')
        widgets = {
            "password": forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for k, v in self.fields.items():
            self.fields[k].required = True
            self.fields[k].widget.attrs["class"] = "form-control"
    
    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return password2
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("Email ya está registrado")
        return email