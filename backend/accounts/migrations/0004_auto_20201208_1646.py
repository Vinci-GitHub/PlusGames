# Generated by Django 3.0.11 on 2020-12-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201208_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=18, unique=True, verbose_name='ユーザ名'),
        ),
    ]
