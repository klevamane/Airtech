# Generated by Django 2.2.4 on 2019-08-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.ImageField(default='https://res.cloudinary.com/health-id/image/upload/v1554552278/Profile_Picture_Placeholder.png', upload_to=''),
        ),
    ]
