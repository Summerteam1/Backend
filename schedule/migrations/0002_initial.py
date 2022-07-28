# Generated by Django 3.2 on 2022-07-28 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='work_days',
            field=models.ManyToManyField(to='schedule.WorkDays'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time_slots',
            field=models.ManyToManyField(to='schedule.TimeSlots'),
        ),
    ]
