# Generated by Django 2.2.24 on 2021-08-25 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210826_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_custodian',
            field=models.OneToOneField(default=11111111111, max_length=30, on_delete=django.db.models.deletion.CASCADE, to='app.Custodian', verbose_name='Öğrencinin Velisi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_lessons',
            field=models.ManyToManyField(default=0, to='app.Lessons', verbose_name='Öğrencinin Dersleri'),
        ),
    ]