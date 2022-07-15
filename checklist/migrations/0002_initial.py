# Generated by Django 4.0.2 on 2022-07-15 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='med_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.medcard'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
        ),
        migrations.AddField(
            model_name='answer',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.question'),
        ),
    ]
