# Generated by Django 2.0 on 2017-12-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image_path',
            field=models.CharField(blank=True, default='https://imger.s3-us-west-2.amazonaws.com/static/ang/assets/images/nature/4.jpg', max_length=120, null=True),
        ),
    ]
