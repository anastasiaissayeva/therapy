# Generated by Django 4.2 on 2025-03-16 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('therapy', '0003_alter_patient_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadiationTherapyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Доп. информация')),
            ],
            options={
                'verbose_name': 'Вид лучевой терапии',
                'verbose_name_plural': 'Виды лучевой терапии',
            },
        ),
        migrations.AlterField(
            model_name='clinicalcase',
            name='radiation_therapy_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapy.radiationtherapytype', verbose_name='Вид лучевой терапии'),
        ),
    ]
