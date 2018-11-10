# Generated by Django 2.1.3 on 2018-11-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('in_gramms', models.FloatField(default=1.0)),
            ],
        ),
    ]