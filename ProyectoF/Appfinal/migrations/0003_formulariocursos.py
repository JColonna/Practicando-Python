# Generated by Django 4.0 on 2021-12-24 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfinal', '0002_auto_20211216_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioCursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=40)),
                ('comision', models.IntegerField()),
            ],
        ),
    ]
