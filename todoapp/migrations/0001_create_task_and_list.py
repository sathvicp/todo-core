# Generated by Django 2.2.16 on 2020-09-19 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('list_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_lists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'task_lists',
                'get_latest_by': ['-priority', 'created_on'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=220)),
                ('description', models.TextField(blank=True, max_length=2500)),
                ('completed', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todoapp.List')),
            ],
            options={
                'db_table': 'task_items',
                'get_latest_by': ['-priority', 'created_on'],
            },
        ),
    ]
