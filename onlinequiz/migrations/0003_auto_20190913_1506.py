# Generated by Django 2.2.4 on 2019-09-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinequiz', '0002_auto_20190912_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='correct_answer',
            field=models.CharField(max_length=100),
        ),
    ]
