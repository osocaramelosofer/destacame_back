# Generated by Django 3.1.14 on 2022-03-21 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passengers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Buss',
        ),
    ]
