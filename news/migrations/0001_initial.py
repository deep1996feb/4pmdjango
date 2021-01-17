# Generated by Django 3.1.3 on 2020-12-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoty', models.CharField(max_length=50)),
                ('head_line', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='')),
                ('detail_news', models.TextField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
