# Generated by Django 4.1.1 on 2022-10-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_employees_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='age',
            field=models.IntegerField(default=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='level',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
