# Generated by Django 4.1.2 on 2022-10-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_collection_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='volume_24h',
            field=models.IntegerField(blank=True, default=1000),
            preserve_default=False,
        ),
    ]
