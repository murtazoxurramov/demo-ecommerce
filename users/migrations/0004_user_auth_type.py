# Generated by Django 4.1.7 on 2023-02-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_type',
            field=models.CharField(choices=[('via_phone', 'via_phone'), ('via_email', 'via_email'), ('via_username', 'via_username')], default='via_username', max_length=31),
        ),
    ]
