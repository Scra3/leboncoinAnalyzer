# Generated by Django 2.1 on 2018-10-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5000)),
                ('description', models.TextField(default='No desc')),
                ('price', models.FloatField(default=0.0, max_length=200)),
                ('city_label', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=200)),
            ],
        ),
    ]
