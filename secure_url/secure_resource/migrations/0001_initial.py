# Generated by Django 3.1.3 on 2020-11-21 12:00

from django.db import migrations, models
import secure_resource.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecureFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_file', models.FileField(upload_to=secure_resource.models.get_file_path)),
                ('password', models.CharField(default=secure_resource.models.generate_password, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SecureUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.URLField(max_length=128)),
                ('password', models.CharField(default=secure_resource.models.generate_password, max_length=128)),
            ],
        ),
    ]
