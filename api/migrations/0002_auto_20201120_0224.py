# Generated by Django 3.1.3 on 2020-11-20 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filteritem',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Filter Name:'),
        ),
    ]
