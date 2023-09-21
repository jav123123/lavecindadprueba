from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model  # Importa get_user_model


from django.contrib.auth import get_user_model
from django.db import models

class AlgunaClase(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class RegistroForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    direccion = forms.CharField(max_length=255, required=False)
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')], required=False)
    first_name = forms.CharField(
        label="Nombre",  # Cambia la etiqueta aquí
        max_length=30,
        required=True,
    )
    last_name = forms.CharField(
        label="Apellido",  # Cambia la etiqueta aquí
        max_length=30,
        required=True,
    )

    

    class Meta:
        model = get_user_model()  # Utiliza get_user_model()
        fields = ('username' , 'first_name','last_name','fecha_nacimiento', 'direccion', 'sexo','password1', 'password2',)
        help_texts = {k:"" for k in fields }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Oculta los campos de ayuda
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['first_name'].help_text = ""
