# Generated by Django 3.1.2 on 2020-12-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201228_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
