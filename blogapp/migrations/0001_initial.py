# Generated by Django 5.1.7 on 2025-03-26 05:46

import django.db.models.deletion
import django.utils.timezone
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mediamanager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('sort', models.IntegerField()),
                ('cuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_cuser', to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mediamanager.mediaitem')),
                ('muser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_muser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('sort', models.IntegerField()),
                ('cuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_cuser', to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mediamanager.mediaitem')),
                ('muser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_muser', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('product_name', models.CharField(max_length=500)),
                ('full_name', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('message', models.TextField()),
                ('cuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_cuser', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_muser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('New', 'New'), ('Followup', 'Followup'), ('Cancelled', 'Cancelled'), ('Converted', 'Converted'), ('Closed', 'Closed')], default='New', max_length=200)),
                ('cuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_cuser', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_base_muser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalBlog',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(blank=True, editable=False)),
                ('mdate', models.DateTimeField(blank=True, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('sort', models.IntegerField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blogapp.blogcategory')),
                ('cuser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mediamanager.mediaitem')),
                ('muser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical blog',
                'verbose_name_plural': 'historical blogs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalBlogcategory',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(blank=True, editable=False)),
                ('mdate', models.DateTimeField(blank=True, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('sort', models.IntegerField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cuser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mediamanager.mediaitem')),
                ('muser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical blogcategory',
                'verbose_name_plural': 'historical blogcategorys',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalBookings',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(blank=True, editable=False)),
                ('mdate', models.DateTimeField(blank=True, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('product_name', models.CharField(max_length=500)),
                ('full_name', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('message', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cuser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical bookings',
                'verbose_name_plural': 'historical bookingss',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalContacts',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status_flag', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('cdate', models.DateTimeField(blank=True, editable=False)),
                ('mdate', models.DateTimeField(blank=True, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('New', 'New'), ('Followup', 'Followup'), ('Cancelled', 'Cancelled'), ('Converted', 'Converted'), ('Closed', 'Closed')], default='New', max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cuser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('muser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical contacts',
                'verbose_name_plural': 'historical contactss',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
