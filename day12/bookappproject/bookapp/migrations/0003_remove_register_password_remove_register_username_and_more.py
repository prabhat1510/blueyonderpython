# Generated by Django 5.0.6 on 2024-07-02 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_login_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
        migrations.AddField(
            model_name='register',
            name='login',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bookapp.login'),
            preserve_default=False,
        ),
    ]
