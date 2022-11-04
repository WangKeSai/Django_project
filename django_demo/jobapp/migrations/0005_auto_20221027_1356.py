# Generated by Django 3.2 on 2022-10-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0004_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=20, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='evaluation',
            field=models.TextField(verbose_name='自我评价'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='major',
            field=models.CharField(max_length=20, verbose_name='所学专业'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='project',
            field=models.CharField(max_length=20, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='project_content',
            field=models.TextField(verbose_name='项目描述'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='project_duty',
            field=models.CharField(max_length=20, verbose_name='项目职务'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='project_endtime',
            field=models.DateField(verbose_name='项目结束时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='project_starttime',
            field=models.DateField(verbose_name='项目开始时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school',
            field=models.CharField(max_length=20, verbose_name='学校名称'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school_endtime',
            field=models.DateField(verbose_name='毕业时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school_starttime',
            field=models.DateField(verbose_name='入学时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_img',
            field=models.BinaryField(verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='work',
            field=models.CharField(max_length=20, verbose_name='公司名称'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='work_content',
            field=models.TextField(verbose_name='工作内容'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='work_duty',
            field=models.CharField(max_length=20, verbose_name='工作岗位'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='work_endtime',
            field=models.DateField(verbose_name='工作结束时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='work_starttime',
            field=models.DateField(verbose_name='工作开始时间'),
        ),
    ]