# Generated by Django 3.0.6 on 2020-06-04 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expresshub', '0004_lfcomment_lostfound'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lfcomment',
            name='lostfound',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lfcomments', to='expresshub.LostFound'),
        ),
    ]