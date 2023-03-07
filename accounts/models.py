from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Interest(models.Model):
    name=models.CharField(max_length=80,unique=True,verbose_name='Nombre')

    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Intereses'
        ordering = ['name']

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image=models.ImageField(default='users/user_profile.jpg', upload_to='users/')
    location=models.CharField(max_length=80,null=True, blank=True)
    bio = models.TextField(max_length=400,null=True, blank=True)
    interest = models.ManyToManyField(Interest, verbose_name='Intereses', null=True, blank=True)

    class Meta:

        verbose_name='Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

def create_user_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)