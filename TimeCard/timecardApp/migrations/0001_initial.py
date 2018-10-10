# Generated by Django 2.0.6 on 2018-10-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('dateOfWork', models.DateField()),
                ('dateOfEntry', models.DateField()),
            ],
        ),
    ]
