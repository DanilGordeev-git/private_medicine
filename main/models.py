from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default.png',
        verbose_name='Аватар'
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
class ServiceCategory(models.Model):
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField('Название услуги', max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField('Краткое описание')
    full_description = models.TextField('Полное описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    duration = models.CharField('Длительность', max_length=50)
    image = models.ImageField('Изображение', upload_to='services/')
    available = models.BooleanField('Доступно', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    advantages = models.TextField('Преимущества', help_text='Перечислите преимущества через точку с запятой')

    class Meta:
        ordering = ['order']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

    def get_advantages_list(self):
        """Разбивает преимущества на список"""
        return [adv.strip() for adv in self.advantages.split(';') if adv.strip()]