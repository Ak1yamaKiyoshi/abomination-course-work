# Generated by Django 4.2.13 on 2024-05-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_work_app", "0005_alter_profilepicture_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilepicture",
            name="profile_picture",
            field=models.TextField(),
        ),
    ]
