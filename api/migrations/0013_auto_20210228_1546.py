# Generated by Django 3.0.5 on 2021-02-28 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201127_1719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('-pub_date',)},
        ),
    ]
