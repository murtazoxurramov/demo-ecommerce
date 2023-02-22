# Generated by Django 4.1.7 on 2023-02-20 05:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Telefon raqamingiz 9 bilan boshlanishi va 12 belgidan oshmasligi kerak! Masalan: 998900459442', regex='^9\\d{12}$')]),
        ),
    ]