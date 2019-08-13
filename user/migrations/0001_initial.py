# Generated by Django 2.2.4 on 2019-08-13 08:43

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
