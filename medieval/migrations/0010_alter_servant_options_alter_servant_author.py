# Generated by Django 4.2.3 on 2023-07-28 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medieval', '0009_alter_person_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servant',
            options={'verbose_name_plural': 'Добавить Холопа'},
        ),
        migrations.AlterField(
            model_name='servant',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medieval.person', verbose_name='относится к'),
        ),
    ]
