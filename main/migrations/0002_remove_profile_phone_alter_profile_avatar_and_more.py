# Generated by Django 5.1.7 on 2025-04-09 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatars/default.png', upload_to='avatars/', verbose_name='Аватар'),
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
