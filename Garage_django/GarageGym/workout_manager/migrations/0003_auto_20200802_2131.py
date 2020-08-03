# Generated by Django 3.0.8 on 2020-08-02 18:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workout_manager', '0002_auto_20200801_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('max_people', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='lesson',
            field=models.ManyToManyField(to='workout_manager.Lesson'),
        ),
    ]
