# Generated by Django 3.0.4 on 2020-07-21 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
