# Generated by Django 3.0.11 on 2020-12-23 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20201223_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_date'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
