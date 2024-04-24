# Generated by Django 4.2.3 on 2024-03-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_usermodel_gender_alter_usermodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='blood_group',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(upload_to='images/user/'),
        ),
    ]