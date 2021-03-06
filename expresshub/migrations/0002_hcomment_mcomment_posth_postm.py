# Generated by Django 3.0.6 on 2020-06-03 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expresshub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlem', models.CharField(max_length=255)),
                ('bodym', models.TextField()),
                ('createdatem', models.DateTimeField(auto_now_add=True)),
                ('updatedatem', models.DateTimeField(auto_now=True)),
                ('statusm', models.IntegerField(choices=[(0, 'Pending'), (1, 'In Process'), (2, 'Completed')])),
                ('authorm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleh', models.CharField(max_length=255)),
                ('bodyh', models.TextField()),
                ('createdateh', models.DateTimeField(auto_now_add=True)),
                ('updatedateh', models.DateTimeField(auto_now=True)),
                ('statush', models.IntegerField(choices=[(0, 'Pending'), (1, 'In Process'), (2, 'Completed')])),
                ('authorh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbody', models.TextField()),
                ('mcreatedate', models.DateTimeField(auto_now_add=True)),
                ('mstatus', models.IntegerField(choices=[(0, 'Draft'), (1, 'Posted')], default=1)),
                ('mauthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcomments', to='expresshub.Post')),
            ],
            options={
                'ordering': ['-mcreatedate'],
            },
        ),
        migrations.CreateModel(
            name='HComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hbody', models.TextField()),
                ('hcreatedate', models.DateTimeField(auto_now_add=True)),
                ('hstatus', models.IntegerField(choices=[(0, 'Draft'), (1, 'Posted')], default=1)),
                ('hauthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hcomments', to='expresshub.Post')),
            ],
            options={
                'ordering': ['-hcreatedate'],
            },
        ),
    ]
