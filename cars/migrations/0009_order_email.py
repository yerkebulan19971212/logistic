# Generated by Django 3.1.7 on 2021-03-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_merge_20210317_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
