# Generated by Django 3.0.6 on 2020-07-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expresshub', '0006_auto_20200702_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostfound',
            name='status',
            field=models.IntegerField(choices=[(0, 'Lost'), (1, 'Found'), (2, 'Claimed')], default=0),
        ),
    ]
