# Generated by Django 3.2.5 on 2021-07-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='diary_images/'),
        ),
    ]
