# Generated by Django 3.2.23 on 2024-01-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_nemone'),
    ]

    operations = [
        migrations.CreateModel(
            name='karmand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('jab', models.CharField(max_length=30)),
                ('dec', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='resume/media')),
            ],
        ),
    ]
