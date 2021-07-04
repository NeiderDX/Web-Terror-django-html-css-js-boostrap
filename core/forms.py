from django.forms import models, widgets
from core.models import Movie, User
from django import forms

class UsersCreationForm(forms.ModelForm):
    
    run=forms.CharField(widget=forms.TextInput(attrs={'class':'form-text'}), max_length=9, label_suffix="Ingrese RUT aqui")
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label_suffix="Ingrese sus nombres")
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label_suffix="Ingrese sus apellidos aqui")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label_suffix="Ingrese su email aqui")
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label_suffix="Ingrese su direccion aqui")
    phone1=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','type':'tel'}), max_length=9,label_suffix="Ingrese su telefono aqui, maximo 9 digitos")
    phone2=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','type':'tel'}), max_length=9, label_suffix="Ingrese otra vez su numero de telefono aqui")
    birth_day=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date','max':'2010-12-31'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label_suffix="Ingrese su contraseña")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label_suffix="Repita su contraseña")
    movie_preference=forms.ChoiceField(choices=(("Terror clasico","Terror Clasico"),("Terror suspenso","Terror Suspenso"),("Terror psicologico", "Terror Psicologico"),("Terror accion", "Terror Accion"),("Terror horror","Terror Horror")), widget=forms.Select(attrs={'class':'valid'}))
    sex=forms.ChoiceField(choices=(("M","Masculino"),("F","Femenino")),widget=forms.RadioSelect())
    class Meta:
        model = User
        fields = ("run","first_name","last_name","email","address","birth_day","movie_preference","sex",)

    def save(self, commit=True):
        user=super(UsersCreationForm,self).save(commit=False)
        phone=self.cleaned_data.get('phone1')
        password=self.cleaned_data.get('password1')
        if commit:
            user.set_password(password)
            user.set_phone(phone)
            user.save()
        return user

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields=(
            "title",
            "release_date",
            "runtime",
            "plot",
            "imdb_rating",
            "user"
            )
        labels={
            'title':'Titulo',
            'release_date':'Fecha de estreno',
            'runtime':'Duracion',
            'plot':'Sinopsis',
            'imdb_rating':'Rating de imdb'
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'release_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'runtime':forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'plot':forms.Textarea(attrs={'class':'form-control','style':'height:80px'}),
            'imdb_rating':forms.NumberInput(attrs={'class':'form-control'}),
            'user':forms.HiddenInput
        }

class ProfileEditForm(forms.ModelForm):

    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label_suffix="Ingrese su nuevo email aqui")
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label_suffix="Ingrese su direccion aqui")
    phone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','type':'tel'}), max_length=9,label_suffix="Ingrese su nuevo telefono aqui, maximo 9 digitos")
    birth_day=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date','max':'2010-12-31'}))
    
    class Meta:
        model = User
        fields = ("email","address","phone","birth_day",)
    
    def save(self, commit=True):
        user=super(ProfileEditForm,self).save(commit=False)
        if commit:
            user.save()
        return user