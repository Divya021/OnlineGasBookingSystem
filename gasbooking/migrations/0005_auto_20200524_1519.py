# Generated by Django 2.2.2 on 2020-05-24 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gasbooking', '0004_bookcylinder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcylinder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gasbooking.Newconnection'),
        ),
    ]