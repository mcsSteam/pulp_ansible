# Generated by Django 2.2.3 on 2019-08-19 14:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_increase_artifact_size_field'),
        ('ansible', '0008_collectionremote_requirements_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionImport',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('namespace', models.CharField(editable=False, max_length=64)),
                ('name', models.CharField(editable=False, max_length=64)),
                ('version', models.CharField(editable=False, max_length=32)),
                ('messages', django.contrib.postgres.fields.jsonb.JSONField(default=list, editable=False)),
                ('task', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
