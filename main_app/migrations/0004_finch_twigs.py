# Generated by Django 4.1.4 on 2022-12-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_twig_alter_food_options_alter_food_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='twigs',
            field=models.ManyToManyField(to='main_app.twig'),
        ),
    ]
