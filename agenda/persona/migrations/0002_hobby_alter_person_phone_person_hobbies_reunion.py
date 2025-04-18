# Generated by Django 5.1.7 on 2025-03-30 23:26

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('hobby', models.CharField(max_length=50, verbose_name='Pasa tiempo')),
            ],
            options={
                'verbose_name': 'Hobby',
                'verbose_name_plural': 'Hobbies',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Telefono'),
        ),
        migrations.AddField(
            model_name='person',
            name='hobbies',
            field=models.ManyToManyField(to='persona.hobby'),
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('asunto', models.CharField(max_length=100, verbose_name='Aunto de Reunion')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.person')),
            ],
            options={
                'verbose_name': 'Reunion',
                'verbose_name_plural': 'Reuniones',
            },
        ),
    ]
