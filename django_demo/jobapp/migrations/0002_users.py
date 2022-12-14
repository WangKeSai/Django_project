# Generated by Django 3.2 on 2022-10-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('user_img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('school', models.CharField(max_length=20)),
                ('school_starttime', models.DateField()),
                ('school_endtime', models.DateField()),
                ('major', models.CharField(max_length=20)),
                ('project', models.CharField(max_length=20)),
                ('project_starttime', models.DateField()),
                ('project_endtime', models.DateField()),
                ('project_duty', models.CharField(max_length=20)),
                ('project_content', models.TextField()),
                ('work', models.CharField(max_length=20)),
                ('work_starttime', models.DateField()),
                ('work_endtime', models.DateField()),
                ('work_duty', models.CharField(max_length=20)),
                ('work_content', models.TextField()),
                ('evaluation', models.TextField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
