# Generated by Django 3.1.4 on 2021-01-09 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserRegistration', '0004_auto_20210108_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fullName',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Reader', 'Reader'), ('Author', 'Author')], default=1, max_length=15),
            preserve_default=False,
        ),
    ]