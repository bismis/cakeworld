# Generated by Django 4.0.3 on 2022-05-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgname', models.CharField(max_length=225)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('img', models.CharField(max_length=2500)),
                ('descr', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]