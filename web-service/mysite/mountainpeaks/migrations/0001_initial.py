# Generated by Django 3.2 on 2021-04-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('altitude', models.FloatField()),
            ],
        ),
    ]
