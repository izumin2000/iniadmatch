# Generated by Django 4.2.7 on 2024-01-02 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iniadmatch', '0003_alter_account_user_alter_booking_schedule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='iniadmatch.teacher'),
        ),
    ]
