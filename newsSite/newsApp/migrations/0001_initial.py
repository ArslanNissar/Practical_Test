# Generated by Django 2.2.3 on 2020-04-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headline_text', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
    ]
