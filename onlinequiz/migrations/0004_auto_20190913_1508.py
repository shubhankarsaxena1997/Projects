# Generated by Django 2.2.4 on 2019-09-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinequiz', '0003_auto_20190913_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='choice1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='choice2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='choice3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='choice4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questions',
            field=models.CharField(max_length=200),
        ),
    ]
