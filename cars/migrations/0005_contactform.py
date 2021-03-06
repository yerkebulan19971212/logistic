# Generated by Django 3.1.6 on 2021-03-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210316_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
