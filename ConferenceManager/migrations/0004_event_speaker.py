# Generated by Django 4.0.6 on 2022-07-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConferenceManager', '0003_event_nameroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='speaker',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
