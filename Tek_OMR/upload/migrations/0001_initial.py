# Generated by Django 2.2.5 on 2019-09-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('svg_file', models.FileField(upload_to='svg/')),
                ('img_file', models.FileField(upload_to='img/')),
            ],
        ),
    ]
