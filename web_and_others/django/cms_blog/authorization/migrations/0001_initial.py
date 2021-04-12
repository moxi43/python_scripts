# Generated by Django 3.0.3 on 2020-02-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=42, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('last_login', models.DateTimeField(default='2020-02-09 19:04:52.7')),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(default='man', max_length=10, verbose_name='first_name')),
                ('last_name', models.CharField(default='man', max_length=10)),
                ('email', models.EmailField(default='some@gmail.com', max_length=254)),
                ('date_joined', models.DateTimeField(default='2020-02-09 19:04:52.7')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]