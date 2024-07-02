# Generated by Django 5.0.6 on 2024-07-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('dob', models.DateTimeField(verbose_name='date of birth')),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]