# Generated by Django 3.1.3 on 2020-11-20 02:08

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilterItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Filter ID:')),
                ('name', models.CharField(max_length=100, verbose_name='Project Name:')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Added:')),
            ],
        ),
        migrations.CreateModel(
            name='InboxItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Item Name:')),
                ('description', models.TextField(max_length=300, verbose_name='Item Description:')),
                ('convert_to_task', models.BooleanField(default=False, verbose_name='Convert To Task?:')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Added:')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified:')),
            ],
        ),
        migrations.CreateModel(
            name='SubTaskItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Task ID:')),
                ('name', models.CharField(max_length=100, verbose_name='Task Name:')),
                ('description', models.TextField(max_length=300, verbose_name='Task Description:')),
                ('task_status', models.CharField(choices=[('Not Started', 'Not Started'), ('Upcoming', 'Upcoming'), ('In Progress', 'In Progress'), ('Due Soon', 'Due Soon'), ('Overdue', 'Overdue')], default='In Progress', max_length=11, verbose_name='Task Status:')),
                ('start_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date:')),
                ('due_date_time', models.DateTimeField(verbose_name='Due Date:')),
                ('duration', models.DurationField(verbose_name='Duration:')),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=6, verbose_name='Task Priority:')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Is Completed?')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Added:')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified:')),
            ],
        ),
        migrations.CreateModel(
            name='TagItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Tag Name:')),
            ],
        ),
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Task ID:')),
                ('name', models.CharField(max_length=100, verbose_name='Task Name:')),
                ('description', models.TextField(max_length=300, verbose_name='Task Description:')),
                ('task_status', models.CharField(choices=[('Not Started', 'Not Started'), ('Upcoming', 'Upcoming'), ('In Progress', 'In Progress'), ('Due Soon', 'Due Soon'), ('Overdue', 'Overdue')], default='In Progress', max_length=11, verbose_name='Task Status:')),
                ('start_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date:')),
                ('due_date_time', models.DateTimeField(verbose_name='Due Date:')),
                ('duration', models.DurationField(verbose_name='Duration:')),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=6, verbose_name='Task Priority:')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Is Completed?')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Added:')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified:')),
                ('child_tasks', models.ManyToManyField(blank=True, related_name='task_child_tasks', to='api.SubTaskItem')),
                ('tags', models.ManyToManyField(blank=True, related_name='task_tags', to='api.TagItem')),
            ],
        ),
        migrations.AddField(
            model_name='subtaskitem',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='subtask_tags', to='api.TagItem'),
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Project ID:')),
                ('name', models.CharField(max_length=100, verbose_name='Project Name:')),
                ('description', models.TextField(max_length=300, verbose_name='Project Description:')),
                ('start_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date:')),
                ('due_date_time', models.DateTimeField(verbose_name='Due Date:')),
                ('duration', models.DurationField(verbose_name='Duration:')),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=6, verbose_name='Priority:')),
                ('project_status', models.CharField(choices=[('Not Started', 'Not Started'), ('Upcoming', 'Upcoming'), ('In Progress', 'In Progress'), ('Due Soon', 'Due Soon'), ('Overdue', 'Overdue')], default='In Progress', max_length=11, verbose_name='Project Status:')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Added:')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified:')),
                ('child_tasks', models.ManyToManyField(blank=True, related_name='project_child_tasks', to='api.TaskItem')),
            ],
        ),
    ]