from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import AuthenticationForm



class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {

            'username':'Nombre de Usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo',
        } 

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Por favor, use una imagen que sea %s x% s píxeles o menos.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Por favor use un JPEG Imagen GIF o PNG')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'El tamaño del archivo no puede superar los 20k.')

        except AttributeError:
            """
            Maneja el caso cuando estamos actualizando el perfil del usuario
            y no proporciones un nuevo avatar
            """
            pass

        return avatar

class Formulariologin(AuthenticationForm):
    print("esty eb el from")
    def __init__(self, *args, **kwargs):
            super(Formulariologin,self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control' 
            self.fields['username'].widget.attrs['placehorder'] = 'Usuario'
            self.fields['password'].widget.attrs['class'] = 'form-control'
            self.fields['password'].widget.attrs['placehorder'] = 'Contraseña'
