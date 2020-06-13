# Generated by Django 2.1.1 on 2019-11-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('describe', models.TextField(default='', verbose_name='描述')),
                ('status', models.BooleanField(default=1, verbose_name='状态')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
