# Generated by Django 3.0 on 2022-10-08 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproduct',
            name='imageurl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='allproduct',
            name='detail',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]