from django.db import models


# Create your models here.
class Jobs(models.Model):
    id = models.AutoField
    job_name = models.TextField()
    company_name = models.TextField()
    provide_salary = models.TextField()
    work_area = models.TextField()
    company_type = models.TextField()
    job_welf = models.TextField()
    company_size = models.TextField()
    company_ind = models.TextField()
    release_date = models.TextField()
    attribute = models.TextField()
    job_link = models.TextField()
    company_link = models.TextField()
    company_cont = models.ForeignKey(to='CompanyInfo', on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = "jobs"


class Users(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=20)
    password = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"


class UserInfo(models.Model):
    user_img = models.BinaryField(verbose_name="头像")
    name = models.CharField(max_length=20, verbose_name="姓名")
    phone = models.CharField(max_length=20, verbose_name="手机号")
    email = models.CharField(max_length=20, verbose_name="邮箱")
    gender = models.CharField(max_length=10, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    school = models.CharField(max_length=20, verbose_name="学校名称")
    school_starttime = models.DateField(verbose_name="入学时间")
    school_endtime = models.DateField(verbose_name="毕业时间")
    major = models.CharField(max_length=20, verbose_name="所学专业")
    project = models.CharField(max_length=20, verbose_name="项目名称")
    project_starttime = models.DateField(verbose_name="项目开始时间")
    project_endtime = models.DateField(verbose_name="项目结束时间")
    project_duty = models.CharField(max_length=20, verbose_name="项目职务")
    project_content = models.TextField(verbose_name="项目描述")
    work = models.CharField(max_length=20, verbose_name="公司名称")
    work_starttime = models.DateField(verbose_name="工作开始时间")
    work_endtime = models.DateField(verbose_name="工作结束时间")
    work_duty = models.CharField(max_length=20, verbose_name="工作岗位")
    work_content = models.TextField(verbose_name="工作内容")
    evaluation = models.TextField(verbose_name="自我评价")
    user = models.OneToOneField(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_info"


class CompanyInfo(models.Model):
    id = models.AutoField
    company_name = models.TextField()
    company_ind = models.TextField(verbose_name="公司介绍")

    class Meta:
        db_table = "company_info"


# class JobInfo(models.Model):
#     class Meta:
#         db_table = "job_info"
