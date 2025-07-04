# Generated by Django 4.1.7 on 2023-02-25 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0005_course_department_alter_place_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_contact', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_gender', models.CharField(max_length=100)),
                ('user_address', models.TextField(null=True)),
                ('user_photo', models.FileField(upload_to='userdocs/')),
                ('user_proof', models.FileField(upload_to='userdocs/')),
                ('user_password', models.CharField(max_length=100, unique=True)),
                ('user_doj', models.DateField(auto_now=True)),
                ('user_graduation', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
                ('user_course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.course')),
            ],
        ),
    ]
