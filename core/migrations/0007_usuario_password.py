# Generated by Django 3.2.3 on 2021-07-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210707_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
