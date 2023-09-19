# Generated by Django 4.2.5 on 2023-09-13 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'script',
            },
        ),
        migrations.CreateModel(
            name='ExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.TextField()),
                ('execution_started_at', models.DateTimeField()),
                ('execution_completed_at', models.DateTimeField()),
                ('execution_time', models.FloatField()),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tkinter_web.script')),
            ],
            options={
                'db_table': 'execution_log',
            },
        ),
    ]