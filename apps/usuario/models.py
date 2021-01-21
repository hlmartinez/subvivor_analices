# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# #from django.contrib.auth.models import AbstractUser
# # Create your models here.
# # class CustomUser(AbstractUser):
# #     pass


# class Perfil(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, blank=True)
#     email = models.EmailField(max_length=150)
#     avatar = models.ImageField(blank=True,null=True)

#     #objects = models.Manager()
#     def __str__(self):
#         return self.User.username
#     '''
#     Con el uso del patron de disenno estructural decorador @receiver, podemos vincular una señal con una función.
#     Por lo tanto, cada vez que una instancia de modelo de Usuario termina de ejecutar su método save ()
#     (o cuando finaliza el registro de usuario), update_profile_signal comenzará a funcionar justo después 
#     de que el usuario haya guardado.
#     '''
# # @receiver(post_save, sender=User)
# # def update_profile_signal(sender, instance, created, **kwargs):
# #     if created:
# #         Perfil.objects.create(user=instance)
# #     instance.profile.save()