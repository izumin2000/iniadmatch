# Generated by Django 4.2.7 on 2024-01-04 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iniadmatch', '0005_remove_schedule_end_remove_schedule_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='routine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='iniadmatch.routine'),
        ),
    ]