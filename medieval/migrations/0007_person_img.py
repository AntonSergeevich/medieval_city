# Generated by Django 4.2.3 on 2023-07-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medieval', '0006_alter_person_categorytype'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
