# Generated by Django 3.2.8 on 2022-03-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('band', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
    ]