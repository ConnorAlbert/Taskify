# Generated by Django 4.1.6 on 2023-02-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
