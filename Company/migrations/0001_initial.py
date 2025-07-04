# Generated by Django 4.1.7 on 2023-03-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_internships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_title', models.CharField(max_length=50)),
                ('int_post', models.CharField(max_length=50)),
                ('int_date', models.DateField(auto_now=True)),
                ('int_duration', models.CharField(max_length=50)),
                ('int_details', models.TextField(null=True)),
                ('int_stipend', models.IntegerField(default=0)),
            ],
        ),
    ]
