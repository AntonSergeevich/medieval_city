# Generated by Django 4.2.3 on 2023-07-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medieval', '0010_alter_servant_options_alter_servant_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='servant',
            name='name_person',
            field=models.CharField(default='Алеша Попович'),
        ),
    ]
