# Generated by Django 2.2.5 on 2019-09-23 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190920_2227'),
        ('course', '0002_auto_20190923_1813'),
        ('user_course', '0003_remove_uservideo_asc'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='uservideo',
            unique_together={('video', 'user')},
        ),
    ]
