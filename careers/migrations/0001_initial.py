# Generated by Django 5.1.7 on 2025-03-26 05:46

import django.db.models.deletion
import django.utils.timezone
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalJobCategory',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(blank=True, editable=False)),
                ('mdate', models.DateTimeField(blank=True, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=200)),
                ('is_suspended', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cuser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical job category',
                'verbose_name_plural': 'historical job categorys',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=200)),
                ('is_suspended', models.BooleanField(default=False)),
                ('cuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_cuser', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_muser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalJobListing',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(blank=True, editable=False)),
                ('mdate', models.DateTimeField(blank=True, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('job_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('no_of_positions', models.IntegerField()),
                ('applications', models.IntegerField(default=0)),
                ('posted_date', models.DateTimeField(blank=True, editable=False)),
                ('deadline', models.DateTimeField()),
                ('is_suspended', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cuser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='careers.jobcategory')),
            ],
            options={
                'verbose_name': 'historical job listing',
                'verbose_name_plural': 'historical job listings',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('job_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('no_of_positions', models.IntegerField()),
                ('applications', models.IntegerField(default=0)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('is_suspended', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careers.jobcategory')),
                ('cuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_cuser', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_muser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField()),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('is_suspended', models.BooleanField(default=False)),
                ('cuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_cuser', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_muser', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careers.joblisting')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalJobApplication',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(blank=True, editable=False)),
                ('mdate', models.DateTimeField(blank=True, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('resume', models.TextField(max_length=100)),
                ('cover_letter', models.TextField()),
                ('applied_date', models.DateTimeField(blank=True, editable=False)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('is_suspended', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cuser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='careers.joblisting')),
            ],
            options={
                'verbose_name': 'historical job application',
                'verbose_name_plural': 'historical job applications',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
