# Generated by Django 4.1.5 on 2023-09-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITC_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sertifikat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_sertifikat', models.FileField(upload_to='sertifikat/')),
            ],
        ),
    ]