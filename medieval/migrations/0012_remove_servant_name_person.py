# Generated by Django 4.2.3 on 2023-07-28 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medieval', '0011_servant_name_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servant',
            name='name_person',
        ),
    ]
