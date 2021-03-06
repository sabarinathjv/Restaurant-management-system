# Generated by Django 4.0.1 on 2022-01-26 18:02

import api.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='start_date',
        ),
        migrations.AddField(
            model_name='newuser',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newuser',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to=api.models.upload_to, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='user_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usr_type', to='api.usertype'),
        ),
        migrations.DeleteModel(
            name='Userdetail',
        ),
    ]
