# Generated by Django 2.2.4 on 2019-08-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatingxml', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.CharField(max_length=100)),
                ('fechaFin', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
    ]
