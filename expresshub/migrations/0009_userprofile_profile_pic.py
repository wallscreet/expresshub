# Generated by Django 3.0.6 on 2020-07-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expresshub', '0008_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/Images'),
        ),
    ]
