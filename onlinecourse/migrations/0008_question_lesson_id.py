# Generated by Django 3.1.3 on 2023-04-25 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0007_auto_20230425_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='lesson_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson'),
            preserve_default=False,
        ),
    ]
